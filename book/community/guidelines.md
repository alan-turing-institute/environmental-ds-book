(cm-guidelines)=
# Guidelines

This section covers guidelines related to effective and inclusive collaboration for the whole open-source repository and executable notebooks. 

## General
Inspired by [the Turing Way Guide for Collaboration](https://the-turing-way.netlify.app/collaboration/maintain-review/maintain-review-maintenance.html), the Environmental DS book has the following defined community roles: 

* **Maintainers**: to provide support with keeping the existing source code updated by keeping track of new contributions and/or update versions of the Jupyter book.
* **Contributors**: to create/design narrative and/or executable content.
* **Reviewer**: to review narrative and/or executable content.
* **Reader/User**: to read/share content, occasionally raise errors such as typos and bugs and fix them.

## Executable notebooks
We present below the main stages and roles involved in the publication of EnvDS executable notebooks.

### Review process

Preparing and publishing EnvDS notebooks are like seedlings. 
Each of them is unique, however there is a common ground i.e. stages in the research life cycle of each one. 
The diagram below aims to illustrate the main stages of the review process and publishing EnvDS notebooks represented by plant growth icons (inner circle) and some auxiliary icons self-describing the main task per stage.

```{figure} ../figures/publication_stages.jpg
---
name: publication-stages
alt: Diagram illustrating the publication of EnvDS notebooks according to six stages representing by icons arranged in two inner circles around an u-turn arrow. Icons in the inner circle represent publication stages using plant growth cycle. The external inner circle represents with more general-focused circles. 
---
Illustration by [@acocac](https://github.com/acocac). Zenodo. [http://doi.org/10.5281/zenodo.7030142](https://doi.org/10.5281/zenodo.7030142)
```

* **Notebook idea**: the corresponding author opens a [notebook idea issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose) in the main EDS book repository. In this stage, the editorial team and/or community will help validating the proposed notebook and provide a general feedback with potential datasets/methods/tools to be considered. 
After validating the notebook idea, the corresponding author should create a first draft of the notebook by using a notebook repository template according to the target programming language, [python](https://github.com/Environmental-DS-Book/template_python), R or Julia. 
The repository templates are adapted from [2i2c hub-user-image-template](https://github.com/2i2c-org/hub-user-image-template). The corresponding author should open a Pull Request to start editing the notebook and dependencies files. Within each PR, a comment will be added containing "Test this PR on Binder" badge. The editorial team will use the binder badge to check how reproducible is the notebook and its viability for the reviewing stage. 

* **Preparation**: the editorial team prepares the notebook repository for the reviewing process. 
The stage includes ensuring the notebook repo with a first draft version is transferred to the [Environmental-DS-Book organisation](https://github.com/Environmental-DS-Book). 
The notebook should generate the same outputs as the initial repository hosted in the GitHub account of the corresponding author. 
The editor will create a review branch in which will tag corresponding author and reviewers indicating the main aspects of the review process. 

* **Review round(s)**: corresponding author and reviewer(s) work together to improve the proposed plain and executable content of the notebook. 
Commits and conversations should be conducted in the *review branch* created by the editorial team. 

* **Post-print**: once reviewer(s) and editor(s) recommend the notebook for publication, the editorial team will share proofs (the draft of the final formatting) through a preview in the main repo of the Environmental DS book.

* **Publication**: refers to the dissemination of the notebook in the official communication channels of the project e.g.Twitter and optionally by other communication channels of preference by authors, reviewers and/or community.

### Roles

```{figure} ../figures/publication_roles.jpg
---
name: publication-roles
alt: Diagram illustrating the roles within the publication process of EnvDS notebooks according to six stages representing by icons arranged in the first column. 
---
Illustration by [@acocac](https://github.com/acocac). Optionally involvement is highlighted with a color Zenodo. [http://doi.org/10.5281/zenodo.7030142](https://doi.org/10.5281/zenodo.7030142)
```

* **Corresponding author**: 
* **Reviewer**:
* **Moderator**:
* **Editorial team**:
* **Community**: 

We cover further details of submission and reviewing processes in the following subsections. 