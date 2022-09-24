(cm-guidelines)=
# Guidelines for EDS notebooks

This section covers guidelines related to effective and inclusive collaboration for EDS computational notebooks. 

## Publication process

Preparing and publishing EDS notebooks are like seedlings. 
Each of them is unique, however there is a common ground i.e. stages in the research life cycle of each one. 
The diagram below aims to illustrate the main stages in the review process and publishing of EDS notebooks represented by plant growth icons (inner circle) and other outer auxiliary icons self-describing the main activity per stage.

```{figure} ../figures/guidelines/publication_stages.jpg
---
name: publication-stages
alt: Diagram illustrating the publication of EDS notebooks according to six stages represented by icons arranged with two surronding circles. Icons in the inner circle represent publication stages using plant growth cycle. The outer circle represents each stage with more general and self-explanatory icons. 
---
Diagram illustrating the publication of EDS notebooks according to six stages represented by icons arranged with two surronding circles. Illustration by [@acocac](https://github.com/acocac). Zenodo: [http://doi.org/10.5281/zenodo.7030142](https://doi.org/10.5281/zenodo.7030142)
```

* **Notebook idea**: the corresponding author opens a [notebook idea issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose) in the main EDS book repository. In this stage, the editorial team and/or community help validating the proposed notebook and provide a general feedback with potential datasets/methods/tools to be considered. 

* **Preparation**: the editorial team prepares the notebook repository for the reviewing process. 
The stage includes ensuring the notebook repo with a first draft version is transferred to the [Environmental-DS-Book organisation](https://github.com/Environmental-DS-Book). 

* **Review round(s)**: corresponding author and reviewer(s) work together to improve the proposed plain and executable content of the notebook. 
Commits and conversations should be conducted in the *review branch* created by the editorial team within the transferred notebook repository in the Environmental-DS-Book organisation. 

* **Post-print**: once reviewer(s) and editor(s) recommend the notebook for publication, the editorial team will share proofs (the draft of the final formatting) through a preview in the main repo of the EDS book.

* **Publication**: refers to the dissemination of the notebook in the official communication channels of the project e.g.Twitter and optionally other communication channels of preference by authors, reviewers and/or community.

## Roles

The table below indicates the roles within EDS notebooks according to six stages of publication process represented in the figure above.  

| Stage                       |               Where               | Author | Reviewer | Moderator | Editorial team | Community | 
|:----------------------------|:---------------------------------:|:------:|:--------:|:--------:| :---: |:--------:|
| Notebook idea               |         EDS repo (issues)         |   ✅    |          |          |   ✅    |     ✅    |
| Preparation                 |  Notebook repo (preprint branch)  |   ✅    |          |          |   ✅    |          |
| Review round(s)             |   Notebook repo (review branch)   |   ✅    |     ✅    |     ✅    |   ✅    |          |
| Post-print                  | Notebook repo (post-print branch) |   ✅    |     ⭕     |          |   ✅    |          |
| Publication                 |      EDS repo (main branch)       |   ⭕ ️    |          |          |   ✅    |          |
| Post-publication            |      Notebook repo (issues)       |   ⭕ ️    |          |          |   ✅    |     ✅    |

* **Corresponding author**: leads the preparation, implementation and reporting to changes of the submitted notebook. 
* **Reviewer**: provides feedback for improving the proposed plain and executable content of the notebook.
* **Moderator**: assists in mediating conversation between author(s) and reviewer(s)
* **Editorial team**: supports the transfer of the notebook in the EDS organisation, share proofs of the recommended notebook and ensure the dissemination in the publication in the available social networks of EDS book. 
* **Community**: suggests and makes constructive comments of the notebook idea or published notebook. 

### Themes

EDS notebooks are categorized under four proposed topics or themes:

* **Exploration**: highlights a particular environmental sensor with visualization and interpretation of the corresponding layers of information.
* **Preprocessing**: refers to all procedures to clean and prepare environmental data for analysis. The notebook should highlight differences between the raw and preprocessed data.
* **Modelling**: comprises models to analyse a given environmental system. 
* **Post-processing**: refers to post-process routines to fine tune and/or adjust modelling outputs.

We cover further details of submission and reviewing processes in the following subsections. 