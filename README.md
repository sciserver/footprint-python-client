# footprint
No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: null
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import footprint 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import footprint
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null
operation = 'operation_example' # str | null (optional)
keep_original = true # bool | null (optional)

try:
    # Compute union, intersection or difference of regions.
    api_response = api_instance.combine_footprint_regions(region_name, operation=operation, keep_original=keep_original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->combine_footprint_regions: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/dobos/footprint-v2.0/Api/V1/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EditorApi* | [**combine_footprint_regions**](docs/EditorApi.md#combine_footprint_regions) | **POST** /footprint/regions/{regionName}?op&#x3D;{operation}&amp;keepOrig&#x3D;{keepOriginal} | Compute union, intersection or difference of regions.
*EditorApi* | [**create_footprint_region**](docs/EditorApi.md#create_footprint_region) | **POST** /footprint/regions/{regionName} | Create new region.
*EditorApi* | [**delete_footprint**](docs/EditorApi.md#delete_footprint) | **DELETE** /footprint | Delete footprint and reset the editor.
*EditorApi* | [**delete_footprint_region**](docs/EditorApi.md#delete_footprint_region) | **DELETE** /footprint/regions/{regionName} | Delete a region.
*EditorApi* | [**delete_footprint_regions**](docs/EditorApi.md#delete_footprint_regions) | **DELETE** /footprint/regions | Deletes multiple regions.
*EditorApi* | [**get_footprint**](docs/EditorApi.md#get_footprint) | **GET** /footprint | Returns the header information of the edited footprint
*EditorApi* | [**get_footprint_outline**](docs/EditorApi.md#get_footprint_outline) | **GET** /footprint/outline | Returns the outline of the footprint.
*EditorApi* | [**get_footprint_outline_points**](docs/EditorApi.md#get_footprint_outline_points) | **GET** /footprint/outline/points?res&#x3D;{resolution} | Returns the points of the outline of the footprint.
*EditorApi* | [**get_footprint_region**](docs/EditorApi.md#get_footprint_region) | **GET** /footprint/regions/{regionName} | Returns the header information of a region.
*EditorApi* | [**get_footprint_region_outline**](docs/EditorApi.md#get_footprint_region_outline) | **GET** /footprint/regions/{regionName}/outline | Returns the outline of the footprint.
*EditorApi* | [**get_footprint_region_outline_points**](docs/EditorApi.md#get_footprint_region_outline_points) | **GET** /footprint/regions/{regionName}/outline/points?res&#x3D;{resolution} | Returns the points of the outline of the footprint.
*EditorApi* | [**get_footprint_region_shape**](docs/EditorApi.md#get_footprint_region_shape) | **GET** /footprint/regions/{regionName}/shape | Returns the shape description of the footprint region.
*EditorApi* | [**get_footprint_region_thumbnail**](docs/EditorApi.md#get_footprint_region_thumbnail) | **GET** /footprint/regions/{regionName}/thumbnail | Gets the thumbnail of a footprint region.
*EditorApi* | [**get_footprint_shape**](docs/EditorApi.md#get_footprint_shape) | **GET** /footprint/shape | Returns the shape description of the footprint.
*EditorApi* | [**get_footprint_thumbnail**](docs/EditorApi.md#get_footprint_thumbnail) | **GET** /footprint/thumbnail | Gets the thumbnail of the footprint.
*EditorApi* | [**list_footprint_regions**](docs/EditorApi.md#list_footprint_regions) | **GET** /footprint/regions | List all regions.
*EditorApi* | [**modify_footprint_region**](docs/EditorApi.md#modify_footprint_region) | **PUT** /footprint/regions/{regionName} | Modify a region.
*EditorApi* | [**plot_footprint**](docs/EditorApi.md#plot_footprint) | **GET** /footprint/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle}&amp;highlights&#x3D;{highlights} | Plots the footprint
*EditorApi* | [**plot_footprint_advanced**](docs/EditorApi.md#plot_footprint_advanced) | **POST** /footprint/plot | Plots the footprint, with advanced parameters
*EditorApi* | [**plot_footprint_region**](docs/EditorApi.md#plot_footprint_region) | **GET** /footprint/regions/{regionName}/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle} | Plots a footprint region.
*EditorApi* | [**plot_footprint_region_advanced**](docs/EditorApi.md#plot_footprint_region_advanced) | **POST** /footprint/regions/{regionName}/plot | Plots a footprint region.
*EditorApi* | [**set_footprint_region_shape**](docs/EditorApi.md#set_footprint_region_shape) | **POST** /footprint/regions/{regionName}/shape | Upload a region shape binary or other representation
*FootprintApi* | [**copy_user_footprint**](docs/FootprintApi.md#copy_user_footprint) | **POST** /users/{owner}/footprints/{name}?op&#x3D;copy | Copy from and existing footprint.
*FootprintApi* | [**create_user_footprint**](docs/FootprintApi.md#create_user_footprint) | **POST** /users/{owner}/footprints/{name} | Create new footprint.
*FootprintApi* | [**create_user_footprint_region**](docs/FootprintApi.md#create_user_footprint_region) | **POST** /users/{owner}/footprints/{name}/regions/{regionName} | Create new region under an existing footprint.
*FootprintApi* | [**delete_user_footprint**](docs/FootprintApi.md#delete_user_footprint) | **DELETE** /users/{owner}/footprints/{name} | Delete footprint.
*FootprintApi* | [**delete_user_footprint_region**](docs/FootprintApi.md#delete_user_footprint_region) | **DELETE** /users/{owner}/footprints/{name}/regions/{regionName} | Delete a region under an existing footprint.
*FootprintApi* | [**find_footprints**](docs/FootprintApi.md#find_footprints) | **GET** /footprints?owner&#x3D;{owner}&amp;name&#x3D;{name}&amp;from&#x3D;{from}&amp;max&#x3D;{max} | Returns the list of footprints of the user.
*FootprintApi* | [**find_user_footprint_regions**](docs/FootprintApi.md#find_user_footprint_regions) | **GET** /users/{owner}/footprints/{name}/regions?regionName&#x3D;{regionName}&amp;from&#x3D;{from}&amp;max&#x3D;{max} | Returns the list of the regions of a footprint.
*FootprintApi* | [**find_user_footprints**](docs/FootprintApi.md#find_user_footprints) | **GET** /users/{owner}/footprints?name&#x3D;{name}&amp;from&#x3D;{from}&amp;max&#x3D;{max} | Returns the list of footprints of the user.
*FootprintApi* | [**get_user_footprint**](docs/FootprintApi.md#get_user_footprint) | **GET** /users/{owner}/footprints/{name} | Returns the header information of a footprint.
*FootprintApi* | [**get_user_footprint_outline**](docs/FootprintApi.md#get_user_footprint_outline) | **GET** /users/{owner}/footprints/{name}/outline | Returns the outline a footprint.
*FootprintApi* | [**get_user_footprint_outline_points**](docs/FootprintApi.md#get_user_footprint_outline_points) | **GET** /users/{owner}/footprints/{name}/outline/points?res&#x3D;{resolution} | Returns the points of the outline of a footprint.
*FootprintApi* | [**get_user_footprint_region**](docs/FootprintApi.md#get_user_footprint_region) | **GET** /users/{owner}/footprints/{name}/regions/{regionName} | Returns the header information of a region.
*FootprintApi* | [**get_user_footprint_region_outline**](docs/FootprintApi.md#get_user_footprint_region_outline) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/outline | Returns the outline a footprint.
*FootprintApi* | [**get_user_footprint_region_outline_points**](docs/FootprintApi.md#get_user_footprint_region_outline_points) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/outline/points?res&#x3D;{resolution} | Returns the points of the outline of a footprint.
*FootprintApi* | [**get_user_footprint_region_shape**](docs/FootprintApi.md#get_user_footprint_region_shape) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/shape | Returns the shape description of a footprint.
*FootprintApi* | [**get_user_footprint_region_thumbnail**](docs/FootprintApi.md#get_user_footprint_region_thumbnail) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/thumbnail | Get the thumbnail of a footprint.
*FootprintApi* | [**get_user_footprint_shape**](docs/FootprintApi.md#get_user_footprint_shape) | **GET** /users/{owner}/footprints/{name}/shape | Returns the shape description of a footprint.
*FootprintApi* | [**get_user_footprint_thumbnail**](docs/FootprintApi.md#get_user_footprint_thumbnail) | **GET** /users/{owner}/footprints/{name}/thumbnail | Get the thumbnail of a footprint.
*FootprintApi* | [**modify_user_footprint**](docs/FootprintApi.md#modify_user_footprint) | **PATCH** /users/{owner}/footprints/{name} | Modify existing footprint.
*FootprintApi* | [**modify_user_footprint_region**](docs/FootprintApi.md#modify_user_footprint_region) | **PUT** /users/{owner}/footprints/{name}/regions/{regionName} | Modify a region under an existing footprint.
*FootprintApi* | [**plot_user_footprint**](docs/FootprintApi.md#plot_user_footprint) | **GET** /users/{owner}/footprints/{name}/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle} | Plots a footprint
*FootprintApi* | [**plot_user_footprint_advanced**](docs/FootprintApi.md#plot_user_footprint_advanced) | **POST** /users/{owner}/footprints/{name}/plot | Plots a footprint, with advanced parameters
*FootprintApi* | [**plot_user_footprint_region**](docs/FootprintApi.md#plot_user_footprint_region) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle} | Plots a footprint.
*FootprintApi* | [**plot_user_footprint_region_advanced**](docs/FootprintApi.md#plot_user_footprint_region_advanced) | **POST** /users/{owner}/footprints/{name}/regions/{regionName}/plot | Plots a footprint.
*FootprintApi* | [**set_user_footprint_region_shape**](docs/FootprintApi.md#set_user_footprint_region_shape) | **POST** /users/{owner}/footprints/{name}/regions/{regionName}/shape | Upload region shape binary or other representation


## Documentation For Models

 - [EquatorialPoint](docs/EquatorialPoint.md)
 - [Footprint](docs/Footprint.md)
 - [FootprintListResponse](docs/FootprintListResponse.md)
 - [FootprintRegion](docs/FootprintRegion.md)
 - [FootprintRegionListResponse](docs/FootprintRegionListResponse.md)
 - [FootprintRegionRequest](docs/FootprintRegionRequest.md)
 - [FootprintRegionResponse](docs/FootprintRegionResponse.md)
 - [FootprintRequest](docs/FootprintRequest.md)
 - [FootprintResponse](docs/FootprintResponse.md)
 - [Links](docs/Links.md)
 - [RestError](docs/RestError.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



