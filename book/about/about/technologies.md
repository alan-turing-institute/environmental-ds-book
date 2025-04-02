(about-technologies)=

# Technologies

This section indicates the main technologies for peer-reviewing and sharing EDS book notebooks.

## Review

The interaction between authors and reviewers in the notebook repository is facilitated through [ReviewNB](https://www.reviewnb.com/), a third-party plugin in GitHub for displaying and commenting Jupyter Notebooks. 
Sharing and viewing the content is faster in ReviewNB than with any other online platform e.g. Binder. 
Also, it easily renders Jupyter Notebook rich diffs than GitHub (see [here](https://blog.reviewnb.com/github-not-rendering-interactive-notebook-widgets/)). 
The inline review comments interface is useful and user-friendly. 
While it supports major visualisation libraries and interactive widgets, it does not render certain libraries for interactive charts and plots e.g. [Bokeh](https://github.com/bokeh/bokeh).

In addition to ReviewNB, other platforms which facilitates the reviewing are:
* [notebooksharing.space](https://notebooksharing.space/) (optional at the review stage): supports bokeh-related widgets. Reviewers can ask the author to upload the notebook in this platform to inspect the interactive content not rendered in ReviewNB. 
Note the notebook file is limited up to 10 MB.
* [Netlify previews](https://docs.netlify.com/site-deploys/deploy-previews/) (only at the post-print stage): a preview hosted by Netlify can be also inspected in the pull request of the contribution. 

### ReviewNB

ReviewNB is a GitHub-verified marketplace app that renders all interactive HTML/JavaScript notebook outputs, except bokeh-related widgets. 
It has been used to review over [200,000 Jupyter Notebooks](https://www.reviewnb.com/#repos).
The app, introduced in 2018 (see [here](https://blog.amirathi.com/2018/10/24/introducing-reviewnb-jupyter-notebook-visual-diff/#more-290)), allows commenting on rich diffs and it will render even the largest of notebooks without timing out.

Let's highlight below the main features of ReviewNB according to its [official documentation](https://docs.reviewnb.com/index.html):

- [Visual diff](https://uploads-ssl.webflow.com/5ba4ebe021cb91ae35dbf88c/5ba93ded243329a486dab26e_sl-code%2Bimage.png) for every commit or pull request containing Notebooks
- [Commenting](https://uploads-ssl.webflow.com/5ba4ebe021cb91ae35dbf88c/5c7d0095d99ee508018a9878_Screenshot%202019-03-04%20at%204.08.48%20PM.png) on the notebook diff to start discussion
- [Conversation threads](https://uploads-ssl.webflow.com/5ba4ebe021cb91ae35dbf88c/5c7eb42d7cef320c0133d1c6_threads-v2.png) to track all open discussions
- [Team conversations](https://blog.reviewnb.com/commenting-for-jupyter/) directly on Jupyter Notebooks

In EDS book, we use ReviewNB in the review step. 
Once Editors-in-Chief or reviewers open a PR in the notebook repository, it will include a link to view changes on ReviewNB.

You can find further information of latest ReviewNB developments in https://blog.reviewnb.com/.

## Research objects and RoHub

Research objects (ROs) are living resources helping to organise and describe the inputs, materials, and methods used in a scientific experiment and obtained as a result and not only at the end when publishing the research outcomes{cite}`ttw-2022`.

[RoHub](https://reliance.rohub.org/) is a Research Object management platform{cite}`rohub-2018` that enables researchers to collaboratively manage, share and preserve their research work (data, software, workflows, models, presentations, videos, articles, etc.){cite}`ttw-2022`. 
RoHub implements the full RO model and paradigm: resources associated to a particular research work are aggregated into a single FAIR digital object, and metadata relevant for understanding and interpreting the content is represented as semantic metadata that are user and machine readable{cite}`ttw-2022`.

All EDS book notebooks are findable in RoHub.
RoHub allows tracking all research life cycle and derivate work of EDS book notebooks (from the notebook idea to post-publication).
In addition, the platform allows sharing, publishing and citing EDS book notebooks.

For further details of RoHub, we suggest visiting its portal documentation [here](https://reliance-eosc.github.io/rohub-portal-documentation/docs/ROHub-navigation) which contains some examples [published by the EDS book community](https://reliance-eosc.github.io/rohub-portal-documentation/docs/ROHub-navigation/research_objects.html).