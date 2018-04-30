# footprint.EditorApi

All URIs are relative to *http://localhost/dobos/footprint-v2.0/Api/V1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**combine_footprint_regions**](EditorApi.md#combine_footprint_regions) | **POST** /footprint/regions/{regionName}?op&#x3D;{operation}&amp;keepOrig&#x3D;{keepOriginal} | Compute union, intersection or difference of regions.
[**create_footprint_region**](EditorApi.md#create_footprint_region) | **POST** /footprint/regions/{regionName} | Create new region.
[**delete_footprint**](EditorApi.md#delete_footprint) | **DELETE** /footprint | Delete footprint and reset the editor.
[**delete_footprint_region**](EditorApi.md#delete_footprint_region) | **DELETE** /footprint/regions/{regionName} | Delete a region.
[**delete_footprint_regions**](EditorApi.md#delete_footprint_regions) | **DELETE** /footprint/regions | Deletes multiple regions.
[**get_footprint**](EditorApi.md#get_footprint) | **GET** /footprint | Returns the header information of the edited footprint
[**get_footprint_outline**](EditorApi.md#get_footprint_outline) | **GET** /footprint/outline | Returns the outline of the footprint.
[**get_footprint_outline_points**](EditorApi.md#get_footprint_outline_points) | **GET** /footprint/outline/points?res&#x3D;{resolution} | Returns the points of the outline of the footprint.
[**get_footprint_region**](EditorApi.md#get_footprint_region) | **GET** /footprint/regions/{regionName} | Returns the header information of a region.
[**get_footprint_region_outline**](EditorApi.md#get_footprint_region_outline) | **GET** /footprint/regions/{regionName}/outline | Returns the outline of the footprint.
[**get_footprint_region_outline_points**](EditorApi.md#get_footprint_region_outline_points) | **GET** /footprint/regions/{regionName}/outline/points?res&#x3D;{resolution} | Returns the points of the outline of the footprint.
[**get_footprint_region_shape**](EditorApi.md#get_footprint_region_shape) | **GET** /footprint/regions/{regionName}/shape | Returns the shape description of the footprint region.
[**get_footprint_region_thumbnail**](EditorApi.md#get_footprint_region_thumbnail) | **GET** /footprint/regions/{regionName}/thumbnail | Gets the thumbnail of a footprint region.
[**get_footprint_shape**](EditorApi.md#get_footprint_shape) | **GET** /footprint/shape | Returns the shape description of the footprint.
[**get_footprint_thumbnail**](EditorApi.md#get_footprint_thumbnail) | **GET** /footprint/thumbnail | Gets the thumbnail of the footprint.
[**list_footprint_regions**](EditorApi.md#list_footprint_regions) | **GET** /footprint/regions | List all regions.
[**modify_footprint_region**](EditorApi.md#modify_footprint_region) | **PUT** /footprint/regions/{regionName} | Modify a region.
[**plot_footprint**](EditorApi.md#plot_footprint) | **GET** /footprint/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle}&amp;highlights&#x3D;{highlights} | Plots the footprint
[**plot_footprint_advanced**](EditorApi.md#plot_footprint_advanced) | **POST** /footprint/plot | Plots the footprint, with advanced parameters
[**plot_footprint_region**](EditorApi.md#plot_footprint_region) | **GET** /footprint/regions/{regionName}/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle} | Plots a footprint region.
[**plot_footprint_region_advanced**](EditorApi.md#plot_footprint_region_advanced) | **POST** /footprint/regions/{regionName}/plot | Plots a footprint region.
[**set_footprint_region_shape**](EditorApi.md#set_footprint_region_shape) | **POST** /footprint/regions/{regionName}/shape | Upload a region shape binary or other representation


# **combine_footprint_regions**
> DefinitionFootprintRegionResponse combine_footprint_regions(region_name, operation=operation, keep_original=keep_original)

Compute union, intersection or difference of regions.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **operation** | **str**| null | [optional] 
 **keep_original** | **bool**| null | [optional] 

### Return type

[**DefinitionFootprintRegionResponse**](DefinitionFootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_footprint_region**
> DefinitionFootprintRegionResponse create_footprint_region(region_name)

Create new region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Create new region.
    api_response = api_instance.create_footprint_region(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->create_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**DefinitionFootprintRegionResponse**](DefinitionFootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footprint**
> delete_footprint()

Delete footprint and reset the editor.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # Delete footprint and reset the editor.
    api_instance.delete_footprint()
except ApiException as e:
    print("Exception when calling EditorApi->delete_footprint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footprint_region**
> delete_footprint_region(region_name)

Delete a region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Delete a region.
    api_instance.delete_footprint_region(region_name)
except ApiException as e:
    print("Exception when calling EditorApi->delete_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footprint_regions**
> delete_footprint_regions()

Deletes multiple regions.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # Deletes multiple regions.
    api_instance.delete_footprint_regions()
except ApiException as e:
    print("Exception when calling EditorApi->delete_footprint_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint**
> DefinitionFootprintResponse get_footprint()

Returns the header information of the edited footprint

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # Returns the header information of the edited footprint
    api_response = api_instance.get_footprint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DefinitionFootprintResponse**](DefinitionFootprintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_outline**
> file get_footprint_outline()

Returns the outline of the footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # Returns the outline of the footprint.
    api_response = api_instance.get_footprint_outline()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_outline: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_outline_points**
> file get_footprint_outline_points(resolution=resolution)

Returns the points of the outline of the footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
resolution = 1.2 # float | null (optional)

try:
    # Returns the points of the outline of the footprint.
    api_response = api_instance.get_footprint_outline_points(resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_outline_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution** | **float**| null | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region**
> DefinitionFootprintRegionResponse get_footprint_region(region_name)

Returns the header information of a region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Returns the header information of a region.
    api_response = api_instance.get_footprint_region(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**DefinitionFootprintRegionResponse**](DefinitionFootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region_outline**
> file get_footprint_region_outline(region_name)

Returns the outline of the footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Returns the outline of the footprint.
    api_response = api_instance.get_footprint_region_outline(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_region_outline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region_outline_points**
> file get_footprint_region_outline_points(region_name, resolution=resolution)

Returns the points of the outline of the footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null
resolution = 1.2 # float | null (optional)

try:
    # Returns the points of the outline of the footprint.
    api_response = api_instance.get_footprint_region_outline_points(region_name, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_region_outline_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **resolution** | **float**| null | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region_shape**
> file get_footprint_region_shape(region_name)

Returns the shape description of the footprint region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Returns the shape description of the footprint region.
    api_response = api_instance.get_footprint_region_shape(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_region_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region_thumbnail**
> file get_footprint_region_thumbnail(region_name)

Gets the thumbnail of a footprint region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Gets the thumbnail of a footprint region.
    api_response = api_instance.get_footprint_region_thumbnail(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_region_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_shape**
> file get_footprint_shape()

Returns the shape description of the footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # Returns the shape description of the footprint.
    api_response = api_instance.get_footprint_shape()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_shape: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_thumbnail**
> file get_footprint_thumbnail()

Gets the thumbnail of the footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # Gets the thumbnail of the footprint.
    api_response = api_instance.get_footprint_thumbnail()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_thumbnail: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_footprint_regions**
> DefinitionFootprintRegionListResponse list_footprint_regions()

List all regions.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # List all regions.
    api_response = api_instance.list_footprint_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->list_footprint_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DefinitionFootprintRegionListResponse**](DefinitionFootprintRegionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_footprint_region**
> DefinitionFootprintRegionResponse modify_footprint_region(region_name)

Modify a region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Modify a region.
    api_response = api_instance.modify_footprint_region(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->modify_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**DefinitionFootprintRegionResponse**](DefinitionFootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint**
> file plot_footprint(projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style, highlights=highlights)

Plots the footprint

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
projection = 'projection_example' # str | null (optional)
sys = 'sys_example' # str | null (optional)
ra = 'ra_example' # str | null (optional)
dec = 'dec_example' # str | null (optional)
b = 'b_example' # str | null (optional)
l = 'l_example' # str | null (optional)
width = 3.4 # float | null (optional)
height = 3.4 # float | null (optional)
color_theme = 'color_theme_example' # str | null (optional)
auto_zoom = 'auto_zoom_example' # str | null (optional)
auto_rotate = 'auto_rotate_example' # str | null (optional)
grid = 'grid_example' # str | null (optional)
degree_style = 'degree_style_example' # str | null (optional)
highlights = 'highlights_example' # str | null (optional)

try:
    # Plots the footprint
    api_response = api_instance.plot_footprint(projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style, highlights=highlights)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **projection** | **str**| null | [optional] 
 **sys** | **str**| null | [optional] 
 **ra** | **str**| null | [optional] 
 **dec** | **str**| null | [optional] 
 **b** | **str**| null | [optional] 
 **l** | **str**| null | [optional] 
 **width** | **float**| null | [optional] 
 **height** | **float**| null | [optional] 
 **color_theme** | **str**| null | [optional] 
 **auto_zoom** | **str**| null | [optional] 
 **auto_rotate** | **str**| null | [optional] 
 **grid** | **str**| null | [optional] 
 **degree_style** | **str**| null | [optional] 
 **highlights** | **str**| null | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint_advanced**
> file plot_footprint_advanced()

Plots the footprint, with advanced parameters

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()

try:
    # Plots the footprint, with advanced parameters
    api_response = api_instance.plot_footprint_advanced()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint_advanced: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint_region**
> file plot_footprint_region(region_name, projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)

Plots a footprint region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null
projection = 'projection_example' # str | null (optional)
sys = 'sys_example' # str | null (optional)
ra = 'ra_example' # str | null (optional)
dec = 'dec_example' # str | null (optional)
b = 'b_example' # str | null (optional)
l = 'l_example' # str | null (optional)
width = 3.4 # float | null (optional)
height = 3.4 # float | null (optional)
color_theme = 'color_theme_example' # str | null (optional)
auto_zoom = 'auto_zoom_example' # str | null (optional)
auto_rotate = 'auto_rotate_example' # str | null (optional)
grid = 'grid_example' # str | null (optional)
degree_style = 'degree_style_example' # str | null (optional)

try:
    # Plots a footprint region.
    api_response = api_instance.plot_footprint_region(region_name, projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **projection** | **str**| null | [optional] 
 **sys** | **str**| null | [optional] 
 **ra** | **str**| null | [optional] 
 **dec** | **str**| null | [optional] 
 **b** | **str**| null | [optional] 
 **l** | **str**| null | [optional] 
 **width** | **float**| null | [optional] 
 **height** | **float**| null | [optional] 
 **color_theme** | **str**| null | [optional] 
 **auto_zoom** | **str**| null | [optional] 
 **auto_rotate** | **str**| null | [optional] 
 **grid** | **str**| null | [optional] 
 **degree_style** | **str**| null | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint_region_advanced**
> file plot_footprint_region_advanced(region_name)

Plots a footprint region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Plots a footprint region.
    api_response = api_instance.plot_footprint_region_advanced(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint_region_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_footprint_region_shape**
> set_footprint_region_shape(region_name)

Upload a region shape binary or other representation

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null

try:
    # Upload a region shape binary or other representation
    api_instance.set_footprint_region_shape(region_name)
except ApiException as e:
    print("Exception when calling EditorApi->set_footprint_region_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

