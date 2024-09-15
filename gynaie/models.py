base_model = {
    'GynAIe-preview-clip-vit-large-patch14-336': {
        'model_id': {
            'Linux': 'kuri54/GynAIe-preview-clip-vit-large-patch14-336-8bit',
            'Apple Silicon Mac': 'kuri54/mlx-GynAIe-preview-clip-vit-large-patch14-336'
            },
            'label':['a image of a normal', 'a image of a abnormal']},
    }

def get_supported_models(platform_info):
    supported_models = []

    for model_name , model_data in base_model.items():
        if platform_info in model_data['model_id']:
            supported_models.append(model_name)

    return supported_models