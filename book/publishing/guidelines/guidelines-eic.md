(pb-guidelines-eic)=

# Guide for Editors-in-chief
Welcome to the guide for notebooks EiC of the EDS book! 

Before you begin this process, please be sure to [understand how the publication process works](pb-guidelines).

We have a [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) which is mandatory for everyone involved in the review process of our notebooks.

Below you will find the main steps we suggest to follow to moderate, validate and publish a notebook to EDS book.

## Scope and Aims
Thank you for considering leading the publication process of a notebook to EDS book.
Our review process aims to be open, collaborative, transparent and inclusive.

## Notebook Idea
In this step, we suggest providing feedback to the notebook idea.

## Notebook Repository
EiC validate how reproducible is the notebook and its feasibility for the reviewing stage. 
This process is aided by the Binder badge in a PR in the corresponding author's notebook repository.

After validating a minimal working version, EiC transfer the notebook repository to the [Environmental Data Science book organisation](https://github.com/Environmental-DS-Book). 

The notebook in the transferred repository should generate the same outputs as the initial repository hosted in the GitHub account of the corresponding author. 

Before moving to PRE-REVIEW, EiC open a new issue `Preparation` in the notebook repository and complete the checklist below: 

```{include} ../../templates/editor-in-chief/eic-preparation-checklist.md
```

## Pre-review
EiC open a PRE-REVIEW issue containing all relevant information of the notebook including a link to the notebook idea issue.

Copy and paste the markdown below in the issue:

```{include} ../../templates/editor-in-chief/eic-prereview-template.md
```

EiC assign an editor to moderate the review and find reviewers.

```{important}
The assigned editor should confirm acceptance and availability within **1 week**.
```

After the editor acceptance, EiC will update the heading at the top of the issue with [EDITOR GITHUB HANDLE] next to **Editor:** section.
Once reviewers agreed on the revision, EiC open a REVIEW issue.

## Review
The REVIEW issue aims to be a space where editor will moderate timings and conversation between authors and reviewers.
To facilitate the discussion, EiC creates a new branch `review` to add reviewers info (name, affiliation, GitHub handle) in the contribution section of the notebook. 
Then EiC commit and push changes to create a PR in the notebook repository. 
The PR will trigger ReviewNB, a third-party plugin in GitHub for displaying and commenting Jupyter Notebooks (see further details [here]).

Once reviewers recommend the notebook for publication, EiC will be notified by the editor to start the post-print stage.

## Post-print
EiC will lead publishing asking authors to proof-read the notebook and indicate any remaining typos, badly formed citations, awkward wording, etc.

## Publication
EiC will announce the notebook in the EDS book social accounts and tag authors accounts according to their authorization.

## Post-publication
EDS book community and other practitioners in GitHub could suggest changes in the notebook. 
Where relevant, EiC will notify authors about proposed changes and their acceptance. If the authors consider suggestions as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook.