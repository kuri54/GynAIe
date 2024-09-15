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
- **`2024/09/06`**: Released the [MLX Version Model](https://huggingface.co/kuri54/mlx-GynAIe-preview-clip-vit-large-patch14-336)! Alongside this release, we've conducted significant code revisions to optimize compatibility and performance. As a result, GynAIe is now operational on Apple Silicon Macs!
- **`2024/09/06`**: Released instructions for using custom parameters! Detailed steps on how to apply these parameters in the `main.py` script are available in the [Usage section](#%EF%B8%8F-customizable-parameters) of our README.
- **`2024/09/04`**: Released the code for conducting screening! Detailed steps on how to run the script are now available in the [Usage section](#-screening) of our README.
Please refer to the Usage section to ensure your setup is correct and to effectively use the screening code.
- **`2024/09/01`**: Licensed under **Apache v2**. Please note, the model itself is licensed under **CC-BY-NC-SA-4.0**, so please be cautious about its use.
- **`2024/08/30`**: Released model! [Hugging Face Model](https://huggingface.co/kuri54/GynAIe-preview-clip-vit-large-patch14-336-8bit)
- **`2024/08/28`**: Released [part of the Usage](#%EF%B8%8F-generating-tile-images) documentation. This includes instructions on generating tile images from WSI using specified parameters. More detailed usage instructions will be provided in future updates.
- **`2024/08/25`**: Added paper highlights and images!
- **`2024/08/24`**: The logo has been uploaded!
- **`2024/08/22`**: Our paper entitled "Enhancing cervical cancer cytology screening via artificial intelligence innovation" has been published in *Scientific Reports*. You can access the paper [here](https://doi.org/10.1038/s41598-024-70670-6)!

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

## 💡Usage
It is recommended to use a virtual environment of your choice, such as Docker.

### 👀 Usage Overview

To effectively utilize the screening code, follow these major steps:

1. [**Generating tile images**](#%EF%B8%8F-generating-tile-images): Start by generating tile images from your source data, which will be used for the screening process.
2. [**Setup**](#-setup): Prepare your environment and organize the necessary input data, including the tile images, as outlined in the setup instructions.
3. [**Running the code**](#-screening): Execute the `main.py` script to perform the screening based on the prepared inputs.
4. [**Checking the results**](#-screening): After running the script, examine the outputs in the `result` directory to evaluate the screening outcomes.
5. [**Using custom parameters**](#%EF%B8%8F-customizable-parameters): Customize your screening process by adjusting various parameters available in the `main.py` script. This section guides you on how to modify parameters such as model selection, batch size, number of workers, and sorting criteria to tailor the analysis to your specific requirements.  

Each of these steps is detailed further in the following sections, ensuring you have all the information needed to successfully deploy and use the screening model.  
<br>

### ✂️ Generating Tile Images
Access this [link](https://github.com/kuri54/Preprocessing-WSI) to generate tile images from WSI (Whole Slide Image).  
This process can also be done on a local machine, but the processing speed will depend on the CPU performance.  
<br>
The tile images in the paper were generated with the following parameters:  
```bash
python preprocessing.py -u 0.3 -s 1024  
```
<br>

### 💻 Setup
**Optional:**　For Apple Silicon Mac  
To set up the environment on Apple Silicon Macs, follow these steps. You can install Python using Homebrew, a package manager for macOS.
Open the Terminal and run the following command:
```bash
brew install python
```

This will install the latest version of Python that is compatible with Apple Silicon. After installation, you can verify the Python version by running ```python3 --version``` in the Terminal to ensure it’s correctly installed.

1. **Installation**: 
   - Clone this repository.
   - Navigate to the cloned directory.
      ```bash
      cd GynAIe
      ```
   - **Optional:**　Setup a virtual environment (if not using Docker):  
     It is recommended to set up a virtual environment to manage dependencies locally without affecting the rest of your system. Use the following commands to create and activate a virtual environment.
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Install the necessary libraries and dependencies as listed in `requirements.txt`.
      ```bash
      pip install -r requirements.txt
      ```

3. **Arranging tile images and creating a CSV file**
   -  Organize the generated tile images as illustrated below:
       <pre>
        .
        └── GynAIe/
            └── input/
                └── 20240904/
                    ├── c202400001/
                    │   ├── c202400001_1.jpg
                    │   ├── c202400001_2.jpg
                    │   └── c202400001_3.jpg
                    │
                    ├── c202400002/
                    │   ├── c202400002_1.jpg
                    │   ├── c202400002_2.jpg
                    │   └── c202400002_3.jpg
                    │
                    └── 20240904.csv
        </pre>
    
    - It is recommended to create a directory named `input`, under which you should place directories containing tile images for each screening case group.

    - Create a CSV file detailing the specifics of each case and place it in the directory where the tile images are stored. Ensure the following for the CSV file:

     - The CSV should include the following details:

     - Ensure that the column names in the CSV file are as follows: 
        | case       | age |
        | ---------- | --- |
        | c202400001 | 35  |
        | c202400002 | 88  |
<br>

### 🔬 Screening
1. Running the code
    To execute the model, use the following command in your terminal. This command runs the `main.py` script and specifies the input directory where your tile images are stored:

    ```bash
    python3 main.py --input_dir input/20240904
    ```

2. Checking the results
   After successfully running `main.py`, a directory named `result` will be created. This directory contains the following outputs:
    
    - **Sorted images**: Images displaying the sorted cases based on the screening results, illustrating how each case ranks according to the evaluated criteria.
    - **result.csv**: A data file containing all the decision data for each image.
    - **calculated.csv**: A file derived from `result.csv` that calculates additional metrics such as anomaly scores.

    **Please review the contents of the `result` directory to evaluate the screening outcomes.**
<br>

### 🛠️ Customizable parameters

<details><summary>The following parameters can be adjusted to customize the behavior of the script according to your specific needs:</summary>

- **`--model_name`**: Specifies the model to be used for processing. Default is **`GynAIe-preview-clip-vit-large-patch14-336-8bit`**. You can switch to alternative models as they become available in future updates.

- **`--batch_size`**: Sets the number of images processed in one batch. Default is `32`. Adjusting the batch size can help balance between memory usage and processing speed.

- **`--num_workers`**: Determines the number of worker processes for loading data. Default is half of the available CPU cores, calculated as `os.cpu_count()//2`. This setting can optimize data loading efficiency and overall processing speed.

- **`--min_image_count`**: Sets the minimum number of images required to avoid being classified as inadequate. Default is `50`. Cases with fewer images than this number are marked as inadequate. This parameter helps ensure that each case analyzed has sufficient data to maintain quality in the screening results.

- **`--sort_by`** and **`--sort_ascending`**: Controls the sorting of results. By default, results are sorted by `anomaly_score` in descending order, and by age in ascending order if scores are close. Sorting by `anomaly_score` is crucial, and you can adjust ascending or descending order based on your preference. It is also possible to include additional parameters for sorting; in such cases, ensure that corresponding columns are created in the CSV file.

    - Sorting by custom parameters in the CSV file:  
      You can sort the results using any parameter included in your CSV file. To accomplish this, first ensure that the desired column is present in the CSV file. Then specify the column name using the `--sort_by` option and set the sort order with `--sort_ascending`.

       **Important Notes**:
        - `anomaly_score` should always be used as the primary sorting criterion to maintain consistency in results prioritization.
        - Sorting criteria should be specified in a list format. This ensures that the sorting logic is applied correctly and in the intended order.

       **Example**:
        If you want to sort by a custom parameter called `new_column`, you can use the following command:
        
        | case       | age | new_column |
        | ---------- | --- | ---------- |
        | c202400001 | 35  |     1      |
        | c202400002 | 88  |     2      |

        ```bash
          python3 main.py --sort_by ['anomaly_score', 'age', 'nwe_column'] --sort_ascending [False, True, True]
        ```
</details>
<br>

## 📆 TODO
- [x] Publication of a paper
- [x] Add paper highlights and images
- [x] Release model
- [x] Release MLX version model
- [x] Granting of a license
- [x] Release usage documentation
  - [x] Add requirements
  - [x] Tile image generation code
  - [x] Screening code
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
