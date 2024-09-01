# GynAIe
<div align="center">

<picture>
  <source media="(prefers-color-scheme: light)" srcset="/assets/GynAIe_logo.PNG">
  <img alt="exo logo" src="/assets/GynAIe_logo.PNG" width="30%" height="30%">
</picture> 

**"Magical AI for women worldwide."**

</div>

**GynAIe**: Pronounced "Genie" (/ˈdʒiːni/)  
The name **"GynAIe"** is a blend of **"Gynecology"** and **"AI"**. We've chosen to pronounce it as "Genie" (/ˈdʒiːni/) to emphasize the magical assistance it provides in the field of gynecology.


## 🤩 Updates
- **`2024/09/01`**: Licensed under **Apache v2**. Please note, the model itself is licensed under **CC-BY-NC-SA-4.0**, so please be cautious about its use.
- **`2024/08/30`**: Released model! [Hugging Face Model](https://huggingface.co/kuri54/GynAIe-preview-clip-vit-large-patch14-336-8bit)
- **`2024/08/28`**: Released [part of the Usage](#generating-tile-images) documentation. This includes instructions on generating tile images from WSI using specified parameters. More detailed usage instructions will be provided in future updates.
- **`2024/08/25`**: Added paper highlights and images!
- **`2024/08/24`**: The logo has been uploaded!
- **`2024/08/22`**: Our paper entitled "Enhancing cervical cancer cytology screening via artificial intelligence innovation" has been published in *Scientific Reports*. You can access the paper [here](https://doi.org/10.1038/s41598-024-70670-6)!

## 🙇🏻‍♂️ Note to Users
Please be advised that this project is managed solely by me. As such, updates to the code and responses to issues may take some time. I appreciate your patience and understanding as I work to make this project as useful and robust as possible. Your feedback and contributions are always welcome and highly valued.

Thank you for your support and understanding.

## ✨ Highlights
- Developed an AI-integrated workflow for cervical cytology screening that reduces screening time to approximately 10 seconds per case and significantly lessens the workload on cytologists.
- Implemented a visual language model that enhances the identification of high-risk cases by prioritizing cases based on anomaly scores and targeting review efforts accordingly.
- Demonstrated the potential of AI technology to improve the efficiency and accuracy of cytological examinations, contributing to faster diagnosis and treatment of cervical cancer.

<p>
    <picture>
        <img alt="overview workflow" src="assets/Overview_workflow.jpg" width="90%" height="90%">
    </picture>
</p>

<p>
    <picture>
        <img alt="result" src="assets/Result.jpg" width="70%" height="70%">
    </picture>
</p>

## Usage
It is recommended to use a virtual environment of your choice, such as Docker.

### Generating Tile Images
Access this [link](https://github.com/kuri54/Preprocessing-WSI) to generate tile images from WSI (Whole Slide Image).  
This process can also be done on a local machine, but the processing speed will depend on the CPU performance.  
<br>
The tile images in the paper were generated with the following parameters:  
```bash
python preprocessing.py -u 0.3 -s 1024  
```
<br>

**More usage instructions will be updated periodically. Please generate the tile images and stay tuned!**

## 📆 TODO
- [x] Publication of a paper
- [x] Add paper highlights and images
- [x] Release model
- [x] Granting of a license
- [ ] Release usage documentation
  - [ ] Add requirements
  - [x] Tile image generation code
  - [ ] Screening code
- [ ] Release Streamlit-based screening workflow

## 🎉 Citation

```
@article{kurita2024gynaie,
         title={Enhancing cervical cancer cytology screening via artificial intelligence innovation}, 
         author={Yuki Kurita et al.},
         year={2024},
         journal={Scientific Reports},
         doi={10.1038/s41598-024-70670-6}
}
```
