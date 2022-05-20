# Import library
import sys
import rohub
import os
sys.path.insert(0, os.path.join(os.getcwd(), 'misc', 'rohub'))
import config

# Authenticate
rohub.login(username=config.username, password=config.password)

# metadata
metadata_contribution = {
    'environment': 'agriculture',
    'topic': 'exploration',
    'filename': 'agriculture-exploration-cosmosuk',
    'title': 'Cosmos-UK soil moisture',
    'inputs': {'input1':{'name':"Inputs of the Jupyter Notebook - Cosmos-UK soil moisture",
                         'url':"https://doi.org/10.5281/zenodo.6567018"},
               },
    'outputs': {'content': 'table and figures',
               'url': "https://doi.org/10.5281/zenodo.6566942"},
    'author_GHuser': 'Environmental-DS-Book',
    'references':{'ref1':{'name':'Daily and sub-daily hydrometeorological and soil data (2013-2019) [cosmos-uk]','url':"https://doi.org/10.5285/b5c190e4-e35d-40ea-8fbe-598da03a1185"},
                  'ref2':{'name':'Soil water content in southern england derived from a cosmic-ray soil moisture observing system – cosmos-uk','url':"https://doi.org/10.1002/hyp.10929"},
                  'ref3':{'name':'Cosmos: the cosmic-ray soil moisture observing system','url':"https://doi.org/10.5194/hess-16-4079-2012"}},
    'sketch': {'title':'Image showing interactive plot of IceNet seasonal forecasts of Artic sea ice according to four lead times and months in 2020',
               'path':'_temp/rohub/agriculture-exploration-cosmosuk/interactive_plotting.png'}
}

title_nb = metadata_contribution['title']

metadata_rohub = {
    'title': f'{title_nb} (Jupyter Notebook) published in the Environmental Data Science book',
    'research_areas': ['Environmental research', 'Soil science', 'Hydrology'],
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
        {"user_id": "https://github.com/acocac",
         "display_name": "Alejandro Coca-Castro",
         "name": "Alejandro Coca-Castro",
         "affiliation": "The Alan Turing Institute"},
        # {"user_id": "https://orcid.org/0000-0003-0808-3480",
        #  "display_name": "Raquel Carmo",
        #  "name": "Raquel Carmo",
        #  "affiliation": "European Space Agency Φ-lab"},
        ]

ro.set_authors(agents=authors)

reviewers=[
    {"user_id": "https://github.com/dorankhamis",
     "display_name": "Doran Khamis",
     "name": "Doran Khamis",
     "affiliation": "UK Centre for Ecology & Hydrology"},
    {"user_id": "https://github.com/mattfry-ceh",
     "display_name": "Matt Fry",
     "name": "Matt Fry",
     "affiliation": "UK Centre for Ecology & Hydrology"},
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
rese_file_url=f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['filename']}/tree/master/{metadata_contribution['filename']}.ipynb"
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