(cm-guidelines-reviewing)=
# Reviewing guidelines

Authors will respond to reviewer-raised issues (if any are raised) on the submission repository’s issue tracker. Reviewer and editor contributions, like any other contributions, should be acknowledged in the repository.

## Context
As a reviewer, you contribute to the technical quality of the content published by our community. 

We welcome submissions along two tracks of material: 
* Plain content: refers to improvements in the content per Environmental system and/or other plain section of the website.
* Executable notebook: consists of shareable and reproducible demonstrators.

Before the review, the editorial committee checks if the submission fits the minimum requirements. If approved, a ‘Ready for Review’ check box is marked within the Pull Request of the contribution.

The quality of the proposed contribution can be assessed through scientific, technical and code criteria. 

### Scientific criteria

You are not expected to conduct a rigorous scientific review of the work. Note, for both plain content and executable notebooks, the authors can provide links to the related research such as peer-reviewed papers, conference proceedings and/or technical reports. If the contribution shows insufficient quality, we encourage you to contact the editorial committee providing the reasons to withdraw it. 

### Technical criteria

The plain and executable content are expected to be jargon free. Some key aspects to consider are listed below.

* Is the text clear and easy to read?
* Are the graphical outputs i.e. tables, figures, among others properly interpreted and help understand the flow of the notebook and/or content?
* Is the content/notebook of an appropriate length?
* Is the content/notebook split into logical sections?
* For notebooks, are the code cells short and readable?

### Code review

When a code is provided, we suggest focusing on a minimal feedback in the following areas:
* Do the first cells relate to the installation and import of libraries to run the notebook?
* Does the code provide a logical folder structure?
* Is the code documented?

## Interactions

### Reviewer and authors

The interaction of the authors is facilitated through ReviewNB, a third-party plugin in GitHub for displaying Jupyter Notebook content. Sharing and viewing the content is much easier and faster than with any other platform e.g. Binder. The inline review comments interface is useful and user-friendly. While it supports major visualisation libraries and interactive widgets, it does not render bokeh-related plots.

In addition to ReviewNB, other platforms which facilitates the reviewing are:
* [notebooksharing.space](https://notebooksharing.space/): supports bokeh-related widgets. Only ask the author to upload the notebook in this platform when you want to inspect the interactive content not rendered in ReviewNB. Note the notebook file is limited up to 10 MB.
* [Netlify previews](https://docs.netlify.com/site-deploys/deploy-previews/): a preview hosted by Netlify can be also inspected in the pull request of the contribution. Note this preview is automatically updated in the reviewing process according to the changes of the authors. 

### Reviewer and editorial team
You can tag the editors in any of the pull requests. For private communications, please send a direct message to [environmental.ds.book@gmail.com](mailto:environmental.ds.book@gmail.com]).

## Conflict of interest
The definition of a conflict of Interest in peer review is a circumstance that makes you “unable to make an impartial scientific judgement or evaluation” (PNAS Conflict of Interest Policy). The Environmental Data Science community is concerned with avoiding any actual conflicts of interest, and being sufficiently transparent that we avoid the appearance of conflicts of interest as well.

As a reviewer, conflict of interests are your present or previous association with any authors of a submission: recent (past four years) collaborators in funded research or work that is published; and lifetime for the family members, business partners, and thesis student/advisor or mentor. In addition, your recent (past year) association with the same organisation of a submitter is a COI, for example, being employed at the same institution.

If you think you are able to make an impartial assessment of the work, you should request that the conflict be waived. For example, if you and a submitter were two of 2000 authors of a high energy physics paper but did not actually collaborate. Or if you and a submitter worked together 6 years ago, but due to delays in the publishing industry, a paper from that collaboration with both of you as authors was published 2 year ago. Or if you and a submitter are both employed by the same very large organisation but in different units without any knowledge of each other.

## Attribution 
Some material in this section has been adapted from [Neurolibre](https://docs.neurolibre.org/en/latest/REVIEWER.html) and the [Journal of Open Source Software](https://github.com/openjournals/joss/blob/master/docs/reviewer_guidelines) reviewing guidelines, released under CC BY 3.0 and MIT licence, respectively.

