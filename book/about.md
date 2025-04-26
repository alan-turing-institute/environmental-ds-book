(about)=

# About

Notebooks has been an excellent tool for prototyping and writing examples to showcase computational analyses [@Rule2019].
EDS book complements the science and methodological development of academic journals by translating research outputs into FAIR notebooks using open infrastructure and open review ([](#notebook-cycle)).

```{figure} images/notebook-cycle.jpg
:label:notebook-cycle
:alt: The Environmental Data Science project aims to engage the wider scientific research community on information extraction and analysis from environmental sensors using innovative data science.

The EDS book community supports and connects environmental scientists and practitioners to communicate their science through customisable interactive notebooks which benefit from a collaborative reviewing process. Illustration by Scriberia as part of _The Turing Way_ book dash in November 2022 [@ttw-scriberia_illustrations].
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

For more information on who can contribute, please see [the contributors section](./contribute.md).

# Why EDS book notebooks?

EDS book notebooks contributes to open, collaborative and transparent Environmental science. 
A shared goal among our community-driven notebooks is to increase awareness and demonstrate open-source software developments and open data suited to Environmental science. 

EDS book notebooks support FAIR principles for research software (FAIR4RS) [@Barker2022-FAIR4RS] as describe below:

- **F - Findable. Software, and its associated metadata, is easy for both humans and machines to find**: 
   - All notebooks are hosted as separate repositories in [the EDS book GitHub organisation](https://github.com/eds-book).
   - Rendered versions of notebooks are indexed and centralized into a [core repository](https://github.com/alan-turing-institute/environmental-ds-book/) hosted at the Alan Turing Institute GitHub organisation. 
   - Notebooks metadata is accessible through [ROHub](https://reliance.rohub.org/), a Research Object management platform that enables researchers to collaboratively manage, share and preserve their research work (read further in [the technologies section](#about-technologies)). 
- **A - Accessible. Software, and its metadata, is retrievable via standardised protocols**: 
  - Notebooks repositories can be retrieved from git clone.
  - RoHub curates EDS book notebooks with their metadata using [Research Object Crate (RO-Crate)](https://www.researchobject.org/ro-crate/). 
- **I - Interoperable. Software interoperates with other software by exchanging data and/or metadata, and/or through interaction via application programming interfaces (APIs), described through standards**: 
  - The Jupyter ecosystem facilitates exchanging data and/or metadata of all published notebooks through standardised protocols, including a [RESTful web service  architecture implemented in Jupyter notebook](https://github.com/jupyter/jupyter/wiki/Jupyter-Notebook-Server-API).
  - Notebooks repositories have a dedicated folder to provide lock environments which pin dependencies according to three main operating systems: Windows, Linux and MacOS. 
- **R - Reusable. Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software)**: 
  - Users have multiple pathways to run notebooks. Notebooks repositories contain clear instructions on how to install their computational environment and dependencies in users own system. We also lower the barrier to access notebooks through public or community cloud-based services in Binder and Jupyter Hubs.
  - Notebook repositories and their RoHub repositories can be reused under an OSI-approved MIT license.

Additional to following FAIR principles, we expand the pedagogical possibilities of Jupyter Notebook and community-centred open infrastructure services.
Furthermore, we contribute in building and connecting the international community of environmental data scientists and enthusiasts in open-source developments at all levels of seniority.

Since the official launch of EDS book in December 2021, the community has successfully published numerous notebooks covering exploration, preprocessing and modelling from environmental datasets.

(about-technologies)=
# Technologies 
This section indicates the main technologies for EDS book and published notebooks.

## Binder
The Binder project offers an easy place to share computing environments to everyone. 
It allows users to specify custom environments and share them with a single link. 
Use cases involve workshops, scientific workflows and streamline sharing among teams.

Binder is entirely powered by an open-source infrastructure stack. 
Its main two tools are BinderHub, which is an open-source tool that deploys the Binder service in the cloud, and repo2docker, which generates reproducible Docker images from a git repository. 
The Binder team also runs a public BinderHub deployment at mybinder.org as a free public service for the community.

For EDS book notebooks, we use tbe public BinderHub to provide a cloud-based service for users to run notebooks without installing any software on their local machine.
Besides the public service, we suggest launching notebooks in the [EGI BinderHub](https://replay.notebooks.egi.eu/) deployment, a private BinderHub instance hosted by the [European Grid Infrastructure](https://www.egi.eu/) (EGI) and the [European Open Science Cloud](https://eosc-portal.eu/) (EOSC) initiative.

You can find out more about Project Binder on their About mybinder.org page.

## MyST
{abbr}`MyST (Markedly Structured Text)` is an open-source, community-driven markup language project building upon [CommonMark](https://commonmark.org/) (a standard form of Markdown) with special syntax extensions [@Cockett_2024].
In 2022, the [Executable Books project](https://executablebooks.org), which hosts Jupyter Book and MyST, started work on the `mystmd` command line interface (CLI), which was initially developed  as the Curvenote CLI, and later transferred to the ExecutableBooks project.
In June 2024, MyST Markdown officially became part of Project Jupyters.
For EDS book, [Jupyter Book](https://next.jupyterbook.org), a distribution of the MyST Document Engine, is used to render the content of the book and notebooks.

For more about MyST, see in https://mystmd.org/.

## ReviewNB
The interaction between authors and reviewers in notebook submissions for EDS book is facilitated through [ReviewNB](https://www.reviewnb.com/), a third-party plugin in GitHub for displaying and commenting Jupyter Notebooks. 
ReviewNB is a GitHub-verified marketplace app that renders all interactive HTML/JavaScript notebook outputs, except bokeh-related widgets. 
The app allows commenting on rich diffs and it will render even the largest of notebooks without timing out.

The main features of ReviewNB according to its [official documentation](https://docs.reviewnb.com/index.html) are:

- [Visual diff](https://uploads-ssl.webflow.com/5ba4ebe021cb91ae35dbf88c/5ba93ded243329a486dab26e_sl-code%2Bimage.png) for every commit or pull request containing Notebooks
- [Commenting](https://uploads-ssl.webflow.com/5ba4ebe021cb91ae35dbf88c/5c7d0095d99ee508018a9878_Screenshot%202019-03-04%20at%204.08.48%20PM.png) on the notebook diff to start discussion
- [Conversation threads](https://uploads-ssl.webflow.com/5ba4ebe021cb91ae35dbf88c/5c7eb42d7cef320c0133d1c6_threads-v2.png) to track all open discussions
- [Team conversations](https://blog.reviewnb.com/commenting-for-jupyter/) directly on Jupyter Notebooks

For more about ReviewNB, see in https://blog.reviewnb.com/.

## RoHub

RoHub [@rohub-2018] is a Research Object management platform that enables researchers to collaboratively manage, share and preserve their research work (data, software, workflows, models, presentations, videos, articles, etc.). 
RoHub implements the full RO model and paradigm: resources associated to a particular research work are aggregated into a single FAIR digital object, and metadata relevant for understanding and interpreting the content is represented as semantic metadata that are user and machine-readable.
All EDS book notebooks are findable in RoHub.
RoHub allows tracking all research life cycle and derivative work of EDS book notebooks.

For more about RoHub, see in https://reliance.rohub.org/.