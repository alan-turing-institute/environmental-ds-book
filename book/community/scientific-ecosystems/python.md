(cm-scientific-ecosystems-python)=

# Python

## Pangeo
Pangeo describes itself as "A Community Platform for Big Data Geoscience".
The Pangeo Software Stack is a loose collection of open source software consisting of Core Packages that are fundamental to Geoscience data anaylsis. 

### Communication
| Information | Links                                                                                                                                                                                              |
|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Website** | [![Website](https://img.shields.io/badge/Website-blue.svg)](https://pangeo.io/)                                                                                                                    |
| **GitHub**  | [![Discourse](https://img.shields.io/badge/GitHub-visit_organisation-yellow?logo=github&logoColor=whitesmoke)](https://github.com/pangeo-data)                                                     |
| **Discuss** | [![Organisation](https://img.shields.io/discourse/https/discourse.pangeo.io/status.svg?colorB=%234CB697&label=Discourse&logo=discourse)](https://discourse.pangeo.io/)                             |
| **Chat**    | [![Join Slack](https://img.shields.io/badge/gitter-join_chat-red?logo=Gitter&style=flat-round&label=gitter)](https://gitter.im/pangeo-data/Lobby)                                                  | 

### Packages

#### Core

| Package                                           | Description                                                                       | Repository Health                                                                                                                                                                                                                                                                                                      |
|:--------------------------------------------------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[Intake](https://github.com/intake/intake)**    | A lightweight package for finding, investigating, loading and disseminating data. | ![starts](https://img.shields.io/github/stars/intake/intake?style=social) ![forks](https://img.shields.io/github/forks/intake/intake?style=social) ![last-commit](https://img.shields.io/github/last-commit/intake/intake.svg) ![license](https://img.shields.io/github/license/intake/intake.svg)                     |
| **[Xarray](https://github.com/pydata/xarray)**    | De facto library to access and represent multidimensional data.                   | ![starts](https://img.shields.io/github/stars/pydata/xarray?style=social) ![forks](https://img.shields.io/github/forks/pydata/xarray?style=social) ![last-commit](https://img.shields.io/github/last-commit/pydata/xarray.svg) ![license](https://img.shields.io/github/license/pydata/xarray.svg)                     |
| **[Dask](https://github.com/dask/dask)**          | A flexible library for parallel computing in Python.                              | ![starts](https://img.shields.io/github/stars/dask/dask?style=social) ![forks](https://img.shields.io/github/forks/dask/dask?style=social) ![last-commit](https://img.shields.io/github/last-commit/dask/dask.svg) ![license](https://img.shields.io/github/license/dask/dask.svg)         |

#### Extensions

##### Xarray
| Package                                               | Description                                                                               | Repository Health                                                                                                                                                                                                                                                                                                      |
|:------------------------------------------------------|:------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[rioxarray](https://github.com/corteva/rioxarray)** | A wrapper package to support GeoTIFF & GDAL rasters and add additional spatial functions. | ![starts](https://img.shields.io/github/stars/corteva/rioxarray?style=social) ![forks](https://img.shields.io/github/forks/corteva/rioxarray?style=social) ![last-commit](https://img.shields.io/github/last-commit/corteva/rioxarray.svg) ![license](https://img.shields.io/github/license/corteva/rioxarray.svg)                     |
| **[cfgrib](https://github.com/ecmwf/cfgrib)**         | A wrapper package to support GRIB files.                                                  | ![starts](https://img.shields.io/github/stars/ecmwf/cfgrib?style=social) ![forks](https://img.shields.io/github/forks/ecmwf/cfgrib?style=social) ![last-commit](https://img.shields.io/github/last-commit/ecmwf/cfgrib.svg) ![license](https://img.shields.io/github/license/ecmwf/cfgrib.svg)                     |

## HoloViz
HoloViz ecosystem consists of high-level Python tools that are designed to work together to solve the entire problem of visualization, from conducting exploratory data analysis to deploying complex dashboards.

### Communication
| Information | Links                                                                                                                                                                       |
|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Website** | [![Website](https://img.shields.io/badge/Website-blue.svg)](https://holoviz.org/)                                                                                           |
| **GitHub**  | [![Discourse](https://img.shields.io/badge/GitHub-visit_organisation-yellow?logo=github&logoColor=whitesmoke)](https://github.com/holoviz/holoviz)                          |
| **Discuss** | [![Organisation](https://img.shields.io/discourse/https/discourse.holoviz.org/status.svg?colorB=%234CB697&label=Discourse&logo=discourse)](https://discourse.holoviz.org//) |
| **Chat**    | [![Join Slack](https://img.shields.io/badge/gitter-join_chat-red?logo=Gitter&style=flat-round&label=gitter)](https://gitter.im/pyviz/pyviz)                                 | 

### Packages

#### Core

| Package                                               | Description                                                            | Repository Health                                                                                                                                                                                                                                                                                                                |
|:------------------------------------------------------|:-----------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **[Panel](https://github.com/holoviz/panel)**         | Create interactive dashboards in Jupyter notebooks or standalone apps. | ![starts](https://img.shields.io/github/stars/holoviz/panel?style=social) ![forks](https://img.shields.io/github/forks/holoviz/panel?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/panel.svg) ![license](https://img.shields.io/github/license/holoviz/panel.svg)                               |
| **[hvPlot](https://github.com/holoviz/hvplot)**       | Quickly and interactively explore data with a familiar API.            | ![starts](https://img.shields.io/github/stars/holoviz/hvplot?style=social) ![forks](https://img.shields.io/github/forks/holoviz/hvplot?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/hvplot.svg) ![license](https://img.shields.io/github/license/holoviz/hvplot.svg)                           |
| **[HoloViews](https://github.com/holoviz/holoviews)** | Visualize while you analyze by declaring data properties.              | ![starts](https://img.shields.io/github/stars/holoviz/holoviews?style=social) ![forks](https://img.shields.io/github/forks/holoviz/holoviews?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/holoviews.svg) ![license](https://img.shields.io/github/license/holoviz/holoviews.svg)               |
| **[GeoViews](https://github.com/holoviz/geoviews)**   | Extend HoloViews for geographic data.                                  | ![starts](https://img.shields.io/github/stars/holoviz/geoviews?style=social) ![forks](https://img.shields.io/github/forks/holoviz/geoviews?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/geoviews.svg) ![license](https://img.shields.io/github/license/holoviz/geoviews.svg)                   |
| **[GeoViews](https://github.com/holoviz/datashader)** | Render big data images in a browser.                                   | ![starts](https://img.shields.io/github/stars/holoviz/datashader?style=social) ![forks](https://img.shields.io/github/forks/holoviz/datashader?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/datashader.svg) ![license](https://img.shields.io/github/license/holoviz/datashader.svg)           | 
| **[Lumen](https://github.com/holoviz/lumen)**         | Construct no-code dashboards from simple YAML specifications.          | ![starts](https://img.shields.io/github/stars/holoviz/lumen?style=social) ![forks](https://img.shields.io/github/forks/holoviz/lumen?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/lumen.svg) ![license](https://img.shields.io/github/license/holoviz/lumen.svg)                               |
| **[Colorcet](https://github.com/holoviz/colorcet)**   | Plot with perceptually based colormaps.                                | ![starts](https://img.shields.io/github/stars/holoviz/colorcet?style=social) ![forks](https://img.shields.io/github/forks/holoviz/colorcet?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/colorcet.svg) ![license](https://img.shields.io/github/license/holoviz/colorcet.svg)                   |
| **[Param](https://github.com/holoviz/param)**         | Declaratively code in Python.                                          | ![starts](https://img.shields.io/github/stars/holoviz/param?style=social) ![forks](https://img.shields.io/github/forks/holoviz/param?style=social) ![last-commit](https://img.shields.io/github/last-commit/holoviz/param.svg) ![license](https://img.shields.io/github/license/holoviz/param.svg)                               |
