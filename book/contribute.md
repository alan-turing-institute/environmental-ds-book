(contribute)=

# Contribute

Contributions are welcome, and they are greatly appreciated! 
Every little bit helps, and credit will always be given.

This section provides a high-level guide to contributing to EDS book via the [core repository](#contribute-repository) and/or [notebook submissions](#contribute-notebooks).
We encourage you to read through the following sections to learn more about how you can contribute.
If you find that you have questions that are not discussed below, please let us know through one of the many ways to get in touch.

(contribute-repository)=
## Core repository

### Structure
The public GitHub repository has the following structure:

```
| Environmental Data Science Book
| ├── **/.github**
| │   ├── ISSUE_template
| │   ├── workflows
| │   └── ...
| ├── **/book**
| │   ├── myst.yml
| │   └── ...
| ├── CODE_OF_CONDUCT.md
| ├── CONTRIBUTING.md
| └── ...
```

The `.github folder` refers to GitHub related deployment files and templates of issues/pull requests usually curated by the repository maintainers or developers. 
The `book folder` holds the website content and other relevant files (e.g. configuration files).

The `myst.yml` file dictates the `project` and `site` configurations. 
For instance, the `project` part declares the table of content i.e. sections found in the ``book`` folder. 
The current version of the book consists of six key sections:

* **About**: describes the mission, vision, the target audience and motivations.
* **Gallery**: contains all published notebooks listed within a gridded gallery.
* **Contribute**: provides a high-level guide to contributing to EDS book.
* **Guidelines**: contains guidelines to publish notebooks in EDS book.
* **Community**: compiles community-related resources such as communication/support channels and a list of open research communities where EDS book members have contributed.
* **Cite**: indicates how to cite the core EDS book repository and published notebooks.

### Who can contribute
We describe two defined roles for contributing to the core repository:

::::{grid} 1 2 2 2
:::{card}
:header: Maintainers/Developers
Keep the source code updated, track new contributions and/or implement features.
:::

:::{card}
:header: Readers/Users
Read/share content, occasionally raise errors such as typos and bugs and fix them.
:::
::::

(contribute-notebooks)=
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

### Who can contribute
The publishing process of EDS book notebooks is open to all members of the community. We list below the main roles and their responsibilities:

::::{grid} 1 2 2 2

:::{card}
:url: ./guidelines-authors.md
:header: Authors
:footer: View guidelines for authors »

Prepare, implement and report changes of the submitted notebook.
:::

:::{card}
:url: ./guidelines-reviewers.md
:header: Reviewers
:footer: View guidelines for reviewers »

Provide feedback for improving the proposed plain and executable content of the notebook.
:::

:::{card}
:url: ./guidelines-eic.md
:header: Editors-in-Chief
:footer: View guidelines for EiC »

Validate the notebook idea, make suggestions to improve it, prepare the notebook for its revision, assign editors, lead publishing and moderate post-publication.
:::

:::{card}
:url: ./guidelines-editors.md
:header: Editors
:footer: View guidelines for editors »

Find reviewers, moderate the conversation between reviewers and authors. 
:::
::::

:::{card}
:url: ./guidelines-community.md
:header: Community
:footer: View guidelines for community »

Propose, explore and/or make constructive comments of the notebook at the idea stage (optional) or after publication. 
:::



The table below indicates the key roles within the publication of EDS book notebooks according to the publication steps mentioned above. 
Mandatory and optional participation are illustrated by ✅ and ⭕ icons, respectively.

| Stage                   |        Where in GitHub         | Authors | Reviewers | Editors-in-Chief | Editors | Community | 
|:------------------------|:------------------------------:|:-------:|:---------:|:----------------:|:-------:|:---------:|
| Notebook idea           |      EDS repo (*issues*)       |    ✅    |           |        ✅         |         |     ⭕     |
| Preparation             |      EDS repo (*issues*)       |    ✅    |           |        ✅         |         |           |
| Prereview and Review    |      EDS repo (*issues*)       |    ✅    |     ✅     |        ✅         |    ✅    |           |
| Post-print              | Notebook repo (*pull request*) |    ✅    |     ⭕     |        ✅         |         |           |
| Publication             | Notebook repo (*main branch*)  |   ⭕ ️   |           |        ✅         |         |           |
| Post-publication        |    Notebook repo (*issues*)    |   ⭕ ️   |           |        ✅         |         |     ✅     |

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

## Need Help?
If you’re stuck or need assistance:

* Reach out via email to environmental.ds.book@gmail.com for personalised assistance.
* Consider attending our coworking sessions (See [community](./community.md) for more details).

## Code of Conduct
Please note that EDS book open-source repository and community are aligned with a [Contributor Code of Conduct](../CODE_OF_CONDUCT.md). 
By contributing to EDS book you agree to abide by its terms.

## Attribution 
Some material in this section and derived guidelines have been adapted from [Neurolibre](https://docs.neurolibre.org/en/latest/REVIEWER.html), the [Journal of Open Source Education](https://openjournals.readthedocs.io/en/jose/index.html) and [pyOpenSci](https://www.pyopensci.org/software-peer-review/index.html) reviewing guidelines, released under CC BY 3.0, CC BY 4.0 and CC BY-SA 4.0, respectively.