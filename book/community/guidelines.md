(cm-guidelines)=
# Guidelines for EDS notebooks

This section introduce the publication process, roles and themes in EDS computational notebooks.

## Publication process

The diagram below illustrates the main steps when submitting and publishing EDS notebooks.

```{figure} ../figures/guidelines/publication_stages.jpg
---
name: publication-stages
alt: Diagram illustrating the publication of EDS notebooks according to six steps represented by icons arranged with two surronding circles. Icons in the inner circle represent publication steps using plant growth cycle. The outer circle represents each step with more general and self-explanatory icons. 
---
Diagram illustrating the publication of EDS notebooks according to six steps represented by icons arranged with two surronding circles. Illustration by [@acocac](https://github.com/acocac). Zenodo: [http://doi.org/10.5281/zenodo.7030142](https://doi.org/10.5281/zenodo.7030142)
```

* **Notebook idea**: authors open a [notebook idea issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose) in the main EDS book repository. 
The Editor-in-chief (EiC) makes a quick check and validates the proposed notebook with a general feedback including potential datasets/methods/tools to be considered.
Once the idea is validated, the EiC assigns an editor who starts a conversation with authors about potential reviewers.

* **Preparation**: Authors prepare a first working version of the notebook and notify the editor when is ready with a link to the notebook repository hosted in a personal GitHub account.
The editor validates the notebook runs in Binder and confirms its reproducibility to the EiC to start the reviewing process. 
The EiC transfers the notebook repository from the personal GitHub account to the [Environmental-DS-Book organisation](https://github.com/Environmental-DS-Book). 

* **Review round(s)**: Once 2 or 3 reviewers are found, the editor officially start the review. 
Authors and reviewers work together to improve the proposed plain and executable content of the notebook. 
All notebook changes and conversations should be conducted in the *review branch* created by the EiC within the transferred notebook repository in the Environmental-DS-Book organisation. 

* **Post-print**: after reviewers and editors confirm their recommendation to accept the notebook for publication, the EiC will share proofs (the draft of the final formatting) hosted as a Pull Request in the main repo of the EDS book.
The EiC asks authors to proof-read the notebook and indicate any remaining typos, badly formed citations, awkward wording, etc.

* **Publication**: the EiC disseminates the publication through the official communication channels of the EDS book community e.g.Twitter. Authors and reviewers are welcome to use other communication channels of their preference.

* **Post-publication**: Anyone from the EDS book community or registered in GitHub is welcome to suggest improvements and/or clarifications in the published notebook. Where relevant, EiC will notify authors about proposed changes and their acceptance. If the authors consider the suggestion as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook. 

## Roles

The table below indicates the roles within the publication of EDS notebooks according to the steps mentioned in the previous section. 
Mandatory and optional participation are illustrated by ✅ and ⭕ icons, respectively.

| Stage                       |                Where                | Authors | Reviewers | Editors-in-chief | Editors | Community | 
|:----------------------------|:-----------------------------------:|:-------:|:---------:|:----------------:|:-------:|:---------:|
| Notebook idea               |         EDS repo (*issues*)         |    ✅    |           |        ✅          |         |           |
| Preparation                 |  Notebook repo (*preprint branch*)  |    ✅    |           |        ✅          |         |           |
| Review round(s)             |   Notebook repo (*review branch*)   |    ✅    |     ✅     |        ✅         |    ✅    |           |
| Post-print                  | Notebook repo (*post-print branch*) |    ✅    |     ⭕     |        ✅          |    ✅    |           |
| Publication                 |      EDS repo (*main branch*)       |   ⭕ ️   |           |         ✅         |         |           |
| Post-publication            |      Notebook repo (*issues*)       |   ⭕ ️   |           |         ✅         |         |     ✅     |

* **Authors**: prepare, implement and report changes of the submitted notebook. 
* **Reviewers**: provide feedback for improving the proposed plain and executable content of the notebook.
* **Editors-in-chief**: participate in a quick-check of the notebook idea, make suggestions to improve it, prepare the notebook for its revision, assign editors, lead publishing and moderate post-publication.
* **Editors**: find reviewers, moderate the conversation between reviewers and authors. 
* **Community**: makes constructive comments of the published notebook. 

### Themes

EDS notebooks are categorized under four proposed topics or themes:

* **Exploration**: highlights a particular environmental sensor with visualization and interpretation of the corresponding layers of information.
* **Preprocessing**: refers to all procedures to clean and prepare environmental data for analysis. The notebook should highlight differences between the raw and preprocessed data.
* **Modelling**: comprises models to analyse a given environmental system. 
* **Post-processing**: refers to post-process routines to fine tune and/or adjust modelling outputs.

We cover further details of submission and reviewing processes by role in the following subsections. 