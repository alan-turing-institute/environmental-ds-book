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
    'environment': 'polar',
    'topic': 'modelling',
    'reponame': '67a1e320-7c47-4ea9-8df8-e868326bc90b',
    'title': "Sea ice forecasting using the IceNet library",
    'inputs': {'input1':{'name':'Codebase of the IceNet library',
                         'url':'https://github.com/icenet-ai/icenet/'},
               },
    'outputs': {'content': 'results',
               'url': "https://doi.org/10.5281/zenodo.12612126"},
    'author_GHuser': 'eds-book-gallery',
    'references':{'ref1':{'name':'Seasonal Arctic sea ice forecasting with probabilistic deep learning',
                          'url':"https://doi.org/10.1038/s41467-021-25257-4"}},
    'sketch': {'title':'Image showing an example of the forecasted sea ice',
               'path':'_temp/rohub/67a1e320-7c47-4ea9-8df8-e868326bc90b/plot.png'}
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
         "display_name": "Bryn Noel Ubald",
         "name": "Bryn Noel Ubald",
         "email": "bryald@bas.ac.uk",
         "orcid_id": "0000-0002-0206-7140",
         "affiliation": "British Antarctic Survey"},
        {"agent_type": "user",
         "display_name": "James Byrne",
         "name": "James Byrne",
         "email": "jambyr@bas.ac.uk",
         "orcid_id": "0000-0003-3731-2377",
         "affiliation": "British Antarctic Survey"},
        ]

ro.set_authors(agents=authors)

reviewers=[
    {"agent_type": "user",
     "display_name": "Wei Ji",
     "name": "Wei Ji",
     "email": "weiji@developmentseed.org",
     "orcid_id": "0000-0003-2354-1988",
     "affiliation": "Development Seed"},
    {"agent_type": "user",
     "display_name": "William Gregory",
     "name": "William Gregory",
     "email": "wg4031@princeton.edu",
     "orcid_id": "0000-0001-8176-1642",
     "affiliation": "Princeton University"},
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