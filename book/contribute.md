(contribute)=

# Contribute

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will always be given.

## Core repository

The public GitHub repository has the following structure:

```
| The Environmental Data Science Book
| ├── **/.github**
| │   ├── ISSUE_template
| │   ├── workflows
| │   └── ...
| ├── **/book**
| │   ├── _toc.yml
| │   ├── _config.yml
| │   └── ...
| ├── CODE_OF_CONDUCT.md
| ├── CONTRIBUTING.md
| └── ...
```

The `.github folder` refers to GitHub related deployment files and templates of issues/pull requests usually curated by the repository maintainers or developers. 
The `book folder` holds the website content and other relevant files (table of content and configuration files).  

For the book content, the following contributions are accepted:
* **Narrative content**: include plain text, citations, equations, figures, special content blocks and more.
* **Executable content**: consists of computational material in a given programming language e.g. python.

:::{seealso}
Please visit the corresponding Jupyter Book guidelines for [`narrative`](https://jupyterbook.org/content/index.html#write-narrative-content) and [`executable`]('https://jupyterbook.org/execute/index.html#write-executable-content) content. 
:::

The `_toc.yml` file sets the main sections of EDS book. 
It is a simple configuration file specifying a table of content from all the executable and narrative content found in the ``book`` folder (and in subfolders). 
The current version of the book consists of five key sections:

* **About**: contains narrative content i.e. plain markdown files describing the aims of the book, the target audience, attribution and how to contribute.
* **Gallery**: contains all published executable content listed within a gridded gallery or with individual links.
* **Contributing**: contains all published executable content listed within a gridded gallery or with individual links.
* **Publishing**: provides an introduction of open review, its relevance to computational notebooks and guidelines to publish in EDS book.
* **Community**: compiles community-related resources such as activities in various open science communities and shared notes of EDS book co-working meetings.
* **Afterword**: describes miscellaneous material such as bibliography.

## Notebooks
### Scope
We consider submissions from all areas of environmental science. This includes (but it is not restricted to):
* introducing relevant environmental datasets irrespective of their modality (image, labels, points, shapes, surface text).
* describing the outputs of a machine learning/computer vision model suited to our understanding of Planet Earth.
* showcasing an open-source software suited to Environmental Data Science.
* pre- or post-processing routines relevant for Environmental Science. 

Submissions could be at any stage from notebook idea to a working prototype from an existing GitHub repository. 
The notebook should address scientific and/or technical aspects that EDS book audience could adopt, reuse, and/or extend for their purposes.

The optimal notebook has between 100 and 500 for physical lines of code in `Code Cells`, and 500 to 5000 comments in `Markdown Cells`.
We have determined these ranges from the pool of published notebooks (by March 2023) using [cloc](https://github.com/AlDanial/cloc), a handy open-source tool to count blank lines, comment lines, and physical lines of source code in many programming languages.

Notebook submissions to EDS book must:

* Be fully open, under the Open Definition. This means that any text content or graphical objects should be under a Creative Commons license (ideally CC-BY) and code components should be under an OSI-approved MIT license. 
* Documentation of computational cells should be complete for self-learning or adoption by EDS book users. 
* Notebook submissions should make a clear contribution to Environmental Data Science using available open-source software. 
* Authors wishing to make a pre-submission enquiry should open an issue on the EDS Book repository.

### Themes
EDS notebooks are categorized under four proposed topics or themes:

* **Exploration**: highlights a particular environmental sensor with visualization and interpretation of the corresponding layers of information.
* **Preprocessing**: refers to all procedures to clean and prepare environmental data for analysis. The notebook should highlight differences between the raw and preprocessed data.
* **Modelling**: comprises models to analyse a given environmental system. 
* **Post-processing**: refers to post-process routines to fine tune and/or adjust modelling outputs.

### Publication process
The main steps when submitting and publishing EDS book notebooks are:

* **Notebook idea**: authors open a [notebook idea issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose) in the main EDS book repository. 
Editors-in-Chief (EiC) validates the proposed notebook with a general feedback including potential datasets/methods/tools to be considered.

* **Preparation**: authors prepare a first working (and reproducible) version of the notebook with a notification to EiC. The notebook repository should be hosted in a personal GitHub account.
EiC verify the notebook runs in Binder and confirms its feasibility. 
After the Binder checkpoint, EiC transfer the notebook repository from the personal GitHub account to the [eds-book-gallery](https://github.com/eds-book-gallery) organisation. 

* **Pre-review and review**: EiC open a *PRE-REVIEW* issue to assign an editor. 
The assigned editor should find 2 reviewers to start the review process. 
Authors and reviewers work together to improve the plain and executable content of the notebook. 
All proposed changes and conversations should be conducted within a *REVIEW* issue opened at the main EDS book repository. 

* **Post-print**: after reviewers and editor confirm their recommendation to accept the notebook for publication, EiC will share proofs (the draft of the final formatting) hosted as a Pull Request in the main repo of the EDS book.
EiC ask authors to proof-read the notebook and indicate any remaining typos, badly formed citations, awkward wording, etc.

* **Publication**: EiC disseminate the publication through the official communication channels of the EDS book community e.g. [Bluesky](https://bsky.app/profile/eds-book.bsky.social), [Mastodon](https://fosstodon.org/@eds_book) and [LinkedIn](https://www.linkedin.com/company/edsbook/) 
Authors and reviewers are welcome to use same or alternative communication channels of their preference.

* **Post-publication**: Anyone from the EDS book community or registered in GitHub complying our [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) is welcome to suggest improvements and/or clarifications in the published notebook. 
Where relevant, EiC will notify authors about proposed changes and their acceptance. If the authors consider suggestions as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook. 

## Who can contribute
Inspired by [the Turing Way Guide for Collaboration](https://github.com/alan-turing-institute/the-turing-way/blob/main/book/website/collaboration/collaboration.md), EDS book has the following defined community roles: 

* **Maintainers**: to provide support with keeping the existing source code updated by keeping track of new contributions and/or update versions of the Jupyter book.

* **Authors**: prepare, implement and report changes of the submitted notebook. 
View guidelines for authors

* **Reviewers**: provide feedback for improving the proposed plain and executable content of the notebook.
View guidelines for reviewers

* **Editors-in-Chief**: validate the notebook idea, make suggestions to improve it, prepare the notebook for its revision, assign editors, lead publishing and moderate post-publication.
View guidelines for EiC

* **Editors**: find reviewers, moderate the conversation between reviewers and authors. 
View guidelines for editors

* **Community**: propose, explore and/or make constructive comments of the notebook at the idea stage (optional) or after publication. 
View guidelines for community

* **Readers/Users**: to read/share content, occasionally raise errors such as typos and bugs and fix them.

The table below indicates the key roles within the publication of EDS book notebooks according to the steps mentioned above. 
Mandatory and optional participation are illustrated by ✅ and ⭕ icons, respectively.

| Stage                   |      Where in GitHub      | Authors | Reviewers | Editors-in-Chief | Editors | Community | 
|:------------------------|:-------------------------:|:-------:|:---------:|:----------------:|:-------:|:---------:|
| Notebook idea           |    EDS repo (*issues*)    |    ✅    |           |        ✅         |         |     ⭕     |
| Preparation             |    EDS repo (*issues*)    |    ✅    |           |        ✅         |         |           |
| Prereview and Review    |    EDS repo (*issues*)    |    ✅    |     ✅     |        ✅         |    ✅    |           |
| Post-print              | EDS repo (*pull request*) |    ✅    |     ⭕     |        ✅         |         |           |
| Publication             | EDS repo (*main branch*)  |   ⭕ ️   |           |        ✅         |         |           |
| Post-publication        | Notebook repo (*issues*)  |   ⭕ ️   |           |        ✅         |         |     ✅     |

### Conflict of interest
The definition of a conflict of Interest in peer review is a circumstance that makes you “unable to make an impartial scientific judgement or evaluation” (PNAS Conflict of Interest Policy). 
EDS book community is concerned with avoiding any actual conflicts of interest, and being sufficiently transparent that we avoid the appearance of conflicts of interest as well.

### Authorship
The authors themselves assume responsibility for deciding who should be credited with co-authorship, and co-authors must always agree to be listed. 
In addition, co-authors agree to be accountable for all aspects of the work, and to notify EDS book if any retraction or correction of mistakes are needed after publication.

### Confidential requests
Please write environmental.ds.book@gmail.com with confidential matters such as retraction requests, report of misconduct, and retroactive author name changes.
In case of a name change, the DOI will be unchanged and the notebook will be updated without publishing a correction notice or notifying co-authors.

## Recognising Contributions
We recognise all kinds of contributions, from fixing small errors, to developing documentation, maintaining the project infrastructure, writing or reviewing narrative and/or executable notebooks.

_EDS book_ follows the [all-contributors](https://allcontributors.org) specifications.
The all-contributors bot usage is described [here](https://allcontributors.org/docs/en/bot/usage).
You can see a list of current contributors [here](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/contributors.md). 

# Code of Conduct
Please note that EDS book open-source repository and community are aligned with a [Contributor Code of Conduct](../CODE_OF_CONDUCT.md). 
By contributing to EDS book you agree to abide by its terms.

### Attribution 
Some material in this section and derived guidelines have been adapted from [Neurolibre](https://docs.neurolibre.org/en/latest/REVIEWER.html), the [Journal of Open Source Education](https://openjournals.readthedocs.io/en/jose/index.html) and [pyOpenSci](https://www.pyopensci.org/software-peer-review/index.html) reviewing guidelines, released under CC BY 3.0, CC BY 4.0 and CC BY-SA 4.0, respectively.