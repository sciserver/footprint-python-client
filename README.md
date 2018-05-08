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
request = footprint.RegionRequest() # RegionRequest | null
keep_original = 'keep_original_example' # str | null (optional)

try:
    # Generate the convex hull of the regions.
    api_response = api_instance.c_hull_regions(region_name, request, keep_original=keep_original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->c_hull_regions: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost/dobos/footprint-v2.0/Api/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*EditorApi* | [**c_hull_regions**](docs/EditorApi.md#c_hull_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/chull | Generate the convex hull of the regions.
*EditorApi* | [**copy_region**](docs/EditorApi.md#copy_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/copy | Copy a region.
*EditorApi* | [**create_region**](docs/EditorApi.md#create_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName} | Create a new region.
*EditorApi* | [**delete_footprint**](docs/EditorApi.md#delete_footprint) | **DELETE** V1/Editor.svc/footprint | Delete footprint and reset the editor.
*EditorApi* | [**delete_region**](docs/EditorApi.md#delete_region) | **DELETE** V1/Editor.svc/footprint/regions/{regionName} | Delete a region.
*EditorApi* | [**download_footprint**](docs/EditorApi.md#download_footprint) | **GET** V1/Editor.svc/footprint/raw | Returns the footprint in raw format text or binary.
*EditorApi* | [**download_footprint_outline**](docs/EditorApi.md#download_footprint_outline) | **GET** V1/Editor.svc/footprint/outline/raw | Returns the outline of the footprint.
*EditorApi* | [**download_region**](docs/EditorApi.md#download_region) | **GET** V1/Editor.svc/footprint/regions/{regionName}/raw | Returns the shape description of the footprint region.
*EditorApi* | [**download_region_outline**](docs/EditorApi.md#download_region_outline) | **GET** V1/Editor.svc/footprint/regions/{regionName}/outline/raw | Returns the outline of the footprint.
*EditorApi* | [**get_footprint**](docs/EditorApi.md#get_footprint) | **GET** V1/Editor.svc/footprint | Returns the header information of the edited footprint
*EditorApi* | [**get_footprint_outline_points**](docs/EditorApi.md#get_footprint_outline_points) | **GET** V1/Editor.svc/footprint/outline/points | Returns the points of the outline of the footprint.
*EditorApi* | [**get_region**](docs/EditorApi.md#get_region) | **GET** V1/Editor.svc/footprint/regions/{regionName} | Returns the header information of a region.
*EditorApi* | [**get_region_outline_points**](docs/EditorApi.md#get_region_outline_points) | **GET** V1/Editor.svc/footprint/regions/{regionName}/outline/points | Returns the points of the outline of the region.
*EditorApi* | [**grow_region**](docs/EditorApi.md#grow_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/grow | Grow region.
*EditorApi* | [**intersect_regions**](docs/EditorApi.md#intersect_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/intersect | Compute the intersection of regions.
*EditorApi* | [**list_regions**](docs/EditorApi.md#list_regions) | **GET** V1/Editor.svc/footprint/regions | List regions.
*EditorApi* | [**modify_footprint**](docs/EditorApi.md#modify_footprint) | **PATCH** V1/Editor.svc/footprint | Modified the properties of the footprint in the editor.
*EditorApi* | [**modify_region**](docs/EditorApi.md#modify_region) | **PATCH** V1/Editor.svc/footprint/regions/{regionName} | Modify a region.
*EditorApi* | [**move_region**](docs/EditorApi.md#move_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/move | Move a region.
*EditorApi* | [**plot_footprint**](docs/EditorApi.md#plot_footprint) | **GET** V1/Editor.svc/footprint/plot | Plots the footprint
*EditorApi* | [**plot_footprint_advanced**](docs/EditorApi.md#plot_footprint_advanced) | **POST** V1/Editor.svc/footprint/plot | Plots the footprint, with advanced parameters
*EditorApi* | [**plot_region**](docs/EditorApi.md#plot_region) | **GET** V1/Editor.svc/footprint/regions/{regionName}/plot | Plots the region
*EditorApi* | [**plot_region_advanced**](docs/EditorApi.md#plot_region_advanced) | **POST** V1/Editor.svc/footprint/regions/{regionName}/plot | Plots the footprint, with advanced parameters
*EditorApi* | [**subtract_regions**](docs/EditorApi.md#subtract_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/subtract | Compute the difference of regions.
*EditorApi* | [**union_regions**](docs/EditorApi.md#union_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/union | Compute the union of regions.
*EditorApi* | [**upload_region**](docs/EditorApi.md#upload_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/raw | Upload a region binary or other representation


## Documentation For Models

 - [Angle](docs/Angle.md)
 - [CHull](docs/CHull.md)
 - [Circle](docs/Circle.md)
 - [ColorTheme](docs/ColorTheme.md)
 - [CombinationMethod](docs/CombinationMethod.md)
 - [CoordinateRepresentation](docs/CoordinateRepresentation.md)
 - [CoordinateSystem](docs/CoordinateSystem.md)
 - [DegreeStyle](docs/DegreeStyle.md)
 - [Footprint](docs/Footprint.md)
 - [FootprintRequest](docs/FootprintRequest.md)
 - [FootprintResponse](docs/FootprintResponse.md)
 - [Links](docs/Links.md)
 - [OutlineReduction](docs/OutlineReduction.md)
 - [Point](docs/Point.md)
 - [Poly](docs/Poly.md)
 - [Projection](docs/Projection.md)
 - [Rect](docs/Rect.md)
 - [Region](docs/Region.md)
 - [RegionListResponse](docs/RegionListResponse.md)
 - [RegionRequest](docs/RegionRequest.md)
 - [RegionResponse](docs/RegionResponse.md)
 - [RestError](docs/RestError.md)
 - [Rotation](docs/Rotation.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



