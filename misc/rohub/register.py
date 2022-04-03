# Import library
import sys
import rohub
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'book', '_temp', 'rohub'))
import config

# Authenticate
rohub.login(username=config.username, password=config.password)

# metadata
metadata_contribution = {
    'environment': 'forest',
    'topic': 'modelling',
    'filename': 'forest-modelling-treecrown_detectreeRGB',
    'title': 'Tree crown delineation using detectreeRGB',
    'inputs': {'input1':{'name':'Datasets of detectreeRGB AI4ER MRes Project',
                         'url':"https://doi.org/10.5281/zenodo.5494629"}},
    'outputs': {'content': 'vector, raster and figures',
               'url': "https://doi.org/10.5281/zenodo.6387953"},
    'author_GHuser': 'alan-turing-institute',
    'author_GHrepo': 'environmental-ds-book',
    'references':{'ref1':{'name':'detectreeRGB source code','url':"https://github.com/shmh40/detectreeRGB"},
                  },
    'sketch': {'title':'Image showing interactive plot of detectreeRGB model predictions of tree crown over a sample drone image in Sepilok, Sabah, Malaysia',
               'path':'book/_temp/forest-modelling-treecrown_detectreeRGB/interactive_plotting.png'}
}

title_nb = metadata_contribution['title']

metadata_rohub = {
    'title': f'{title_nb} (Jupyter Notebook) published in the Environmental Data Science book',
    'research_areas': ['Environmental research','Ecology'],
    'description': f'The research object refers to the {title_nb} notebook published in the Environmental Data Science book.',
    'ros_type': 'Executable Research Object',
    'ros_template': 'Executable Research Object folders structure',
}

# create
ro_title=metadata_rohub['title']
ro_research_areas=metadata_rohub['research_areas']
ro_description=metadata_rohub['description']
ro_ros_type=metadata_rohub['ros_type']
ro_ros_template=metadata_rohub['ros_template']

ro = rohub.ros_create(title=ro_title, research_areas=ro_research_areas, description=ro_description, ros_type=ro_ros_type, template=ro_ros_template)

# edition
authors=[
        {"user_id": "https://github.com/shmh40",
         "display_name": "Sebastian Hickman",
         "name": "Sebastian Hickman",
         "affiliation": "University of Cambridge"},
        # {"user_id": "https://orcid.org/0000-0003-0808-3480",
        #  "display_name": "Raquel Carmo",
        #  "name": "Raquel Carmo",
        #  "affiliation": "European Space Agency Φ-lab"},
        ]

ro.set_authors(agents=authors)

reviewers=[
    {"user_id": "https://github.com/acocac",
     "display_name": "Alejandro Coca-Castro",
     "name": "Alejandro Coca-Castro",
     "affiliation": "The Alan Turing Institute"},
    ]


ro.set_contributors(agents=reviewers)

# List RO Folders
myfolders = ro.list_folders()

## sketch
rese_folder=myfolders[myfolders.path=='output']['identifier'].values

resi_res_type="Sketch"
resi_file_path=metadata_contribution['sketch']['path']
resi_title=metadata_contribution['sketch']['title']

my_res_int0=ro.add_internal_resource(res_type=resi_res_type,file_path=resi_file_path, title=resi_title, folder=rese_folder[0])

## tool
rese_folder=myfolders[myfolders.path=='tool']['identifier'].values

rese_res_type="Jupyter Notebook"
rese_file_url=f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['author_GHrepo']}/tree/master/book/{metadata_contribution['environment']}/{metadata_contribution['topic']}/{metadata_contribution['filename']}.ipynb"
rese_title=f"Jupyter notebook"
rese_description="Jupyter Notebook hosted by the Environmental Data Science Book"

my_res_ext0=ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title, description=rese_description, folder=rese_folder[0])

## input
rese_folder=myfolders[myfolders.path=='input']['identifier'].values
rese_res_type = "Dataset"

if len(metadata_contribution['inputs']) > 0:
    for i in metadata_contribution['inputs']:
        rese_file_url=metadata_contribution['inputs'][i]['url']
        rese_title=f"Input {metadata_contribution['inputs'][i]['name']}"
        rese_description=f"Contains input {metadata_contribution['inputs'][i]['name']} used in the Jupyter notebook of {metadata_contribution['title']}"
        my_res_ext0=ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title, description=rese_description, folder=rese_folder[0])

## output
rese_folder=myfolders[myfolders.path=='output']['identifier'].values

rese_res_type="Dataset"
rese_file_url=metadata_contribution['outputs']['url']
rese_title=f"Outputs"
rese_description=f"Contains outputs, ({metadata_contribution['outputs']['content']}), generated in the Jupyter notebook of {metadata_contribution['title']}"
my_res_ext0=ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title, description=rese_description, folder=rese_folder[0])

## biblio
rese_folder=myfolders[myfolders.path=='biblio']['identifier'].values
rese_res_type="Bibliographic Resource"

if len(metadata_contribution['inputs']) > 0:
    for i in metadata_contribution['references']:
        rese_file_url=metadata_contribution['references'][i]['url']
        rese_title=metadata_contribution['references'][i]['name']
        rese_description = f"Related publication of the {metadata_contribution['topic']} presented in the Jupyter notebook"
        my_res_ext0 = ro.add_external_resource(res_type=rese_res_type, url=rese_file_url, title=rese_title,
                                               description=rese_description, folder=rese_folder[0])

# license
MIT_index = rohub.list_available_licenses().index("MIT")
ro.set_license(license_id=rohub.list_available_licenses()[MIT_index])