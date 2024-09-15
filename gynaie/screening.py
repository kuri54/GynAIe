import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset
from PIL import Image
from rich.progress import track
from sklearn.metrics import *
from transformers import AutoModel, AutoProcessor
from gynaie.check import log_message

class CLIPDataset(Dataset):
    def __init__(self, df, label, processor):
        self.df = df
        self.label = label
        self.processor = processor

    def __len__(self):
        return len(self.df.path.values)

    def __getitem__(self, idx):
        image_path = self.df.path.values[idx]

        return self.processor(text=self.label, images=Image.open(image_path), return_tensors="pt", padding=True)

class Evaluater():
    def __init__(self, df, model_id, label, batch_size, num_workers):
        self.df = df
        self.model_id = model_id
        self.label = label
        self.batch_size = batch_size
        self.num_workers = num_workers

    def create_model_preprocess(self):
        model = AutoModel.from_pretrained(self.model_id, device_map='auto')
        processor = AutoProcessor.from_pretrained(self.model_id)

        return model, processor

    def create_dataloader(self, processor):
        dataset = CLIPDataset(self.df, self.label, processor)
        log_message(f'Number of images processes: {len(dataset)}', 'notice')

        data_loader = DataLoader(dataset,
                                 batch_size=self.batch_size,
                                 pin_memory=True,
                                 num_workers=self.num_workers
                                 )

        return data_loader

    def evaluate(self, data_loader, model):
        result_df = None

        pred_labels = []
        pred_scores = []

        # for inputs in tqdm(data_loader):
        for inputs in track(data_loader):
            if next(model.parameters()).device.type == 'mps':
                inputs.to('mps')

            with torch.no_grad():
                outputs = model(pixel_values=inputs['pixel_values'].squeeze(),
                                input_ids=inputs['input_ids'][0].squeeze()
                                )

                logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
                probs = logits_per_image.softmax(dim=1).cpu().detach().numpy()
                predicted_class_idx = [prob.argmax(-1).item() for prob in probs]

                pred_labels.extend(self.label[pred_class] for pred_class in predicted_class_idx)
                pred_scores.extend(probs[i][pred_class] for i, pred_class in enumerate(predicted_class_idx))

        result_df = pd.DataFrame(data={f'pred_label': pred_labels, f'pred_score': pred_scores})

        return pd.concat([self.df, result_df], axis=1)

    def run_evaluation(self):
        model, processor = self.create_model_preprocess()
        data_loader = self.create_dataloader(processor)
        result_df = self.evaluate(data_loader, model)

        return result_df
