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
    'reponame': '39d9c177-11da-41b2-9b64-63f4c1c834b3',
    'title': "Variational data assimilation with deep prior (CIRC23)",
    'inputs': {'input1':{'name':'Codebase of the reproduced paper',
                         'url':'https://github.com/ArFiloche/Deepprior4DVar_CI22'},
               },
    'outputs': {'content': 'figures, models and results',
               'url': "https://doi.org/10.5281/zenodo.8338556"},
    'author_GHuser': 'eds-book-gallery',
    'references':{'ref1':{'name':'Deep prior in variational assimilation to estimate an ocean circulation without explicit regularization',
                          'url':"http://doi.org/10.1017/eds.2022.31"}},
    'sketch': {'title':'Image showing an example of the estimated motion fields with various algorithms',
               'path':'_temp/rohub/39d9c177-11da-41b2-9b64-63f4c1c834b3/plot.png'}
}

title_nb = metadata_contribution['title']

metadata_rohub = {
    'title': f'{title_nb} (Jupyter Notebook) published in the Environmental Data Science book',
    'research_areas': ['Environmental research', 'Oceanography', 'Deep learning'],
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
         "display_name": "Mukulika Pahari",
         "name": "Mukulika Pahari",
         "email": "mukulikapahari@gmail.com",
         "orcid_id": None,
         "affiliation": "University of Mumbai"},
        {"agent_type": "user",
         "display_name": "Rutika Bhoir",
         "name": "Rutika Bhoir",
         "email": "rutikabhoir1316@gmail.com",
         "orcid_id": None,
         "affiliation": "University of Mumbai"},
        ]

ro.set_authors(agents=authors)

reviewers=[
    {"agent_type": "user",
     "display_name": "Tina Odaka",
     "name": "Tina Odaka",
     "email": "tina.odaka@ifremer.fr",
     "orcid_id": "0000-0002-1500-0156",
     "affiliation": "Ifremer"},
    {"agent_type": "user",
     "display_name": "Caroline Arnold",
     "name": "Caroline Arnold",
     "email": "arnold@dkrz.de",
     "orcid_id": "0000-0002-9458-1517",
     "affiliation": "German Climate Computing Center"},
    {"agent_type": "user",
     "display_name": "Paolo Pelucchi",
     "name": "Paolo Pelucchi",
     "email": "paolo.pelucchi@uv.es",
     "orcid_id": None,
     "affiliation": "Universitat de València"},
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

## lock files
rese_res_type = "File"

rese_file_url=f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['reponame']}/tree/main/.lock/conda-lock.yml"
rese_title=f"Lock conda file"
rese_description=f"Lock conda file of the Jupyter notebook hosted by the Environmental Data Science Book"
ro.add_external_resource(res_type=rese_res_type, input_url=rese_file_url, title=rese_title, description=rese_description, folder='tool')

## environment.yml
rese_res_type = "File"
rese_file_url = f"https://github.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['reponame']}/tree/main/.binder/environment.yml"
rese_title = f"Conda environment"
rese_description = f"Conda environment when user want to have the same libraries installed without concerns of package versions"
ro.add_external_resource(res_type=rese_res_type, input_url=rese_file_url, title=rese_title, description=rese_description, folder='tool')

## rendered version
rese_res_type="Publication"
rese_file_url=f"https://edsbook.org/notebooks/gallery/{metadata_contribution['reponame']}/notebook.html"
rese_title=f"Online rendered version of the Jupyter notebook"
rese_description="Rendered version of the Jupyter Notebook hosted by the Environmental Data Science Book"

my_res_ext0=ro.add_external_resource(res_type=rese_res_type, input_url=rese_file_url, title=rese_title, description=rese_description, folder='tool')

## license
MIT_index = rohub.list_available_licenses().index("MIT")
ro.set_license(license_id=rohub.list_available_licenses()[MIT_index])