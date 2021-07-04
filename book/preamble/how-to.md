How to use this book
=======================

:::{note}
Under construction
:::

While we provide a rendered version of the interactive material, in some cases the outputs of the code may be hidden by default. To experiment and interact with the Python code, we suggest the following pathways to do this:

# Public users: interact through a cloud-based Binder service 
This will work well for many of the simple examples. We use the [Pangeo binder](https://binder.pangeo.io/) which comes with most of the scientific packages in Python use in the examples. In addition, it allows using distributed processing which in certain examples accelerates computing the results. 

#Anyone: run the code in your own Python environment
Following the guidelines of Brian Rose for The Climate Laboratory book, you will need to:

You will need the following:

* The [conda package manager](https://docs.conda.io/en/latest/)
* Basic knowledge of [version control with git](https://git-scm.com)
* Basic knowledge of [Jupyter notebooks](https://jupyter-notebook.readthedocs.io/en/stable/)

The first step is to clone the [source repository for this book on github](https://github.com/acocac/environmental-ai-book).

Once you have the source repo, the following commands will create a self-contained
[conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html)
with everything you need to run the notebooks (Mac, Linux and Windows).

From within the `enviromental-ai-book` directory in your favorite terminal, do this:

```
conda env create --file environment.yml
conda activate envai-book
```

Then find all the Jupyter notebook `*.ipynb` files in `enviromental-ai-book/book`

You may find it useful to do all your work in a separate git branch,
and leave your `main` branch untouched, so you can keep it up to date with
the source repository.