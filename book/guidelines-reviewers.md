(pb-guidelines-reviewers)=

# Guide for Reviewers
Welcome to the guide for notebooks reviewers of the EDS book! 

Before you begin this process, please be sure to [understand how the publication process works](#contribute-notebooks).

We have a [code of conduct](https://raw.githubusercontent.com/alan-turing-institute/environmental-ds-book/master/CODE_OF_CONDUCT.md) which is mandatory for everyone involved in the review process of our notebooks.

Below you will find the main steps we suggest to follow to review notebooks submitted to EDS book.

## Scope and Aims
Thank you for considering reviewing a notebook for EDS book.
Our review process aims to be open, collaborative, transparent and inclusive.
We therefore welcome reviewers from a diversity of background and with varying levels of programming/domain expertise.

We encourage reviewers to adhere to the principles of the [Open Science Peer Review Oath](https://doi.org/10.12688/f1000research.5686.2).

## Pre-review
An editor will confirm reviewers interest to review the notebook by tagging them into a PRE-REVIEW issue within the main EDS book repository.
The PRE-REVIEW contains some relevant information of the notebook including a link to the notebook idea issue. 

## Review
After confirming reviewers availability, Editor-in-Chief (EiC) opens a REVIEW issue to moderate a high-level discussion between notebook authors and reviewers. 

```{important}
Reviewers will be asked to conduct the review within **2 weeks** of accepting the invitation by the assigned editor. 
Authors will be asked to respond to reviewers’ comments within **2 weeks** of the last-submitted review.
We suggest an additional **1 week** for reviewer approval of changes.
Please contact the editor directly or in the REVIEW issue thread to inform possible delays.
```

To review a notebook, we provide a review template (see below) with a checklist.

```{include} templates/reviewers/reviewers-review-checklist.md
```

The checklist will be available per reviewer within the first comment of the notebook REVIEW issue created by EiC.

Additional comments are welcome on the same issue or directly to the notebook repo. 

If reviewers do the latter, they will find a PR in the notebook repository where authors and reviewers carry out the discussion through ReviewNB, a third-party plugin in GitHub for displaying and commenting Jupyter Notebooks (see further details [here](../about/notebooks-technologies.md)).
Reviewers can open issues in the notebook repo too and link the URL of the notebook REVIEW issue thread.
This facilitates centralizing comments.
All changes implemented by authors will be available in the `review` PR. 
The editor will ask reviewers to re-evaluate the notebook after the authors' changes.

Authors should respond within 2 weeks with their changes to the notebook in response to reviewers comments.