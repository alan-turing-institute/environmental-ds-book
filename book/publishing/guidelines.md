(pb-guidelines)=
# Guidelines for EDS book notebooks

This section introduces the publication process, roles and themes in EDS book computational notebooks.

## Publication process

The main steps when submitting and publishing EDS book notebooks are:

* **Notebook idea**: authors open a [notebook idea issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose) in the main EDS book repository. 
Editors-in-chief (EiC) validates the proposed notebook with a general feedback including potential datasets/methods/tools to be considered.

* **Preparation**: Authors prepare a first working (and reproducible) version of the notebook with a notification to EiC. The notebook repository should be hosted in a personal GitHub account.
EiC verifies the notebook runs in Binder and confirms its feasibility. 
After the binder checkpoint, EiC transfers the notebook repository from the personal GitHub account to the [Environmental-DS-Book organisation](https://github.com/Environmental-DS-Book). 

* **Pre-review and review**: EiC opens a *preview issue* to assign an Editor. 
The assigned editor should find 2 or 3 reviewers to start the review process. 
Authors and reviewers work together to improve the plain and executable content of the notebook. 
All proposed changes and conversations should be conducted within a *review issue* opened at the main EDS book repository. 

* **Post-print**: after reviewers and editor confirm their recommendation to accept the notebook for publication, EiC will share proofs (the draft of the final formatting) hosted as a Pull Request in the main repo of the EDS book.
EiC asks authors to proof-read the notebook and indicate any remaining typos, badly formed citations, awkward wording, etc.

* **Publication**: EiC disseminates the publication through the official communication channels of the EDS book community e.g. [Twitter](https://twitter.com/EnvDSbook), [Mastodon](https://fosstodon.org/@EDSbook). 
Authors and reviewers are welcome to use other communication channels of their preference.

* **Post-publication**: Anyone from the EDS book community or registered in GitHub is welcome to suggest improvements and/or clarifications in the published notebook. 
Where relevant, EiC will notify authors about proposed changes and their acceptance. If the authors consider suggestions as a substantial contribution, EiC will acknowledge it by adding the contributor's name to the citation of the notebook. 

## Roles

The table below indicates the key roles within the publication of EDS book notebooks according to the steps mentioned above. 
Mandatory and optional participation are illustrated by ✅ and ⭕ icons, respectively.

| Stage                   |           Where in GitHub           | Authors | Reviewers | Editors-in-chief | Editors | Community | 
|:------------------------|:-----------------------------------:|:-------:|:---------:|:----------------:|:-------:|:---------:|
| Notebook idea           |         EDS repo (*issues*)         |    ✅    |           |        ✅          |         |     ⭕     |
| Preparation             |       EDS repo (*issues*)           |    ✅    |           |        ✅          |         |           |
| Prereview and Review    |         EDS repo (*issues*)         |    ✅    |     ✅     |        ✅         |    ✅    |           |
| Post-print              | Notebook repo (*post-print branch*) |    ✅    |     ⭕     |        ✅          |         |           |
| Publication             |      EDS repo (*main branch*)       |   ⭕ ️   |           |         ✅         |         |           |
| Post-publication        |      Notebook repo (*issues*)       |   ⭕ ️   |           |         ✅         |         |     ✅     |

* **Authors**: prepare, implement and report changes of the submitted notebook. 
* **Reviewers**: provide feedback for improving the proposed plain and executable content of the notebook.
* **Editors-in-chief**: validate the notebook idea, make suggestions to improve it, prepare the notebook for its revision, assign editors, lead publishing and moderate post-publication.
* **Editors**: find reviewers, moderate the conversation between reviewers and authors. 
* **Community**: explore and/or make constructive comments of the published notebook. 

### Conflict of interest
The definition of a conflict of Interest in peer review is a circumstance that makes you “unable to make an impartial scientific judgement or evaluation” (PNAS Conflict of Interest Policy). The Environmental Data Science community is concerned with avoiding any actual conflicts of interest, and being sufficiently transparent that we avoid the appearance of conflicts of interest as well.

As a reviewer, conflict of interests are your present or previous association with any authors of a submission: recent (past four years) collaborators in funded research or work that is published; and lifetime for the family members, business partners, and thesis student/advisor or mentor. In addition, your recent (past year) association with the same organisation of a submitter is a COI, for example, being employed at the same institution.

If you think you are able to make an impartial assessment of the work, you should request that the conflict be waived. For example, if you and a submitter were two of 2000 authors of a high energy physics paper but did not actually collaborate. Or if you and a submitter worked together 6 years ago, but due to delays in the publishing industry, a paper from that collaboration with both of you as authors was published 2 year ago. Or if you and a submitter are both employed by the same very large organisation but in different units without any knowledge of each other.

### Attribution 
Some material in this section and derived guidelines has been adapted from [Neurolibre](https://docs.neurolibre.org/en/latest/REVIEWER.html), the [Journal of Open Source Education](https://openjournals.readthedocs.io/en/jose/index.html) and [pyOpenSci](https://www.pyopensci.org/software-peer-review/index.html) reviewing guidelines, released under CC BY 3.0, CC BY 4.0 and CC BY-SA 4.0, respectively.

