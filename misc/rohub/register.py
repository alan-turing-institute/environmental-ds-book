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
    'environment': 'ocean',
    'topic': 'modelling',
    'reponame': '3286b92f-4fae-4cc6-a29e-e408bc844542',
    'title': "Learning the Underlying Physics of a Simulation Model of the Ocean's Temperature (CIRC23)",
    'inputs': {'input1':{'name':'MITgcm Dataset for paper: Sensitivity analysis of a data-driven model of ocean temperature (v1.1)',
                         'url':'https://doi.org/10.5281/zenodo.7919172'},
                'input2':{'name':'Reproducible Challenge - Team 3 - Sensitivity analysis- Models',
                         'url':'https://doi.org/10.5281/zenodo.7954232'}
               },
    'outputs': {'content': 'figures',
               'url': "https://doi.org/10.5281/zenodo.8271978"},
    'author_GHuser': 'eds-book-gallery',
    'references':{'ref1':{'name':'A sensitivity analysis of a regression model of ocean temperature','url':"http://doi.org/10.1017/eds.2022.10"}},
    'sketch': {'title':'Image showing spatially averaged errors from the model trained with only a 2D neighborhood of inputs',
               'path':'_temp/rohub/circ2023-team3/plot.png'}
}

title_nb = metadata_contribution['title']

metadata_rohub = {
    'title': f'{title_nb} (Jupyter Notebook) published in the Environmental Data Science book',
    'research_areas': ['Environmental research', 'Ocean science', 'Climate science'],
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

ro = rohub.ros_create(title=ro_title, research_areas=ro_research_areas, description=ro_description, ros_type=ro_ros_type, use_template=ro_ros_template)

# edition
authors=[
        {"agent_type": "user",
         "display_name": "Garima Malhotra",
         "name": "Garima Malhotra",
         "orcid_id": None,
         "email": "garima.malhotra@colorado.edu",
         "affiliation": "University of Colorado Boulder"},
        {"agent_type": "user",
         "display_name": "Daniela Pinto Veizaga",
         "name": "Daniela Pinto Veizaga",
         "email": "daniela.pinto@berkeley.edu",
         "orcid_id": None,
         "affiliation": "University of California, Berkeley"},
        {"agent_type": "user",
         "display_name": "Jorge Eduardo Peña Velasco",
         "name": "Jorge Eduardo Peña Velasco",
         "email": "jorge_eduardo2894@hotmail.com",
         "orcid_id": None,
         "affiliation": "Claremont McKenna College"}
        ]

ro.set_authors(agents=authors)

reviewers=[
    {"user_id": "https://github.com/RachelFurner",
     "display_name": "Rachel Furner",
     "name": "Rachel Furner",
     "email": "raf59@damtp.cam.ac.uk",
     "affiliation": "University of Cambridge"},
    {"user_id": "https://github.com/oscarbau",
     "display_name": "Oscar Bautista",
     "name": "Oscar Bautista",
     "affiliation": "World Food Programme",
     "email": "ovbautistac@unal.edu.co"
     },
    {"user_id": "https://github.com/ricardobarroslourenco",
     "display_name": "Ricardo Barros Lourenço",
     "name": "Ricardo Barros Lourenço",
     "affiliation": "McMaster University",
     "email": "barroslr@mcmaster.ca"
     },
        ]

ro.set_contributors(agents=reviewers)

# List RO Folders
myfolders = ro.list_folders()

## sketch
rese_folder=myfolders[myfolders.path=='output']['identifier'].values

resi_res_type="Sketch"
resi_file_path=metadata_contribution['sketch']['path']
resi_title=metadata_contribution['sketch']['title']

my_res_int0=ro.add_internal_resource(res_type=resi_res_type,file_path=resi_file_path, title=resi_title, folder='output')

## tool
rese_res_type="Jupyter Notebook"
rese_file_url=f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['reponame']}/blob/main/notebook.ipynb"
rese_title=f"Jupyter notebook"
rese_description="Jupyter Notebook hosted by the Environmental Data Science Book"

my_res_ext0=ro.add_external_resource(res_type=rese_res_type, input_url=rese_file_url, title=rese_title, description=rese_description, folder='tool')

## input
rese_res_type = "Dataset"

if len(metadata_contribution['inputs']) > 0:
    for i in metadata_contribution['inputs']:
        rese_file_url=metadata_contribution['inputs'][i]['url']
        rese_title=f"Input {metadata_contribution['inputs'][i]['name']}"
        rese_description=f"Contains input {metadata_contribution['inputs'][i]['name']} used in the Jupyter notebook of {metadata_contribution['title']}"
        my_res_ext0=ro.add_external_resource(res_type=rese_res_type, input_url=rese_file_url, title=rese_title, description=rese_description, folder='input')

## output
rese_res_type="Dataset"
rese_file_url=metadata_contribution['outputs']['url']
rese_title=f"Outputs"
rese_description=f"Contains outputs, ({metadata_contribution['outputs']['content']}), generated in the Jupyter notebook of {metadata_contribution['title']}"
my_res_ext0=ro.add_external_resource(res_type=rese_res_type, input_url=rese_file_url, title=rese_title, description=rese_description, folder='output')

## biblio
rese_res_type="Bibliographic Resource"

if len(metadata_contribution['inputs']) > 0:
    for i in metadata_contribution['references']:
        rese_file_url=metadata_contribution['references'][i]['url']
        rese_title=metadata_contribution['references'][i]['name']
        rese_description = f"Related publication of the {metadata_contribution['topic']} presented in the Jupyter notebook"
        my_res_ext0 = ro.add_external_resource(res_type=rese_res_type, input_url=rese_file_url, title=rese_title,
                                               description=rese_description, folder='biblio')

# license
MIT_index = rohub.list_available_licenses().index("MIT")
ro.set_license(license_id=rohub.list_available_licenses()[MIT_index])