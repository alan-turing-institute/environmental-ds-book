# Import library
import sys
import rohub
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'misc', 'rohub'))
import config

# Authenticate
rohub.login(username=config.username, password=config.password)

post_publication = False

metadata_contribution = {
    'environment': 'agriculture',
    'topic': 'exploration',
    'filename': 'agriculture-exploration-cosmosuk',
    'title': 'Cosmos-UK soil moisture',
    'author_GHuser': 'Environmental-DS-Book',
    'conda_os_files': ['linux', 'osx', 'win'],
    'requirements_txt': False
}

myros = rohub.list_my_ros()

ro_id = myros[myros.title.str.startswith(metadata_contribution['title'])]['identifier']
ro=rohub.ros_load(identifier=ro_id.values[0])

if post_publication:
    ### UPDATE GITHUB REPO
    ## resources
    results=ro.list_resources()

    # jupyter notebook
    rese_title=f"Jupyter Notebook of {metadata_contribution['title']}"

    rese_file_url="https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/ocean/modelling/ocean-modelling-litter-philab.ipynb"

    res_id = results[results.title == rese_title]['identifier'].values[0]
    my_res1=rohub.resource_load(identifier=res_id)
    my_res1.show_metadata()
    rese_file_url="https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/ocean/modelling/ocean-modelling-litter-philab.ipynb"
    my_res1.update_content(input_url=rese_file_url)

## UPLOAD PUBLICATION
# List RO Folders
myfolders = ro.list_folders()

## output
rese_folder=myfolders[myfolders.path=='tool']['identifier'].values

### rendered version
rese_res_type="Publication"
rese_file_url=f"https://the-environmental-ds-book.netlify.app/gallery/{metadata_contribution['topic']}/{metadata_contribution['filename']}/{metadata_contribution['filename']}.html"
rese_title=f"Online rendered version of the Jupyter notebook"
rese_description="Rendered version of the Jupyter Notebook hosted by the Environmental Data Science Book"

my_res_ext0=ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title, description=rese_description, folder=rese_folder[0])

### lock files
rese_res_type = "File"

def lock_file(lock_os):
    rese_file_url=f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['filename']}/tree/master/.binder/conda-{lock_os}-64.lock"
    rese_title=f"Lock conda file for {lock_os}-64"
    rese_description=f"Lock conda file for {lock_os}-64 OS of the Jupyter notebook hosted by the Environmental Data Science Book"
    ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title, description=rese_description, folder=rese_folder[0])

[lock_file(i) for i in metadata_contribution['conda_os_files']]

if metadata_contribution['requirements_txt']:
    ###requirements - only if needed
    rese_res_type = "File"
    rese_file_url = f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['author_GHrepo']}/tree/master/.binder/requirements.txt"
    rese_title = f"Pip requirements for lock conda environments"
    rese_description = f"Pip requirements file containing libraries to install after conda lock"
    ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title, description=rese_description, folder=rese_folder[0])

###environment.yml
rese_res_type = "File"
rese_file_url = f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['filename']}/tree/master/.binder/environment.yml"
rese_title = f"Conda environment"
rese_description = f"Conda environment when user want to have the same libraries installed without concerns of package versions"
ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title, description=rese_description, folder=rese_folder[0])

##add location
geojson = 'book/_temp/forest-modelling-treecrown_detectreeRGB/studyarea.geojson'
ro.add_geolocation(body_specification_json=geojson)

##MODIFY
## modify conda
rese_title=f"Input"

res_id = results[results.title.str.startswith(rese_title)]['identifier'].values[0]
my_res1=rohub.resource_load(identifier=res_id)
my_res1.show_metadata()

rese_title=f"Input images"
my_res1.title=rese_title
my_res1.update_metadata()

my_res1.update_content(title=rese_title)

#add contributor
reviewers=[
    {"user_id": "https://github.com/acocac",
     "display_name": "Alejandro Coca-Castro",
     "name": "Alejandro Coca-Castro",
     "affiliation": "The Alan Turing Institute"},
    ]

ro.set_contributors(agents=reviewers)