from setuptools import setup, find_packages

install_requires = [
    'accelerate==0.34.2',
    'natsort==8.4.0',
    'torch==2.3.0',
    'torchaudio==2.3.0',
    'torchvision==0.18.0',
    'transformers==4.44.2',
    'streamlit==1.39.0'
    'bitsandbytes',
    'matplotlib',
    'mlx',
    'numpy',
    'pandas',
    'pillow',
    'rich',
    'scikit-learn',
    'seaborn',
]

setup(
    name='GynAIe',
    version='0.0.1',
    packages=find_packages(),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'gynaie-run = gynaie.main:run',
            'gynaie-viewer = gynaie.viewer.viewer_run:run'
        ]
    }
)
