(pb-guidelines-authors)=

# Guide for Authors
Welcome to the guide for notebooks authors of the EDS book! 

Before you begin this process, please be sure to [understand how the publication process works](#contribute-notebooks).

We have a [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) which is mandatory for everyone involved in the review process of our notebooks.

Below you will find the main steps we suggest to follow to submit a notebook to EDS book for peer review.

## Scope and Aims
Thank you for considering submitting a notebook to EDS book.
Our review process aims to be open, collaborative, transparent and inclusive. 
We therefore welcome authors from a diversity of background and with varying levels of programming/domain expertise.

## Notebook Idea
In this step, we provide a transparent discussion space to validate notebooks ideas (NBI) before their review. 

Submitting a NBI is as simple as:

* Open a NBI [issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose).
* Fill the NBI template with some description of the notebook and information about the input data and target theme.
* Wait for Editors-in-Chief (EiC) and/or community (optional) to provide feedback.
* Once you get a minimal and satisfactory feedback, we encourage to start preparing the notebook repository.

## Preparation
After validating the notebook idea, a first draft of the notebook should be created by using a notebook repository template according to the target programming language:
* [Python](https://github.com/eds-book/template_python)
* [R](https://github.com/eds-book/template_r)
* [Julia](https://github.com/eds-book/template_julia)

The repository templates are adapted from [2i2c hub-user-image-template](https://github.com/2i2c-org/hub-user-image-template). 
The corresponding author should open a Pull Request to start editing the notebook and dependencies files. 
Within each PR, a comment will be added containing "Test this PR on Binder" badge. 

Some general guidelines are:
* Fill the information header according to your use case. Feel free to guide from previous published notebooks, see for instance the [IceNet notebook](https://edsbook.org/notebooks/gallery/ac327c3a-5264-40a2-8c6e-1e8d7c4b37ef/notebook.html).
* Change the structure of the remaining sections of the notebook according to your preference.
  * We advise following the 10 rules of compelling notebooks provided by the EarthCube initiative available in their [Notebook Template](https://github.com/earthcube/NotebookTemplates/blob/main/EC_05_Template_Notebook_for_EarthCube_Long_Version.ipynb) (section `Data processing and analysis`).
* For `python` packages, we suggest exploring the [Pangeo stack](https://pangeo.io/). The Pangeo community curates a wide diversity of environments in the `pangeo-docker-images` [repository](https://github.com/pangeo-data/pangeo-docker-images/tree/master/pangeo-notebook). 
  * For notebooks, we suggest using the `pangeo-notebook` conda environment available [here](https://github.com/pangeo-data/pangeo-docker-images/blob/master/pangeo-notebook/environment.yml). The environment can be installed in your system using `conda env create -f environment.yml`.
* Test the notebook is working according to the Binder badge in the PR.
* For notebooks showcasing deep learning models, the public Binder does not provide GPU support, so we suggest testing the notebook works with `cpu` when predicting from the pretrained models. 

When the minimal working version of the notebook is ready, authors should tag EiC in the PR with the latest Binder badge.
EiC will check how reproducible is the notebook and its feasibility for the reviewing stage. 

After EiC's approval of the draft version of the notebook, the EiC will fork the notebook repository to the [eds-book](https://github.com/eds-book) organisation. 

EiC will assist you to prepare the notebook repository for the review process.

## Pre-review
EiC will open a PRE-REVIEW issue where a handling editor and authors suggest reviewers. 
The editor can give initial directions to authors for improving the notebook, especially if the notebook lacks some requested sections.
Once reviewers agreed on the revision, EiC opens a REVIEW issue. 

## Review
The REVIEW issue aims to be the key space where editor will moderate timings and high-level conversation between authors and reviewers.

```{important}
Reviewers will be asked to provide review feedback as comments on the REVIEW issue or directly to the notebook repo within **2 weeks**.
Authors should respond to reviewers’ comments within **2 weeks** of the last-submitted review.
Please contact the editor directly or in the REVIEW issue thread to inform possible delays.
```

Authors should address reviewers suggestions according to their relevance.
Each reviewer is guided by a checklist which facilitate to evaluate the notebook.
Reviewers are encouraged to make detailed comments directly to the notebook repo.
To facilitate the conversation, EiC opens a `review` PR in the notebook repository where authors and reviewers carry out a detailed discussion through ReviewNB, a third-party plugin in GitHub for displaying and commenting Jupyter Notebooks (see further details [here](../about/notebooks-technologies.md)).
Authors should implement relevant changes in the notebook repository hosted in their personal GitHub account, and submit changes to the `review` branch created by EiC (for example, see [here](https://github.com/eds-book/67a1e320-7c47-4ea9-8df8-e868326bc90b/pull/6) a PR submitted from the author of the IceNet Python API notebook).
EiC will merge changes into the `review` PR.
The editor should ask reviewers to re-evaluate the notebook.

Once reviewers recommend the notebook for publication, the editor pings EiC to start the post-print stage.

## Post-print
EiC will lead publishing asking authors to proof-read the notebook and indicate any remaining typos, badly formed citations, awkward wording, etc.

## Publication
While EiC will announce the notebook in the EDS book social accounts, authors should promote the published notebook in their communication channels.

Some authors have promoted EDS notebooks in LinkedIn, etc. 
Others have added them to their online CV and/or personal website.

## Post-publication
The EDS book community and other practitioners in GitHub complying our [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) could suggest changes in the notebook. 
Where relevant, EiC will notify authors about proposed changes and their acceptance. 
If the authors consider suggestions as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook.