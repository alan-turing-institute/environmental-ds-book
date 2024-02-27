(pb-guidelines)=

# Guidelines for EDS book notebooks
This section introduces the publication process, roles and themes in EDS book computational notebooks.

## Publication process
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

* **Publication**: EiC disseminate the publication through the official communication channels of the EDS book community e.g. [Twitter](https://twitter.com/EnvDSbook), [Mastodon](https://fosstodon.org/@eds_book). 
Authors and reviewers are welcome to use same or alternative communication channels of their preference.

* **Post-publication**: Anyone from the EDS book community or registered in GitHub complying our [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) is welcome to suggest improvements and/or clarifications in the published notebook. 
Where relevant, EiC will notify authors about proposed changes and their acceptance. If the authors consider suggestions as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook. 

## Roles
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

* **Authors**: prepare, implement and report changes of the submitted notebook. 
* **Reviewers**: provide feedback for improving the proposed plain and executable content of the notebook.
* **Editors-in-Chief**: validate the notebook idea, make suggestions to improve it, prepare the notebook for its revision, assign editors, lead publishing and moderate post-publication.
* **Editors**: find reviewers, moderate the conversation between reviewers and authors. 
* **Community**: propose, explore and/or make constructive comments of the notebook at the idea stage (optional) or after publication. 

### Attribution 
Some material in this section and derived guidelines have been adapted from [Neurolibre](https://docs.neurolibre.org/en/latest/REVIEWER.html), the [Journal of Open Source Education](https://openjournals.readthedocs.io/en/jose/index.html) and [pyOpenSci](https://www.pyopensci.org/software-peer-review/index.html) reviewing guidelines, released under CC BY 3.0, CC BY 4.0 and CC BY-SA 4.0, respectively.