(pr-how-to)=
# How to use this book

While we provide a rendered version of the interactive material, in some cases the outputs of the code may be hidden by default. To experiment and interact with the Python code, we suggest the following pathways to do this:

## Public users: interact through a cloud-based Binder service 
This will work well for many of the executable notebooks. We use [binder](https://mybinder.readthedocs.io/en/latest/index.html) to create custom computing environments to run executable content online. Among the available BinderHubs, we use those with vCPU >= 2 and RAM (GB) >=8. This recent [GitHub comment](https://github.com/pangeo-data/pangeo-binder/issues/195#issuecomment-989107771) indicates some current BinderHubs available.   

## Local conda environment
We provide two options to run exactly the same environments from (1) a single file for all executable notebooks or (2) individual file by executable notebook. 

If you aren't familiar with Anaconda or GitHub, we suggest exploring the following resources:

* The [conda package manager](https://docs.conda.io/en/latest/)
* Basic knowledge of [version control with git](https://git-scm.com)
* (optional) Basic knowledge of [Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/)

### Single file for all executable notebooks
This route allows running all the notebooks using a single computing environment. 

The first step is to clone the [source repository for this book on github](https://github.com/alan-turing-institute/environmental-ds-book).

Once you have the source repo, the following commands will create a self-contained
[conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)
with everything you need to run the notebooks (Mac, Linux and Windows).

From within the `enviromental-ds-book` directory in your favorite terminal, do this:

```
conda env create --file environment.yml
conda activate envds-book
```

Now you are ready to run `jupyter lab` in your terminal to work with various notebooks and projects from a single environment file on your local computer.

Then find all the executable notebooks `*.ipynb` files in `enviromental-ds-book/book`

:::{note}
You may find it useful to do all your work in a separate git branch,  and leave your `main` branch untouched, so you can keep it up to date with the source repository.
:::

### Individual file by executable notebook
While the same environment for various notebooks sounds great, the main drawback is longer waiting times to get all dependencies working without conflicts. 

If the single environment file does not work in your machine, or you're only interested to explore a particular notebook, we also provide individual environments files in [_environments](./../_environments)

For each executable notebook, we provide lock files for installing exactly the same package across different operating system. For instance, for recreating the environment of the notebook [`forest-modelling-treecrown_deepforest`](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/forest/modelling/forest-modelling-treecrown_deepforest.ipynb) on Linux:

```
conda create -n forest-modelling-treecrown_deepforest --file=https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/book/_environments/forest-modelling-treecrown_deepforest/conda-linux-64.lock
```

Certain notebooks require to install some packages via `pip`. If this is the case, you'll find a `requirements.txt` file which can be run:

```
pip install -r https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/book/_environments/forest-modelling-treecrown_deepforest/requirements.txt
```

For Linux, MacOSX, or Windows, if you're not concerned with package versions and simply want to have the same libraries installed on your system you can run:

```
wget https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/book/_environments/forest-modelling-treecrown_deepforest/environment.yml
conda env create environment.yml
```

Now you are ready to run `jupyter notebook` in your terminal to work with a particular notebook with its corresponding environment file on your local computer.
