(pb-guidelines-eic)=

# Guide for Notebooks Editors-in-chief

Welcome to the guide for notebooks EiC of the EDS book! 

Before you begin this process, please be sure to [understand how the publication process works](pb-guidelines).

We have a [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) which is mandatory for everyone involved in the review process of our notebooks.

Below you will find the main steps we suggest to follow to moderate, validate and publish a notebook to EDS book.

## Scope and Aims
Thank you for considering leading the publication process of a notebook to EDS book.
Our review process aims to be collaborative, transparent and inclusive.

## Notebook Idea

In this step, we suggest providing feedback to the notebook idea.

## Notebook Repository

EiC validate how reproducible is the notebook and its feasibility for the reviewing stage using the binder badge in the PR.

After validating the minimal working version, EiC transfer the notebook repository to the [Environmental Data Science book organisation](https://github.com/Environmental-DS-Book). 

The notebook in the transferred repository should generate the same outputs as the initial repository hosted in the GitHub account of the corresponding author. 

Then if it generates the same results, create a review branch in which will tag corresponding author and reviewers indicating the main aspects of the review process. 

Rename the filename of the template to the pattern (XXX-YYY-ZZZ, where XXX refers to the environmental system, YYY to the theme and ZZZ to a preferred identifier of the model, sensor or pre/post-processing pipeline). For example, "forest-modelling-treecrown.ipynb".

## Pre-review
EiC will open a PR containing all relevant information for pre-reviewing the notebook. 
EiC assigns an editor to moderate the review and find reviewers.
Once reviewers agreed on the revision, EiC opens a review issue 

## Review
The review issue aims to be a space where editor will moderate timings and conversation between authors and reviewers.
Once reviewers recommend the notebook for publication, EiC will be notified by the editor to start the post-print stage.

## Post-print
EiC will lead publishing asking authors to proof-read the notebook and indicate any remaining typos, badly formed citations, awkward wording, etc.

## Publication
EiC will announce the notebook in the EDS book social accounts and tag authors accounts according to their authorization.

## Post-publication
EDS book community and other practitioners in GitHub could suggest changes in the notebook. 
Where relevant, EiC will notify authors about proposed changes and their acceptance. If the authors consider suggestions as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook.