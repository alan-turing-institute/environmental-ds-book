(pr-how-to)=
# How to use EDS book notebooks

While we provide a rendered version of the interactive material, in some cases the outputs of the code may be hidden by default. 
To experiment and interact with the executable EDS book notebooks, we suggest the following pathways to do this:

## Public users: interact through a cloud-based Binder service 
This will work well for many of executable notebooks.
Each notebook has a [binder](https://mybinder.readthedocs.io/en/latest/index.html) badge which builds the virtual computing environment with specific dependencies.
Among the available BinderHubs, we use those with vCPU >= 2 and RAM (GB) >=8. 
This [GitHub comment](https://github.com/pangeo-data/pangeo-binder/issues/195#issuecomment-989107771) indicates some current BinderHubs available.   

## Local conda environment
The README across all notebooks repositories provides instructions on how to run the same environment locally using conda. 

If you aren't familiar with Anaconda or GitHub, we suggest exploring the following resources:

* The [conda package manager](https://docs.conda.io/en/latest/)
* Basic knowledge of [version control with git](https://git-scm.com)
* (optional) Basic knowledge of [Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/)

Notebooks repositories also provide lock files for installing exactly the same package across different operating system. 
For instance, for recreating the environment of the notebook [`forest-modelling-treecrown_deepforest`](https://github.com/eds-book-gallery/forest-modelling-treecrown_deepforest) on Linux:

```
conda create -n forest-modelling-treecrown_deepforest --file=https://raw.githubusercontent.com/eds-book-gallery/forest-modelling-treecrown_deepforest/main/.lock/conda-linux-64.lock
```

Certain notebooks require to install some packages via `pip`. If this is the case, you'll find a `requirements.txt` file which can be run:

```
pip install -r https://raw.githubusercontent.com/eds-book-gallery/forest-modelling-treecrown_deepforest/main/.lock/requirements.txt
```

For Linux, MacOSX, or Windows, if you're not concerned with package versions and simply want to have the same libraries installed on your system you can run:

```
wget https://raw.githubusercontent.com/eds-book-gallery/forest-modelling-treecrown_deepforest/main/.binder/environment.yml
conda env create environment.yml
```

Now you are ready to run `jupyter notebook` in your terminal to work with a particular notebook with its corresponding environment file on your local computer.