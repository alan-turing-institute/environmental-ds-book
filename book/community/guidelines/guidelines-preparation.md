(cm-guidelines-preparation)=

# Preparation

## Corresponding author
After validating the notebook idea, a first draft of the notebook should be created by using a notebook repository template according to the target programming language, [Python](https://github.com/Environmental-DS-Book/template_python), R or Julia. 

The repository templates are adapted from [2i2c hub-user-image-template](https://github.com/2i2c-org/hub-user-image-template). 
The corresponding author should open a Pull Request to start editing the notebook and dependencies files. 
Within each PR, a comment will be added containing "Test this PR on Binder" badge. 
The editorial team will use the binder badge to check how reproducible is the notebook and its viability for the reviewing stage. 

Some general guidelines are:
* Fill the information header according to your use case. Be free to guide from previous published notebooks, see for instance the [IceNet notebook](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/gallery/modelling/polar-modelling-icenet.ipynb).
* Change the structure of the remaining sections of the notebook according to your preference.
  * We advise following the 10 rules of compelling notebooks provided by the EarthCube initiative available in their [Notebook Template](https://github.com/earthcube/NotebookTemplates/blob/main/EC_05_Template_Notebook_for_EarthCube_Long_Version.ipynb) (section `Data processing and analysis`). 

* For `python` packages, we suggest exploring the [Pangeo stack](https://pangeo.io/). The Pangeo community curates a wide diversity of environments in the `pangeo-docker-images` [repository](https://github.com/pangeo-data/pangeo-docker-images/tree/master/pangeo-notebook). 
  * For notebooks, we suggest using the `pangeo-notebook` conda environment available [here](https://github.com/pangeo-data/pangeo-docker-images/blob/master/pangeo-notebook/environment.yml). The environment can be installed in your system using `conda env create -f environment.yml`.

* Test the notebook is working according to the Binder badge in the PR.
* Note, the Binder does not provide GPU support, so we suggest testing the notebook works with cpu when predicting from the pretrained models. 

Once you have tested a draft version of the notebook containing the information in the heading and remaining sections, please transfer the repository to the [Environmental Data Science book organisation](https://github.com/Environmental-DS-Book). A maintainer of the EDS book will assist you to add the notebook to a new branch in the main repo. After, a pull request will be created.

## Editorial team
The notebook in the transferred repository should generate the same outputs as the initial repository hosted in the GitHub account of the corresponding author. 

Then if it generates the same results,  create a review branch in which will tag corresponding author and reviewers indicating the main aspects of the review process. 

Rename the filename of the template to the pattern (XXX-YYY-ZZZ, where XXX refers to the environmental system, YYY to the theme and ZZZ to a preferred identifier of the model, sensor or pre/post-processing pipeline). For example, "forest-modelling-treecrown.ipynb".

In the PR, you will have to fill a form with a series of questions related to the contribution. Please complete them. If you have any questions, please send a direct message to [environmental.ds.book@gmail.com](mailto:environmental.ds.book@gmail.com]).
