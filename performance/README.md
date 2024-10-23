# Model performance details

## Details of the dataset used

- **Number of cases**: 10
- **Total number of tile images**: 4,323

## Results

| Model name                                                                                                                     | Quantization       | Labels used         | Inference time<br>RTX A6000 | Inference time<br>M2 Ultra 192GB | Results images* |
| :----------------------------------------------------------------------------------------------------------------------------- | :----------------: | :-----------------: | :-------------------------: | :------------------------------: | :-------------: |
| [GynAIe-preview-clip-vit-large-patch14-336-8bit](https://huggingface.co/kuri54/GynAIe-preview-clip-vit-large-patch14-336-8bit) | :white_check_mark: | normal' 'abnormal'  | 00:01:22                    | -                                |                 |
| [mlx-GynAIe-preview-clip-vit-large-patch14-336](https://huggingface.co/kuri54/mlx-GynAIe-preview-clip-vit-large-patch14-336)   |                    | 'normal' 'abnormal' | -                           | 00:02:45                         |                 |
| [GynAIe-preview-B16-5k](https://huggingface.co/kuri54/GynAIe-preview-B16-5k)                                                   |                    | 'normal' 'anomaly'  | 00:00:13                    | -                                |                 |
| [mlx-GynAIe-preview-B16-5k](https://huggingface.co/kuri54/mlx-GynAIe-preview-B16-5k)                                           |                    | 'normal' 'anomaly'  | -                           | 00:00:36                         |                 |

*The images linked here represent the sorted results of cervical LBC from 938 cases used in the study.
