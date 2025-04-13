(about)=

# About

Notebooks has been an excellent tool for prototyping and writing examples to showcase computational analyses {cite}`10.1371/journal.pcbi.1007007`.
EDS book complements the science and methodological development of academic journals by translating research outputs into FAIR notebooks using open infrastructure and open review ([](#notebook-cycle)).

```{figure} images/notebook-cycle.jpg
:label:notebook-cycle
:alt: The Environmental Data Science project aims to engage the wider scientific research community on information extraction and analysis from environmental sensors using innovative data science.

The EDS Book community supports and connects environmental scientists and practitioners to communicate their science through customisable interactive notebooks which benefit from a collaborative reviewing process. Illustration by Scriberia as part of _The Turing Way_ book dash in November 2022. Zenodo. [http://doi.org/10.5281/zenodo.7587336](http://doi.org/10.5281/zenodo.7587336)
```

# Vision

Environmental scientists work collaboratively to demonstrate and communicate their science through FAIR executable notebooks and have gained significant skills to publish in notebook-based scholarly publication systems.

# Mission

Educate and leverage good scientific software and data management practices among environmental scientists through peer-reviewed findable, accessible, interoperable and reusable (FAIR) executable notebooks.

In addition to the book, our goal is to build a computational notebook community putting open science into practice towards collaborative, reusable and transparent environmental research.

# Who is the book for?

While the scientific community is broad, we think the target audience of this book is:

* Researchers with some background in environmental science interested in AI and data science methods.
* Researchers with some background in computer science interested in environmental data science.  
* Anyone else interested in reproducibility, inclusive, shareable and collaborative open environmental science.

# Why EDS book notebooks?

EDS book notebooks contributes to open, collaborative and transparent Environmental science. 
A shared goal among our community-driven notebooks is to increase awareness and demonstrate open-source software developments and open data suited to Environmental science. 

EDS book notebooks support FAIR principles for research software (FAIR4RS){cite}`Barker2022-FAIR4RS` as describe below:

- **F: Software, and its associated metadata, is easy for both humans and machines to find**: 
   - All notebooks are hosted as separate repositories in [EDS Book GitHub organisation](https://github.com/eds-book). 
   - Rendered versions of notebooks are indexed and centralized into a Jupyter Book hosted as [a repository in the Alan Turing Institute GitHub organisation](https://github.com/alan-turing-institute/environmental-ds-book/). 
   - GitHub allows handling notebooks versioning and discoverability through its integration with Zenodo.
- **A: Software, and its metadata, is retrievable via standardised protocols**: 
  - Notebooks repositories can be retrieved through git clone.
- **I: Software interoperates with other software by exchanging data and/or metadata, and/or through interaction via application programming interfaces (APIs), described through standards**: 
  - The Jupyter ecosystem facilitates exchanging data and/or metadata of all published notebooks.  through standardised protocols, including a [RESTful web service  architecture implemented in Jupyter notebook](https://github.com/jupyter/jupyter/wiki/Jupyter-Notebook-Server-API).
  - Notebooks repositories have a dedicated folder to provide lock environments which pin dependencies according to three main operating systems: Windows, Linux and MacOS. 
- **R: Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software)**: 
  - Users have multiple pathways to run notebooks. Notebooks repositories contain clear instructions on how to install their computational environment and dependencies in users own system. We also lower the barrier to access notebooks through public or community cloud-based services in Binder and JupyterHubs.
  - Notebook repositories and their RoHub repositories can be reused under an OSI-approved MIT license.

Additional to following FAIR principles, we expand the pedagogical possibilities of Jupyter Notebook and community-centred open infrastructure services.
We aim to build and connect a community of environmental data scientists and enthusiasts in open-source developments at all levels of seniority.

Since the official launch of EDS book in December 2021, the community has successfully published numerous notebooks covering exploration, preprocessing and modelling from environmental datasets.

# Themes
EDS notebooks are categorized under four proposed topics or themes:

* **Exploration**: highlights a particular environmental sensor with visualization and interpretation of the corresponding layers of information.
* **Preprocessing**: refers to all procedures to clean and prepare environmental data for analysis. The notebook should highlight differences between the raw and preprocessed data.
* **Modelling**: comprises models to analyse a given environmental system. 
* **Post-processing**: refers to post-process routines to fine tune and/or adjust modelling outputs.

We cover further details of submission and reviewing processes in the [guidelines section](pb-guidelines).

# Technologies in EDS book
This section indicates the main technologies for EDS book and published notebooks.

## Notebooks
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