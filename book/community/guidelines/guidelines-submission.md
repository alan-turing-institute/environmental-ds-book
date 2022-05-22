(cm-guidelines-submission)=
# Submission guidelines

## Repository structure

The public GitHub repository has the following structure:

```
| The Environmental Data Science Book
| ├── **/.github**
| │   ├── ISSUE_template
| │   ├── workflows
| │   └── ...
| ├── **/book**
| │   ├── _toc.yml
| │   ├── _config.yml
| │   └── ...
| ├── CODE_OF_CONDUCT.md
| ├── CONTRIBUTING.md
| └── ...
```

The `.github folder` refers to GitHub related deployment files and templates of issues/pull requests usually curated by the repository maintainers or developers. The `book folder` holds the website content and other relevant files (table of content and configuration files).  

For the book content, the following contributions are accepted:
* **Narrative content**: include plain text, citations, equations, figures, special content blocks and more.
* **Executable content**: consists of computational material in a given programming language e.g. python along a narrative.

:::{seealso}
Please visit the corresponding Jupyter Book guidelines for [`narrative`](https://jupyterbook.org/content/index.html#write-narrative-content) and [`executable`]('https://jupyterbook.org/execute/index.html#write-executable-content) content. 
:::

The `_toc.yml` file sets the main sections of the Environmental DS book. It is a simple configuration file specifying a table of content from all the executable and narrative content found in the ``book`` folder (and in subfolders). The current version of the book consists of four key sections:

* **Preamble**: contains narrative content i.e. plain markdown files describing the aims of the book, the target audience, how to use and attribution.
* **Gallery**: provides narrative and executable content by theme. We set different themes: exploration, modelling, etc to differentiate the type of analysis or procedure.
* **Community**: compiles community-related resources such as notes of co-working meetings, templates for new executable content i.e. demonstrators and interesting readings.  
* **Afterword**: describe miscellaneous material such as glossary, bibliography and execution statistics. 

## Contribution of executable notebooks

The contribution process has three main steps: navigation, preparation and submission.

### Navigation

We encourage you to navigate existing templates of proposed topics or themes which are available in the community section (see {ref}`Templates <cm-templates>`). The proposed themes are described below.
* **Exploration**: highlights a particular environmental sensor with visualisation and interpretation of the corresponding layers of information.
* **Preprocessing**: refers to all procedures to clean and prepare environmental data for analysis. The notebook should highlight differences between the raw and preprocessed data.
* **Modelling**: comprises models to analyse a given environmental system. 
* **Post-processing**: refers to post-process routines to fine tune and/or adjust modelling outputs.

In addition to defining the target environmental system and theme, we suggest inspecting existing published notebooks to have some notions about the expected content. For instance, a common component of the notebooks is their interactive plotting. For python notebooks, we suggest to watch [this recent webinar](https://event.on24.com/wcc/r/3296081/71BDD53E21EC72B3ACA24FEC98EE2A7C?mode=login&email=acocac@gmail.com) about open-source packages for handling and visualising geospatial data. Some of these packages have been successfully used in the existing notebooks of the Environmental DS book, including `intake` for data cataloguing and `hvplot` for interactive plotting. 

### Preparation

The following procedures will prepare you to make submission: 

* Log the notebook idea in [issues](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose).
* Go to the [Environmental Data Science book organisation](https://github.com/Environmental-DS-Book) which is dedicated to host notebooks.
* Copy the chosen notebook template to a new folder with the name of the target theme inside the directory of the target environmental system. 
* Rename the filename of the template to the pattern (XXX-YYY-ZZZ, where XXX refers to the environmental system, YYY to the theme and ZZZ to a preferred identifier of the model, sensor or pre/post-processing pipeline). For example, "forest-modelling-treecrown.ipynb".
* Fill the information header according to your use case. Be free to guide from previous modelling notebooks, see for instance the [IceNet notebook](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/polar/modelling/polar-modelling-icenet.ipynb).
* Change the structure of the remaining sections of the notebook according to your preference.
  * We advise following the 10 rules of compelling notebooks provided by the EarthCube initiative available in their [Notebook Template](https://github.com/earthcube/NotebookTemplates/blob/main/EC_05_Template_Notebook_for_EarthCube_Long_Version.ipynb) (section `Data processing and analysis`).
* Test the notebook is working according to your virtual or conda environment.
  * Not familiar with open-source `python` packages? We suggest exploring [Pangeo stack](https://pangeo.io/). The Pangeo community curates a wide diversity of environments in the `pangeo-docker-images` [repository](https://github.com/pangeo-data/pangeo-docker-images/tree/master/pangeo-notebook). 
  * For notebooks, we suggest using the `pangeo-notebook` conda environment available [here](https://github.com/pangeo-data/pangeo-docker-images/blob/master/pangeo-notebook/environment.yml). The environment can be installed in your system using `conda env create -f environment.yml`.
* Note, the Binder does not provide GPU support, so we would suggest testing the notebook works with cpu when predicting from the pretrained models. 

### Submission
Once you have tested a draft version of the notebook containing the information in the heading and remaining sections, you make a pull request. You will have to fill a form with a series of questions related to the contribution. Please complete them. If you have any questions, please send a direct message to [environmental.ds.book@gmail.com](mailto:environmental.ds.book@gmail.com]).

## Attribution 
Some material in this section has been adapted from [Neurolibre submission guidelines](https://docs.neurolibre.org/en/latest/SUBMIT.html), released under CC BY 3.0. 
