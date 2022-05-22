---
tags: environmental-ds, collaboration-cafe
---
*This HackMD is re-used under a CC-BY license from [_The Turing Way_ collaboration cafe template](https://github.com/alan-turing-institute/the-turing-way/blob/master/book/website/community-handbook/templates/template-coworking-collabcafe.md)*

*A **permanent document** exists in the HackMD: [https://hackmd.io/@environmental-ds/collaboration-cafe](https://hackmd.io/@environmental-ds/collaboration-cafe) that is regularly updated with the empty template for next event.*

# _The Environmental Data Science_ ⛰ 🌳 🏙️ ❄️ 🔥 🌊  online Collaboration Cafe 

## 26 April 2022 | TBC

### Thank you for joining the _The Environmental Data Science_'s online Collaboration Cafe ☕ ✨ 🍰! 

We're delighted to have you here 🎉

**When?** 26 April 2022, 14:00 - 16:00 UTC ([see in your time zone](https://arewemeetingyet.com/London/2021-08-24/14:00))

**Next call:** 28 June 2022

**What?** *The Environmental Data Science is a **community aiming to learn and discuss scientific software practises/developments fostered by AI and data science for a better understanding of our Planet Earth and environmental systems**. 
[Collaboration Cafes](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/community/coworking/coworking-collabcafe.md) are **online coworking calls** that engage anyone interested in learning and discussing about relevant themes in AI and data science to environmental studies*.

**Who?** ***Everyone** interested in reproducible, ethical, and inclusive Data Science and research for environmental studies are welcome to join the full or any part of The Environmental Data Science project, community, and/or this call.*

**How?** **Join Zoom Meeting**
https://turing-uk.zoom.us/j/6779579342?pwd=L25scnhXUUNmVjFsc0hRWTAzTVJ1dz09

***All questions, comments, and recommendations are welcome!***

### Useful links

* All about [online Collaboration Cafes](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/book/community/coworking/coworking-collabcafe.md)

### Code of conduct

* [Take a moment to read this](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/CODE_OF_CONDUCT.md)

### Sign up below

**Name + `Ice breaker question` + ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**
*(Remember that this is a public document. You can use a pseudonym if you'd prefer.)*
==*If you are new to HackMD, please see this document for a short guide (right click, open in a new window): [https://hackmd.io/@turingway/hackmd-guide](https://hackmd.io/@turingway/hackmd-guide).*==

* 

### Conversation Starters

*Advertise and promote your event or anything exciting you're working on.* ✨

* 

## Agenda

### Shared clock/timer :timer_clock: 

https://cuckoo.team/environmental-ds

### Schedule

| Duration | Activity |
| ---- | -------- |
| Start | 👋 Welcome, code of conduct review |
| 10 mins | Introductions and personal goal setting |
| 25 mins | 🍅 1st Pomodoro session |
| 5 mins | ☕️ Break |
| 20 mins | 🍅 2nd Pomodoro session |
| 5 mins | ☕️ Break  |
| 20 mins | 🍅 3rd Pomodoro session |
| 5 mins | ☕️ Break |
| 30 mins | Open discussion: celebrations, reflections and future directions |
| 5 mins | 👋 Close |

### Breakout rooms: Topic proposals

*If you have an idea for a topic you'd like to discuss in a breakout room, please add it below and put your name next to it. If you like one of the topics that are already suggested, please add your name next to that one. Teamwork makes the dream work. For more information about breakout rooms see [the description on GitHub](https://github.com/alan-turing-institute/the-turing-way/blob/master/project_management/online-collaboration-cafe.md#breakout-rooms).*

*Topics for breakout / Names*

* 

### Notes and questions

* 
    
### Request for reviews!

* 

### Feedback at the end of the call

* 

----

# Notes from the last call: 

## Archive: 22 Febraury 2021 | Prepare compelling and reproducible notebooks for the EnvDS book

### Sign up below

**Name + Which is your essential clothing accessory for frozen days? + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

* Alejandro + Gloves + :gloves:	
* Pirta + Beanie + :billed_cap:
* Tim + Argyle + :socks:
* Ricardo + Scarf + :scarf: 

### Conversation Starters

* None

### Breakout rooms: Topic proposals

* No breakout rooms, all in the main room

### Notes and questions

* Alejandro went through the key steps to submit a notebook to the EnvDS book:
    * Step 1: Notebook idea
        * Log your notebook idea as a [new issue](https://github.com/alan-turing-institute/environmental-ds-book/issues/new/choose) in the project repo
        * Once the idea is clear e.g purpose, data sources, packages,  and/or you receive a feedback from a collaborator or EnvDS community, you can move to the next step :arrow_down: 
    * Step 2: Preparation
        * Open a terminal in your local/remote machine.
        * Fork the EnvDS repository to your personal github account.
        * Clone the forked repository into your local/remote machine.
        * Go to the folder of the forked repository in your local/remote machine.
        * If the environmental system and/or topic doesn't exist create a folder in the forked repository.
        * Copy the template of your topic from the community chapter, (see [here](https://github.com/alan-turing-institute/environmental-ds-book/tree/master/book/community/templates)).
    * Step 3: Setup
        * Open a terminal in your local/remote machine and change the current directory (path) to the directory of the forked repo.
        * Verify if you have `conda` i.e. type `conda`. If you don't get results after the verification, follow this [guide for installing conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
        * Prepare a conda environment for your notebook. Note the environment should use python version of the EnvDS book (python 3.8) and also install `jupyter` which is the library to edit the notebook. The lines below guide you to launch a `jupyter notebook` session, one of the `jupyter` interfaces to edit notebooks. 
            * conda create -n <environment_name> python=3.8 jupyter
            * follow the instructions to activate your environment
            * check the list of packages in the [environment.yml](https://github.com/alan-turing-institute/environmental-ds-book/blob/master/environment.yml) of the EnvDS book. 
            * install relevant packages from the list using `conda install <package-name>`
            * type `jupyter notebook`
            * If a package relevant for your notebook isn't in the list, you can add a cell to install it before the import libraries section in the notebook. Packages can be installed using `pip -q install <package-name>` where `-q` means to install in silent mode. 
    * Step 4: Edit the the noebook
        * Once you have the environment ready for your notebook, you can modify the sections of the template.
        * (optional) follow the 10 rules of compelling notebooks provided by the EarthCube initiative available in their Notebook Template (section [Data processing and analysis](https://github.com/earthcube/NotebookTemplates/blob/main/EC_05_Template_Notebook_for_EarthCube_Long_Version.ipynb)).
        * Once happy with the first editions of the notebook. Save it and push the changes. Not sure how to push changes, follow [Turing Way community chapter in Github](https://the-turing-way.netlify.app/collaboration/github-novice.html).
    * Step 5: Open a pull request
        * Go to the forked github repository in your Github account. 
        * Click in contribute and open a pull request
            * ![](https://i.imgur.com/Fq8c0vR.png)
        * You'll see a form which you should fill and submit according to the information requested. 
        * Go to the EnvDS main repo and you'll see the PR as below:
            * ![](https://i.imgur.com/r9BekKL.png)
    * Step 6: Editions
        * Click in your pull request
            * To facilitate the interaction with the reviewer, we are using ReviewNB and Netlify previews. You can access to ReviewNB clicking in the purple buttom below:
            * ![](https://i.imgur.com/G5vEhDT.png)
        * Note you can continue implementing changes in the forked repo. They'll automatically will change the notebook in the PR. 
    * Step 6: Review
        * Once you're happy with the first version in the pull request, you can change to Ready to review in the checkbox.
        * A reviewer will be assigned to your pull request.
        * The reviewer will start a discussion of your notebook through the ReviewNB platform.
    * Step 7: Publication
        * Once both parties, author(s) and reviewer(s) are ha

* Some useful resources mentioned in the meeting:
    * [Turing Way community chapter in Github](https://the-turing-way.netlify.app/collaboration/github-novice.html)
    * Setting a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
    * [Guide for organising community calls](https://the-turing-way.netlify.app/project-design/pd-overview/pd-overview-repro.html?highlight=collaboration)
    * Library for [spectral indices](https://awesome-ee-spectral-indices.readthedocs.io/en/latest/list.html)

* Celebrations :rocket: 
    * Four great notebooks ideas!
        * [name=Alejandro]: COSMOS-UK Sensor Visualisation, see [issue#49](https://github.com/alan-turing-institute/environmental-ds-book/issues/49)
        * [name=Ricardo]: Long timeseries phenology using Landsat data, see [issue#52](https://github.com/alan-turing-institute/environmental-ds-book/issues/52)
        * [name=Tim]: Concatenating a gridded rainfall dataset into a time series, see [issue#53](https://github.com/alan-turing-institute/environmental-ds-book/issues/53)
        * [name=Pirta] Nutrientscape mapping in optically shallow tropical coastal waters, see [issue#54](https://github.com/alan-turing-institute/environmental-ds-book/issues/54)
    
### Request for reviews!

* None

### Feedback at the end of the call

* None


## Archive: 23 November 2021 | FAIR data in Environmental Sciences

![Illustration of the FAIR principles to show the definition of being Findable, Accessible, Interoperable and Reusable. Source: [The Turing Way: The FAIR Principles](https://the-turing-way.netlify.app/reproducible-research/rdm/rdm-fair.html?highlight=fair)](https://i.imgur.com/f27a9aX.jpg)
*_The Turing Way_ project illustration by Scriberia. Used under a CC-BY 4.0 licence. DOI: [10.5281/zenodo.3332807](https://doi.org/10.5281/zenodo.3332807).*

### Sign up below

**Name + What is your recent favorite resource or tool or app or software? + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

* Alejandro + _The Turing Way_ + :milky_way: 
* Bea + _scivision_ + :koala: 

### Conversation Starters

* None

### Breakout rooms: Topic proposals

* Main room (silent mode)
    * Bea: working on the submission of her PhD thesis.
    * Alejandro: 
        * adding helpful resources about FAIR and example of research repositories for Environmental Sciences.
        * checking which sample data within the Environmental Data Science book can be curated in [the Environmental Data Science Zenodo community](https://zenodo.org/communities/the-environmental-ds-community/?page=1&size=20).

### Notes and questions

* Alejandro
    * Useful resources about FAIR :
        * [FAIR Cookbook](https://fairplus.github.io/the-fair-cookbook/content/home.html): an online resource for the Life Sciences with recipes to make and keep data FAIR.
        * [The Turing Way: The FAIR Principles](https://the-turing-way.netlify.app/reproducible-research/rdm/rdm-fair.html?highlight=fair): light introduction to FAIR principles, pointing to key resources in the topic.
        * [Library Carpentry: FAIR Data and Software](https://librarycarpentry.org/lc-fair-research/aio/index.html): lesson exploring the meaning of FAIR elements. 
    * Research data platforms:
        * General
            * [re3data.org](https://www.re3data.org/): initiative indexing research data platforms by content topic and knowledge domain.
            * [Stats datacite](https://stats.datacite.org/): dashboard mapping the registration of persistent identifiers (DOIs) for research data and other research outputs.
        * Environmental science (list of platforms with the highest number of total DOIs registrations according to Stats datacite):
            * [Global Biodiversity Information Facility](https://www.gbif.org/)
            * [FAO Global Information System of the International Treaty on Plant Genetic Resources for Food and Agriculture (PGRFA)](https://ssl.fao.org/glis/)
            * [PANGAEA](https://www.pangaea.de/): earth system research.
            * [Environmental Data Initiative (EDI)](https://portal.edirepository.org/nis/home.jsp): platform suited to curate environmental data, includes code snippets to import the data across multiple programming languages (python, R).
            
    * Other interesting FAIR-driven platforms:
        * [ROHub](https://reliance.rohub.org/): research object management platform supporting the preservation and lifecycle management of scientific investigations, research campaigns and operational processes. It implements FAIR digital objects and specific metadata for data-cube in Earth Science. 

    * Challenges of FAIR data repositories for Environmental sciences (ES):
        * ES is structured as tabular data collected in the field or laboratory (see further discussion in [BEXIS2](https://bdj.pensoft.net/article/72901/)).
        * FAIR-enabled data available could be daunting for many ES researchers and organisations due to the lack of awareness, efficient data management tools, infrastructure and skills [see further discussion in BEXIS2](https://bdj.pensoft.net/article/72901/)).
        * Spatio-temporal (data cubes) > this seems to be adressed by novel research object management platforms such as [ROHub](https://reliance.rohub.org/).
    
### Request for reviews!

* None

### Feedback at the end of the call

* Alejandro: Few participants in this particular collaboration cafe. We should restructure the promotion strategy, proposing new topics and/or changing the format for coming collaborations cafes in 2022 :face_with_monocle:. 

## Archive: 26 October 2021 - Reproducibility in Environmental Science

### Sign up below

**Name + Share a song that expresses your personality + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

* Alejandro + Should stay or Should I go (The Clash) + 🧳
* Sam + Wish you were here (Pink Floyd) 
* Matt - BBC Grandstand Theme - :horse_racing:

### Conversation Starters

* EGU22 session was accepted, [Bridging the spatial scales, from surface sensors to satellite sensors: Innovative approaches towards the construction of Earth’s digital twin](https://meetingorganizer.copernicus.org/EGU22/session/43565). Deadlines:
    * Abstract submission deadline: 12 January 2022, 13:00 CET
    * Travel Support application deadline: 1 December 2021

### Breakout rooms: Topic proposals

* Matt, making a reproducible GitHub code for his MRes dissertation
* Alejandro, preparing contributions guidelines for the Environmentel AI book 
* Sam J, exploration of resources for reproducibility and feedback on Matt and Alejandro's topics

### Notes and questions

* Sam J:
    *  [The Turing Way](https://the-turing-way.netlify.app/welcome), a great resource to guide Environmental scientist in reproducible research.
    *  [Cornell Dataset Description](https://cornell.app.box.com/v/ReadmeTemplate) a good starting template for dataset documentation!
    *  Standards in data catalogues, e.g. [STAC](https://stacspec.org) (but it isn't mature)
* Alejandro:
    * Zenodo:
        * It is great to keep your sample data (up to 50 GB).
    * notebooksharing.space
        * A nice resource to share notebooks with interactive plotting (up to 10Mb). However, it doesn't allow track changes as [ReviewNB](https://www.reviewnb.com) does. 
    * Contributors guidelines for the EnvAI book
        * Sam suggests example environmental python packages with links to notebooks (e.g. hvplot, geopandas etc.)
        * Minimal publishable version guidelines e.g. Binder
        * Use external links for general versioning principles e.g. how to pull request in Github
        * Provide examples how to create lock environments 
        * Section of tools for sharing notebooks e.g. ReviewNB, notebooksharing.space
* Matt
    * Publishing reproducible code for environmental science
        * It can be more important that the process can be reproduced rather than accuracies to the nearest 0.01%
        * Use a subset of data to demonstrate the tool where the owners aren't happy to share the whole thing - training & inference
        * In env science a visual demonstration of the results can be more useful than a commandline readout of accuracy
        * Suggest sensible ranges for hyperparameters in the documentation

### Request for reviews!

* **Sam J**: reviewers need for SEVIRI wildfire data notebook of the EnvAI book, see [PR#12](https://github.com/acocac/environmental-ai-book/pull/12)

### Feedback at the end of the call

* None

## Archive: 28 September - Data preprocessing

**Name + What’s the hardest part about working virtually for you? and the easiest? + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

* Alejandro + social interaction, more sleep time + :busts_in_silhouette:	 :sleeping: 
* Sam A. + I still have just as many meetings if not more and it is soooo tiring! :sleeping: :pleading_face:
* Evangeline + Feeling self-conscious on camera, flexibility + :movie_camera: :clock1: 

### Conversation Starters

* Met Office / Joint centre for excellence in environmental intelligence conference 16/17 Dec 2021!
* We have a fresh interactive notebook in the Environmental Data S Book :earth_asia::books: The notebook focuses on detecting tree crowns using the *DeepForest* model :deciduous_tree:. Have a look at the rendered version [here](https://acocac.github.io/environmental-ai-book/forest/modelling/forest-modelling-treecrown_deepforest.html). Other recent community contributions are the exploration of sensor data, [Met Office UKV high-resolution atmosphere model data for urban settings](https://acocac.github.io/environmental-ai-book/urban/sensors/urban-sensors-ukv.html) and [MODIS satellite imagery and wildfire data](https://acocac.github.io/environmental-ai-book/wildfires/sensors/wildfires-sensors-modis.html).

### Breakout rooms: Topic proposals

* Sam A. Manufacture Urban Data in GIS format
* Evie. Preprocessing satellite data for crop yield prediction
* Alejandro. Preprocess FluxNet data and related gridded products

### Notes and questions

* We showcased the [SEPAL platform](https://docs.sepal.io/en/latest/cookbook/area_estimation.html) for Vegetation Satellite Image analysis. 
* Discussed challenges around scoping and extracting satellite data for machine learning models of vegetation (agricultural crops):
    * Appropriate satellite platform (Sentinel/LANDSAT?)
    * Preprocessing of radar and optical data (i.e. dealing with cloud cover)
    * Appropriate time series/critical dates for plant growth
* Sam A. used ArcGIS pro to extract site-specific temperature information from a gridded netCDF dataset using the Spatial Analyst 'Sample' tool. It is very useful in that it works across the time dimension so I could do this for 1 year of data in one go. It is also possible to set a desired output coordinate system. I could save the data out as a csv file and then use standard python tools like pandas and numpy for further processing  
* Sam A. suggests using [Iris package](https://scitools-iris.readthedocs.io/en/latest/) for reprojecting gridded netCDF files. The project is
* Data preprocessing is still too time-consuming, and there is lack of communication of the tools available. 

### Request for reviews!

* None

### Feedback at the end of the call

* None

## Archive: 29 June - Data Visualization

**Name + Something you watch (video, movie, documentary. etc) recently that was inspiring for you? + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

* Alejandro + [Black Holes: The Edge of All We Know](https://www.rottentomatoes.com/m/black_holes_the_edge_of_all_we_know) + :milky_way:	 
* Scott + [Coded Bias](https://www.imdb.com/title/tt11394170/) + 🧠
* Tom Andersson + [The Dig (Netflix film on Sutton Hoo dig site)](https://www.wikiwand.com/en/Sutton_Hoo) + :spades: 
* Emily + actual paint drying on my bedroom wall + :lower_left_paintbrush: 
* Sam Jackson + [Calibre](https://en.wikipedia.org/wiki/Calibre_(film))  + :smile:

### Conversation Starters

* Alejandro: EGU Public call-for-session-proposals all other sessions: Deadline: [6 September 2021](https://www.egu22.eu/)
* Scott: Pangeo European Community is growing and there are plans of coffee chats and regular showcase meetings (see [here](https://cnrs.zoom.us/j/95432814658))

### Breakout rooms: Topic proposals

* Sam J: Regridding MODIS data for wildfires detection
* Tom: Produce script to reproduce IceNet paper figures for *Nature Communications*
* Emily: Visualization of LiDAR data
* Scott: Organizing and Admin EnvSensors WPs project timetable
* Alejandro: Deploying a FluxNet use case visualization outputs for the Environmental Data Science book

### Notes and questions

* Emily showed a cool visualization of a laser scan image (100 GB) using the propietary software of the scanner device. After data preprocessing, she will use  libraries for visualizing individual trees. 
    * Emily says there are also some radar sensors that collect soil data. 
* Tools for regridding MODIS data. Sam is using [*satpy*](https://satpy.readthedocs.io/en/stable/overview.html). Suggestions of other existing tools are welcome. 
* Tom is making his code nicer i.e. modules and efficient i.e using dask. 
* Alejandro shows FluxNet demo
    * Emily suggest adding woodlands and shrubs to subset FluxNet data. 

### Feedback at the end of the call
* Add a disclaimer collaboration cafes' hackMDs are public.
* Names for breakout rooms.
* We should aim to keep to time, once we are used to the format etc.