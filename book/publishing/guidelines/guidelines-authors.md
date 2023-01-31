(pb-guidelines-authors)=

# Guide for Notebooks Authors

Welcome to the guide for notebooks authors of the EDS book! 

Before you begin this process, please be sure to [understand how the publication process works](pb-guidelines).

We have a [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) which is mandatory for everyone involved in the review process of our notebooks.

Below you will find the main steps we suggest to follow to submit a notebook to EDS book for peer review.

## Scope and Aims
Thank you for considering submitting a notebook to EDS book.
Our review process aims to be collaborative, transparent and inclusive. 
We therefore welcome authors from a diversity of background and with varying levels of programming/domain expertise.

Previous submissions had a mix of technical and domain focus.

## Notebook Idea

In this step, we provide a transparent discussion space to validate notebooks ideas (NBI) before their review. 

Submitting a NBI is as simple as:

* Open a NBI [issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose).
* Fill the NBI template with some description of the notebook and information about the input data and target theme.
* Wait for Editors-in-chief and/or community (optional) to provide feedback.
* Once you get a minimal and satisfactory feedback, we encourage to start preparing the notebook repository.

## Notebook Repository

After validating the notebook idea, a first draft of the notebook should be created by using a notebook repository template according to the target programming language:
* [Python](https://github.com/Environmental-DS-Book/template_python)
* R (TODO)
* Julia (TODO)

The repository templates are adapted from [2i2c hub-user-image-template](https://github.com/2i2c-org/hub-user-image-template). 
The corresponding author should open a Pull Request to start editing the notebook and dependencies files. 
Within each PR, a comment will be added containing "Test this PR on Binder" badge. 
Editors-in-chief will use the binder badge to check how reproducible is the notebook and its feasibility for the reviewing stage. 

Some general guidelines are:
* Fill the information header according to your use case. Feel free to guide from previous published notebooks, see for instance the [IceNet notebook](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/gallery/modelling/polar-modelling-icenet.ipynb).
* Change the structure of the remaining sections of the notebook according to your preference.
  * We advise following the 10 rules of compelling notebooks provided by the EarthCube initiative available in their [Notebook Template](https://github.com/earthcube/NotebookTemplates/blob/main/EC_05_Template_Notebook_for_EarthCube_Long_Version.ipynb) (section `Data processing and analysis`).
* For `python` packages, we suggest exploring the [Pangeo stack](https://pangeo.io/). The Pangeo community curates a wide diversity of environments in the `pangeo-docker-images` [repository](https://github.com/pangeo-data/pangeo-docker-images/tree/master/pangeo-notebook). 
  * For notebooks, we suggest using the `pangeo-notebook` conda environment available [here](https://github.com/pangeo-data/pangeo-docker-images/blob/master/pangeo-notebook/environment.yml). The environment can be installed in your system using `conda env create -f environment.yml`.
* Test the notebook is working according to the Binder badge in the PR.
* For notebooks showcasing deep learning models, the public Binder does not provide GPU support, so we suggest testing the notebook works with `cpu` when predicting from the pretrained models. 

After an approval of the draft version of the notebook by EiC, please transfer the notebook repository to the [Environmental Data Science book organisation](https://github.com/Environmental-DS-Book). 

EiC will assist you to prepare the notebook repository for the review process.

## Pre-review
EiC will open a PRE-REVIEW issue where a handling editor and authors suggest reviewers. 
The editor can give initial direction to the authors for improving the notebook can already happen here, especially if the notebook lacks some requested sections.
Once reviewers agreed on the revision, a REVIEW issue is open by EiC. 

## Review
The REVIEW issue aims to be a space where editor will moderate timings and conversation between authors and reviewers.
Reviewers will open issues in the notebook repository indicating their main suggestions. 
Authors should address reviewers suggestions according to their relevance.
Once reviewers recommend the notebook for publication, the editor will contact EiC to start the post-print stage.

### Interation
The interaction between authors and reviewers is facilitated through ReviewNB, a third-party plugin in GitHub for displaying Jupyter Notebook content. 
Sharing and viewing the content is much easier and faster than with any other platform e.g. Binder. 
The inline review comments interface is useful and user-friendly. 
While it supports major visualisation libraries and interactive widgets, it does not render bokeh-related plots.

In addition to ReviewNB, other platforms which facilitates the reviewing are:
* [notebooksharing.space](https://notebooksharing.space/): supports bokeh-related widgets. Only ask the author to upload the notebook in this platform when you want to inspect the interactive content not rendered in ReviewNB. Note the notebook file is limited up to 10 MB.
* [Netlify previews](https://docs.netlify.com/site-deploys/deploy-previews/): a preview hosted by Netlify can be also inspected in the pull request of the contribution (only at the post-print stage). 

## Post-print
EiC will lead publishing asking authors to proof-read the notebook and indicate any remaining typos, badly formed citations, awkward wording, etc.

## Publication
While EiC will announce the notebook in the EDS book social accounts, authors should promote their work in their communication channels.

Some authors have promoted EDS notebooks in LinkedIn. 
Others have added them to their online CV and/or personal website.

## Post-publication
EDS book community and other practitioners in GitHub could suggest changes in the notebook. 
Where relevant, EiC will notify authors about proposed changes and their acceptance. 
If the authors consider suggestions as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook.