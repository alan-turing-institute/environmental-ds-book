import rohub
import os
import sys
sys.path.insert(0, os.path.join(os.getcwd(), 'misc', 'rohub'))
import config

# RoHub functionalities
## list available licenses
rohub.list_available_licenses()

# login
rohub.login(username=config.username, password=config.password)

# list ros
myros= rohub.list_my_ros()

# retrieve first RO
ro_id=myros.loc[0,"identifier"]

# delete RO
ro_id_to_delete=ro_id
rohub.ros_delete(identifier=ro_id_to_delete)

# show possible values for RO types, Resources types, templates, etc.
rohub.list_valid_research_areas()