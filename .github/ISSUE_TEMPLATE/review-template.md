---
name: "\U0001F440 REVIEW"
about: Log a REVIEW issue!
title: '[REVIEW]'
labels: ["review"]
---

# Notebook Review: Issue#[PREREVIEW ID]

<p align="left">
    <a href="https://notebooks.gesis.org/binder/v2/gh/eds-book-gallery/[NOTEBOOK NAME]/review?labpath=[NOTEBOOK NAME].ipynb">
        <img alt="Binder" src="https://mybinder.org/badge_logo.svg">
    </a>
</p>

**Submitting author:** [AUTHOR GITHUB HANDLE]

**Repository:** [NOTEBOOK REPOSITORY LINK]

**Notebook idea issue:** [NOTEBOOK IDEA ISSUE ID]

**Notebook preview:** [NOTEBOOK PR IN EDS BOOK]

**Editor:** [EDITOR GITHUB HANDLE]

**Reviewer:** [REVIEWER1 GITHUB HANDLE], [REVIEWER2 GITHUB HANDLE]

**Managing EiC:** [EIC GITHUB HANDLE]

## Status

**Reviewer instructions & questions**

Hi 👋 [REVIEWER1 GITHUB HANDLE] & [REVIEWER2 GITHUB HANDLE], please carry out your review in this issue by updating the checklist below. 

As a reviewer, you contribute to the technical quality of the content published by our community. 

Before the review, EiC checked if the submission fits the minimum requirements. 

The quality of the proposed contribution can be assessed through scientific, technical and code criteria. 

The reviewer guidelines are available here: https://edsbook.org/publishing/guidelines/guidelines-reviewers.html. 
Any questions/concerns please let [EDITOR GITHUB HANDLE] know.

## Review checklist for [REVIEWER GITHUB HANDLE]

*Please check off boxes as applicable, and elaborate in comments below. Your review is not limited to these topics, as described in the reviewer guide.*

### Conflict of interest
- [ ] As the reviewer I confirm that there are no conflicts of interest for me to review this work (If you are unsure whether you are in conflict, please speak to your editor _before_ starting your review).

### Code of conduct an peer-review principles
- [ ] I confirm that I read and will adhere to the Environmental Data Science [code of conduct](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/CODE_OF_CONDUCT.md).
- [ ] I confirm that I read and will adhere to [Open Science Peer Review Oath](https://doi.org/10.12688/f1000research.5686.2) 

### General checks
- [ ] **Notebook:** Is the notebook file (``notebook.ipynb``) part of the notebook repository?
- [ ] **Contribution and authorship:** Does the author list seem appropriate and complete (full name, affiliation, and GitHub/ORCID handle)?
- [ ] **Scope and eligibility:** Does the submission contain an original and complete analysis according to the [scope of EDS book](https://edsbook.org/notebooks/about/aims-and-scope.html#aims-and-scope)?

### Reproducibility
- [ ] Does the notebook run in a local environment?
- [ ] Does the notebook build and run in binder?
- [ ] Are all data sources openly accessible and properly cited (e.g. with citation to a persistent DOI) in the heading section?

### Pedagogy
- [ ] Are the notebook purpose and highlights clear?
- [ ] Does the notebook demonstrate some specific data analysis or visualisation techniques?
- [ ] Is the notebook well documented, using both markdown cells and comments in code cells?
- [ ] Does the conclusion section provide clear and concise final say on the tools, analysis and/or datasets used?
- [ ] Is the notebook narrative well written (it does not require editing for structure, language, or writing quality)?

### Ethical
- [ ] Is any linkage of datasets in the notebook unlikely to lead to an increased risk of the personal identification of individuals?
- [ ] Is the notebook truthful and clear about any limitations of the analysis (and potential biases in data and/or tools)?
- [ ] Is the notebook unlikely to lead to negative social outcomes, such as (but not limited to) increasing discrimination or injustice?

### Other Requirements
- [ ] All mentioned software should be formally and consistently cited wherever possible.
- [ ] Acronyms should be spelled out upon first mention.
- [ ] License conditions on images and figures must be respected (Creative Commons, etc.).

### Final approval (post-review)

- [ ] **Authors has responded to my review and made changes to my satisfaction. I recommend approving the notebook for publication.**

## Additional instructions

Reviewer general comments are welcome on this REVIEW issue or directly to the notebook repository.

If you do the latter, you will find a Pull Request titled REVIEW where you can carry out the discussion with authors through ReviewNB, a third-party plugin in GitHub for displaying and commenting Jupyter Notebooks (see further details [here](https://edsbook.org/notebooks/about/notebooks-technologies.html#reviewnb)). 

In addition to ReviewNB, we suggest to explore or run the notebook in:
* **Binder** (run): Click the Launch Binder button at the top level of this message.
* **Netlify** (only previews): a preview hosted by Netlify can be also inspected in the pull request of the contribution in EDS book (see link in *Notebook preview*).