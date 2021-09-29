---
tags: environmental-ai, collaboration-cafe
---
*This HackMD is based on [_The Turing Way_ collaboration cafe template](https://github.com/alan-turing-institute/the-turing-way/blob/master/book/website/community-handbook/templates/template-coworking-collabcafe.md)*

*A **permanent document** exists in the HackMD: [https://hackmd.io/@environmental-ai/collaboration-cafe](https://hackmd.io/@environmental-ai/collaboration-cafe) that is regularly updated with the empty template for next event.*

# _The Environmental AI_ ⛰ 🌳 🏙️ ❄️ 🔥 🌊  online Collaboration Cafe 

## 26 October 2021 | TBC

Thank you for joining the _The Environmental AI_'s online Collaboration Cafe! 

We're delighted to have you here ☕ ✨ 🍰

**When?** 26 October 2021, 14:00 - 16:00 UTC ([see in your time zone](https://arewemeetingyet.com/London/2021-08-24/14:00))

**Next call:** 30 November 2021

**What?** *The Environmental AI is a **community aiming to learn and discuss about good research practices to use existing AI and data science solutions to a better understanding of the planet earth across multiple environmental settings**. 
[Collaboration Cafes](https://the-turing-way.netlify.app/community-handbook/coworking/coworking-collabcafe.html) are **online coworking calls** that engage anyone interested in learning and discussing about relevant themes in AI and data science to environmental studies*.

**Who?** ***Everyone** interested in reproducible, ethical, and inclusive data science and research for environmental studies are welcome to join the full or any part of The Environmental AI project, community, and/or this call.*

**How?** **Join Zoom Meeting**
https://turing-uk.zoom.us/j/6779579342?pwd=L25scnhXUUNmVjFsc0hRWTAzTVJ1dz09

==*The waiting room is enabled. The host of this call will let you in.*==

***All questions, comments, and recommendations are welcome!***

### Code of conduct
* [Take a moment to read this](https://github.com/acocac/environmental-ai-book/blob/acoca-codeofconduct/CODE_OF_CONDUCT.md)

### Useful links
* All about [online Collaboration Cafes](https://github.com/alan-turing-institute/the-turing-way/blob/master/project_management/online-collaboration-cafe.md)

### Sign up below

**Name + Break Ice Question + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

*(Remember that this is a public document. You can use a pseudonym if you'd prefer.)*
==*If you are new to HackMD, please see this document for a short guide (right click, open in a new window): [https://hackmd.io/@turingway/hackmd-guide](https://hackmd.io/@turingway/hackmd-guide).*==

* 
* 

### Conversation Starters

*Advertise and promote your event or anything exciting you're working on.* ✨

* 
* 

## Agenda


### Shared clock/timer

https://cuckoo.team/environmental-ai

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
* 

### Notes and questions

*  
*  

### Request for reviews!

*  
* 

### Feedback at the end of the call

* 
* 

----

# Notes from the last call: 

## Archive: 28 September - Data preprocessing

**Name + What’s the hardest part about working virtually for you? and the easiest? + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

*(Remember that this is a public document. You can use a pseudonym if you'd prefer.)*
==*If you are new to HackMD, please see this document for a short guide (right click, open in a new window): [https://hackmd.io/@turingway/hackmd-guide](https://hackmd.io/@turingway/hackmd-guide).*==

* Alejandro + social interaction, more sleep time + :busts_in_silhouette:	 :sleeping: 
* Sam A. + I still have just as many meetings if not more and it is soooo tiring! :sleeping: :pleading_face:
* Evangeline + Feeling self-conscious on camera, flexibility + :movie_camera: :clock1: 

### Conversation Starters

*Advertise and promote your event or anything exciting you're working on.* ✨

* Met Office / Joint centre for excellence in environmental intelligence conference 16/17 Dec 2021!
* We have a fresh interactive notebook in the Environmental AI Book :earth_asia::books: The notebook focuses on detecting tree crowns using the *DeepForest* model :deciduous_tree:. Have a look at the rendered version [here](https://acocac.github.io/environmental-ai-book/forest/modelling/forest-modelling-treecrown_deepforest.html). Other recent community contributions are the exploration of sensor data, [Met Office UKV high-resolution atmosphere model data for urban settings](https://acocac.github.io/environmental-ai-book/urban/sensors/urban-sensors-ukv.html) and [MODIS satellite imagery and wildfire data](https://acocac.github.io/environmental-ai-book/wildfires/sensors/wildfires-sensors-modis.html).

### Breakout rooms: Topic proposals
*Topics for breakout / Names*

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
* Sam A suggests using [Iris package](https://scitools-iris.readthedocs.io/en/latest/) for reprojecting gridded netCDF files. The project is
* Data preprocessing is still too time-consuming, and there is lack of communication of the tools available. 

### Request for reviews!

* None

### Feedback at the end of the call

* None

## Archive: 29 June - Data Visualization

**Name + Something you watch (video, movie, documentary. etc) recently that was inspiring for you? + an emoji to represent it ([emoji cheatsheet](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md))**

*(Remember that this is a public document. You can use a pseudonym if you'd prefer.)*
==*If you are new to HackMD, please see this document for a short guide (right click, open in a new window): [https://hackmd.io/@turingway/hackmd-guide](https://hackmd.io/@turingway/hackmd-guide).*==

* Alejandro + [Black Holes: The Edge of All We Know](https://www.rottentomatoes.com/m/black_holes_the_edge_of_all_we_know) + :milky_way:	 
* Scott + [Coded Bias](https://www.imdb.com/title/tt11394170/) + 🧠
* Tom Andersson + [The Dig (Netflix film on Sutton Hoo dig site)](https://www.wikiwand.com/en/Sutton_Hoo) + :spades: 
* Emily + actual paint drying on my bedroom wall + :lower_left_paintbrush: 
* Sam Jackson + [Calibre](https://en.wikipedia.org/wiki/Calibre_(film))  + :smile:

### Conversation Starters

*Advertise and promote your event or anything exciting you're working on.* ✨

* Alejandro: EGU Public call-for-session-proposals all other sessions: Deadline: [6 September 2021](https://www.egu22.eu/)
* Scott: Pangeo European Community is growing and there are plans of coffee chats and regular showcase meetings (see [here](https://cnrs.zoom.us/j/95432814658))

### Breakout rooms: Topic proposals

*Topics for breakout / Names*

* Sam J: Regridding MODIS data for wildfires detection
* Tom: Produce script to reproduce IceNet paper figures for *Nature Communications*
* Emily: Visualization of LiDAR data
* Scott: Organizing and Admin EnvSensors WPs project timetable
* Alejandro: Deploying a FluxNet use case visualization outputs for the Environmental AI book

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