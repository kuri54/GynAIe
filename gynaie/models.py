base_model = {
    'GynAIe-preview-clip-vit-large-patch14-336-8bit': {'model_id': 'kuri54/GynAIe-preview-clip-vit-large-patch14-336-8bit',
                                                       'label':['a image of a normal', 'a image of a abnormal']},
    }

def get_supported_models():
    return list(base_model.keys())