(templates-eic-readme-python)=

# Title

<p align="center">
    <a href="https://github.com/eds-book/[repository name]/actions/workflows/monthly-build.yaml/badge.svg">
        <img alt="Continuous integration badge" src="https://github.com/eds-book/[repository name]/actions/workflows/monthly-build.yaml/badge.svg">
    </a>
    <a href="http://mybinder.org/v2/gh/eds-book/[repository name]/main?labpath=notebook.ipynb">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg">
    </a>
    <a href="https://doi.org/10.5281/zenodo.XXX">
        <img alt="doi" src="https://zenodo.org/badge/XXX.svg">
    </a>
    <a href="https://github.com/eds-book/[repository name]/pull/X">
        <img alt="notebook review" src="https://img.shields.io/badge/view-review-purple">
    </a>
</p>

## How to run

## Running on Binder
The notebook is designed to be launched from Binder. 

Click the **Launch Binder** button at the top level of the repository

## Running locally
You may also download the notebook from GitHub to run it locally:
1. Open your terminal

2. Check your conda install with `conda --version`. If you don't have conda, install it by following these instructions (see [here](https://docs.conda.io/en/latest/miniconda.html))

3. Clone the repository
    ```bash
    git clone https://github.com/eds-book/[repository name].git
    ```

4. Move into the cloned repository
    ```bash
    cd [repository name]
    ```

5. Create and activate your environment from the `.binder/environment.yml` file
    ```bash
    conda env create -f .binder/environment.yml
    conda activate [repository name]
    ```  

6. Launch the jupyter interface of your preference, notebook, `jupyter notebook` or lab `jupyter lab`