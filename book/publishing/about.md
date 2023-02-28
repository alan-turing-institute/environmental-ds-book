(pb-about)=

# About EDS book notebooks
With the great diversity in open data, software and computational resources, environmental data science research and applications have accelerated rapidly. 
This presents a timely opportunity for advancing the cyberinfrastructure for showcasing these emerging developments. 
Building upon existing open science communities such as the [Turing Way](https://the-turing-way.netlify.app/) and [Pangeo](https://pangeo.io), EDS book aims at educating and leveraging good scientific software and data management practises among environmental scientists through peer-reviewed findable, accessible, interoperable and reusable (FAIR) computational notebooks. 

Computation notebooks (CNs) allow users to combine interactive code with text and graphical objects. 
CNs have become a successful mechanism for sharing the analysis of data and documenting research workflows. 
Notebooks has been an excellent tool for prototyping and writing examples to showcase a piece of software. 

The EDS book aims to complement the science and methodological development embedded within academic journals using open infrastructure to translate research outputs into FAIR notebooks which benefit from a collaborative and open reviewing process (Figure 2).

```{figure} ../figures/notebook-cycle.jpg
---
name: notebook-cycle
alt: The Environmental Data Science project aims to engage the wider scientific research community on information extraction and analysis from environmental sensors using innovative data science.
---
The EDS Book community supports and connects Environmental scientists and practitioners to communicate their science through customisable interactive notebooks which benefit from a collaborative reviewing process. Illustration by Scriberia as part of _The Turing Way_ book dash in November 2022. Zenodo. [http://doi.org/10.5281/zenodo.7587336](http://doi.org/10.5281/zenodo.7587336)
```

### Why EDS book notebooks?
EDS book notebooks contributes to open, collaborative and transparent Environmental science. 
A shared goal among our community-driven notebooks is to increase awareness and demonstrate open-source software developments and open data suited to Environmental science. 
Building upon recent efforts by [EarthCube Peer-Reviewed Jupyter Notebooks initiative](https://www.earthcube.org/notebooks), EDS book notebooks advance in providing standards and guidelines for evaluating notebooks and their quality. 

EDS book notebooks support FAIR principles for research software (FAIR4RS){cite}`Barker2022-FAIR4RS` as describe below:

- **F: Software, and its associated metadata, is easy for both humans and machines to find**: 
   - All notebooks are hosted as separate repositories in [EDS Book GitHub organisation](https://github.com/Environmental-DS-Book). 
   - Rendered versions of notebooks are indexed and centralized into a Jupyter Book hosted as [a repository in the Alan Turing Institute GitHub organisation](https://github.com/alan-turing-institute/environmental-ds-book/). 
   - Notebooks metadata (inputs, outputs, bibliography and software) are findable in [ROHub](https://reliance.rohub.org/), a Research Object management platform that enables researchers to collaboratively manage, share and preserve their research work (read further in [the technologies sections of EDS book notebooks](pb-about-techologies)). 
   - The same platform allows handling notebooks versions and assign distinct identifiers. 
- **A: Software, and its metadata, is retrievable via standardised protocols**: 
  - Notebooks repositories can be retrieved from Git Clone from GitHub.
  - RoHub packages EDS book notebooks with their metadata using [Research Object Crate (RO-Crate)](https://www.researchobject.org/ro-crate/). 
- **I: Software interoperates with other software by exchanging data and/or metadata, and/or through interaction via application programming interfaces (APIs), described through standards**: 
  - The Jupyter ecosystem facilitates exchanging data and/or metadata of all published notebooks.  through standardised protocols, including a [RESTful web service  architecture implemented in Jupyter notebook](https://github.com/jupyter/jupyter/wiki/Jupyter-Notebook-Server-API).
  - Notebooks repositories have a dedicated folder to provide lock environments which pin dependencies according to three main operating systems: Windows, Linux and MacOS. 
- **R: Software is both usable (can be executed) and reusable (can be understood, modified, built upon, or incorporated into other software)**: 
  - Users have multiple pathways to run notebooks. Notebooks repositories contain clear instructions on how to install their computational environment and dependencies in users own system. We also lower the barrier to access notebooks through public or community cloud-based services in Binder and JupyterHubs.
  - Notebook repositories and their RoHub repositories can be reused under an OSI-approved MIT license.

Additional to following FAIR principles, we expand the pedagogical possibilities of Jupyter Notebook and community-centred open infrastructure services.
We aim to build and connect a community of environmental data scientists and enthusiasts in open-source developments at all levels of seniority.

Since the official launch of EDS book in December 2021, the community has successfully published numerous notebooks covering exploration, preprocessing and modelling from environmental datasets.

## Attribution
Some material in this section and derived content has been adapted from [The Turing Way](https://the-turing-way.netlify.app/), the [Journal of Open Source Education](https://openjournals.readthedocs.io/en/jose/index.html) and [pyOpenSci](https://www.pyopensci.org/software-peer-review/index.html) content, released under CC BY 4.0, CC BY 4.0 and CC BY-SA 4.0, respectively. 