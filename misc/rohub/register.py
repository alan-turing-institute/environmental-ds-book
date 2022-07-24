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
    'environment': 'general',
    'topic': 'exploration',
    'filename': 'general-preprocessing-rainfall_noaa',
    'title': 'Concatenating a gridded rainfall reanalysis dataset into a time series',
    'inputs': {'input1':{'name':"Inputs of the Jupyter Notebook - Concatenating a gridded rainfall reanalysis dataset into a time series",
                         'url':"https://downloads.psl.noaa.gov/Datasets/ncep.reanalysis.derived/surface_gauss/prate.sfc.mon.mean.nc"},
               },
    'outputs': {'content': 'figures',
               'url': "https://doi.org/10.5281/zenodo.6824189"},
    'author_GHuser': 'Environmental-DS-Book',
    'references':{'ref1':{'name':'The NMC/NCAR 40-year reanalysis project','url':"http://doi.org/10.1175/1520-0477(1996)077%3C0437:TNYRP%3E2.0.CO;2"},
                  'ref1':{'name':'Quantifying Causal Pathways of Teleconnections','url':"https://doi.org/10.1175/BAMS-D-20-0117.1"}},
    'sketch': {'title':'Image showing interactive plot of global monthly precipitation mean computed from NCEP/NCAR reanalysis dataset',
               'path':'_temp/rohub/general-preprocessing-rainfall_noaa/interactive_plotting.png'}
}

title_nb = metadata_contribution['title']

metadata_rohub = {
    'title': f'{title_nb} (Jupyter Notebook) published in the Environmental Data Science book',
    'research_areas': ['Environmental research', 'Climatology'],
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
        {"user_id": "https://github.com/timo0thy",
         "display_name": "Timothy Lam",
         "name": "Timothy Lam",
         "email": "tlam@turing.ac.uk",
         "affiliation": "University of Exeter"},
        {"user_id": "https://github.com/MarleneKretschmer",
         "display_name": "Marlene Kretschmer",
         "name": "Marlene Kretschmer",
         "email": "m.j.a.kretschmer@reading.ac.uk",
         "affiliation": "University of Reading"},
        {"user_id": "https://github.com/svadams",
         "display_name": "Samantha Adams",
         "name": "Samantha Adams",
         "email": "samantha.adams@metoffice.gov.uk",
         "affiliation": "Met Office Informatics Lab"},
        {"user_id": "https://github.com/RPrudden",
         "display_name": "Rachel Prudden",
         "name": "Rachel Prudden",
         "email": "rachel.prudden@informaticslab.co.uk",
         "affiliation": "Met Office Informatics Lab"},
        {"user_id": "https://github.com/ESaggioro",
         "display_name": "Elena Saggioro",
         "name": "Elena Saggioro",
         "email": "e.saggioro@pgr.reading.ac.uk",
         "affiliation": "University of Reading"},
        ]

ro.set_authors(agents=authors)

reviewers=[
    {"user_id": "https://github.com/NHomer-Edi",
     "display_name": "Nick Homer",
     "name": "Nick Homer",
     "email": "nhomer@turing.ac.uk",
     "affiliation": "University of Edinburgh"},
    {"user_id": "https://github.com/acocac",
     "display_name": "Alejandro Coca-Castro",
     "name": "Alejandro Coca-Castro",
     "affiliation": "The Alan Turing Institute",
     "email": "acoca@turing.ac.uk"
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
rese_file_url=f"https://sgithub.com/{metadata_contribution['author_GHuser']}/{metadata_contribution['filename']}/blob/main/{metadata_contribution['filename']}.ipynb"
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