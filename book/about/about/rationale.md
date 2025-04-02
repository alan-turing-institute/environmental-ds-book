(about-rationale)=

### Why EDS book notebooks?

EDS book notebooks contributes to open, collaborative and transparent Environmental science. 
A shared goal among our community-driven notebooks is to increase awareness and demonstrate open-source software developments and open data suited to Environmental science. 
Building upon recent efforts by [EarthCube Peer-Reviewed Jupyter Notebooks initiative](https://www.earthcube.org/notebooks), EDS book notebooks advance in providing standards and guidelines for evaluating notebooks and their quality. 

EDS book notebooks support FAIR principles for research software (FAIR4RS){cite}`Barker2022-FAIR4RS` as describe below:

- **F: Software, and its associated metadata, is easy for both humans and machines to find**: 
   - All notebooks are hosted as separate repositories in [EDS Book Gallery GitHub organisation](https://github.com/eds-book-gallery). 
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
