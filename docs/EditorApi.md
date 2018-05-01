# footprint.EditorApi

All URIs are relative to *http://localhost/dobos/footprint-v2.0/Api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**combine_footprint_regions**](EditorApi.md#combine_footprint_regions) | **POST** V1/Editor.svc/footprint/regions/{regionName}?op&#x3D;{operation}&amp;keepOrig&#x3D;{keepOriginal} | Compute union, intersection or difference of regions.
[**create_footprint_region**](EditorApi.md#create_footprint_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName} | Create new region.
[**delete_footprint**](EditorApi.md#delete_footprint) | **DELETE** V1/Editor.svc/footprint | Delete footprint and reset the editor.
[**delete_footprint_region**](EditorApi.md#delete_footprint_region) | **DELETE** V1/Editor.svc/footprint/regions/{regionName} | Delete a region.
[**delete_footprint_regions**](EditorApi.md#delete_footprint_regions) | **DELETE** V1/Editor.svc/footprint/regions | Deletes multiple regions.
[**get_footprint**](EditorApi.md#get_footprint) | **GET** V1/Editor.svc/footprint | Returns the header information of the edited footprint
[**get_footprint_outline**](EditorApi.md#get_footprint_outline) | **GET** V1/Editor.svc/footprint/outline | Returns the outline of the footprint.
[**get_footprint_outline_points**](EditorApi.md#get_footprint_outline_points) | **GET** V1/Editor.svc/footprint/outline/points?res&#x3D;{resolution} | Returns the points of the outline of the footprint.
[**get_footprint_region**](EditorApi.md#get_footprint_region) | **GET** V1/Editor.svc/footprint/regions/{regionName} | Returns the header information of a region.
[**get_footprint_region_outline**](EditorApi.md#get_footprint_region_outline) | **GET** V1/Editor.svc/footprint/regions/{regionName}/outline | Returns the outline of the footprint.
[**get_footprint_region_outline_points**](EditorApi.md#get_footprint_region_outline_points) | **GET** V1/Editor.svc/footprint/regions/{regionName}/outline/points?res&#x3D;{resolution} | Returns the points of the outline of the footprint.
[**get_footprint_region_shape**](EditorApi.md#get_footprint_region_shape) | **GET** V1/Editor.svc/footprint/regions/{regionName}/shape | Returns the shape description of the footprint region.
[**get_footprint_region_thumbnail**](EditorApi.md#get_footprint_region_thumbnail) | **GET** V1/Editor.svc/footprint/regions/{regionName}/thumbnail | Gets the thumbnail of a footprint region.
[**get_footprint_shape**](EditorApi.md#get_footprint_shape) | **GET** V1/Editor.svc/footprint/shape | Returns the shape description of the footprint.
[**get_footprint_thumbnail**](EditorApi.md#get_footprint_thumbnail) | **GET** V1/Editor.svc/footprint/thumbnail | Gets the thumbnail of the footprint.
[**list_footprint_regions**](EditorApi.md#list_footprint_regions) | **GET** V1/Editor.svc/footprint/regions | List all regions.
[**modify_footprint_region**](EditorApi.md#modify_footprint_region) | **PATCH** V1/Editor.svc/footprint/regions/{regionName} | Modify a region.
[**plot_footprint**](EditorApi.md#plot_footprint) | **GET** V1/Editor.svc/footprint/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle}&amp;highlights&#x3D;{highlights} | Plots the footprint
[**plot_footprint_advanced**](EditorApi.md#plot_footprint_advanced) | **POST** V1/Editor.svc/footprint/plot | Plots the footprint, with advanced parameters
[**plot_footprint_region**](EditorApi.md#plot_footprint_region) | **GET** V1/Editor.svc/footprint/regions/{regionName}/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle} | Plots a footprint region.
[**plot_footprint_region_advanced**](EditorApi.md#plot_footprint_region_advanced) | **POST** V1/Editor.svc/footprint/regions/{regionName}/plot | Plots a footprint region.
[**set_footprint_region_shape**](EditorApi.md#set_footprint_region_shape) | **POST** V1/Editor.svc/footprint/regions/{regionName}/shape | Upload a region shape binary or other representation


# **combine_footprint_regions**
> FootprintRegionResponse combine_footprint_regions(region_name, request, operation=operation, keep_original=keep_original)

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
request = footprint.FootprintRegionRequest() # FootprintRegionRequest | null
operation = 'operation_example' # str | null (optional)
keep_original = 'keep_original_example' # str | null (optional)

try:
    # Compute union, intersection or difference of regions.
    api_response = api_instance.combine_footprint_regions(region_name, request, operation=operation, keep_original=keep_original)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->combine_footprint_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**FootprintRegionRequest**](FootprintRegionRequest.md)| null | 
 **operation** | **str**| null | [optional] 
 **keep_original** | **str**| null | [optional] 

### Return type

[**FootprintRegionResponse**](FootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_footprint_region**
> FootprintRegionResponse create_footprint_region(region_name, request)

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
request = footprint.FootprintRegionRequest() # FootprintRegionRequest | null

try:
    # Create new region.
    api_response = api_instance.create_footprint_region(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->create_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**FootprintRegionRequest**](FootprintRegionRequest.md)| null | 

### Return type

[**FootprintRegionResponse**](FootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footprint**
> RestError delete_footprint()

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
    api_response = api_instance.delete_footprint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->delete_footprint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RestError**](RestError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footprint_region**
> RestError delete_footprint_region(region_name)

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
    api_response = api_instance.delete_footprint_region(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->delete_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**RestError**](RestError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_footprint_regions**
> RestError delete_footprint_regions(region_names)

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
region_names = [footprint.list[str]()] # list[str] | null

try:
    # Deletes multiple regions.
    api_response = api_instance.delete_footprint_regions(region_names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->delete_footprint_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_names** | **list[str]**| null | 

### Return type

[**RestError**](RestError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint**
> FootprintResponse get_footprint()

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

[**FootprintResponse**](FootprintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_outline_points**
> EquatorialPoint get_footprint_outline_points(resolution=resolution)

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
resolution = 'resolution_example' # str | null (optional)

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
 **resolution** | **str**| null | [optional] 

### Return type

[**EquatorialPoint**](EquatorialPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region**
> FootprintRegionResponse get_footprint_region(region_name)

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

[**FootprintRegionResponse**](FootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region_outline**
> file get_footprint_region_outline()

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
    api_response = api_instance.get_footprint_region_outline()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_region_outline: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region_outline_points**
> EquatorialPoint get_footprint_region_outline_points(region_name, resolution=resolution)

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
resolution = 'resolution_example' # str | null (optional)

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
 **resolution** | **str**| null | [optional] 

### Return type

[**EquatorialPoint**](EquatorialPoint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_region_shape**
> file get_footprint_region_shape()

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

try:
    # Returns the shape description of the footprint region.
    api_response = api_instance.get_footprint_region_shape()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_region_shape: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/octet-stream, text/xml

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

 - **Content-Type**: Not defined
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

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/octet-stream, text/xml

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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_footprint_regions**
> FootprintRegionListResponse list_footprint_regions()

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

[**FootprintRegionListResponse**](FootprintRegionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_footprint_region**
> FootprintRegionResponse modify_footprint_region(region_name, request)

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
request = footprint.FootprintRegionRequest() # FootprintRegionRequest | null

try:
    # Modify a region.
    api_response = api_instance.modify_footprint_region(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->modify_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**FootprintRegionRequest**](FootprintRegionRequest.md)| null | 

### Return type

[**FootprintRegionResponse**](FootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint**
> file plot_footprint()

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

try:
    # Plots the footprint
    api_response = api_instance.plot_footprint()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/png, image/gif, image/bmp, application/pdf, application/postscript, windows/metafile

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

 - **Content-Type**: image/jpeg, image/png, image/gif, image/bmp, application/pdf, application/postscript, windows/metafile
 - **Accept**: image/jpeg, image/png, image/gif, image/bmp, application/pdf, application/postscript, windows/metafile

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint_region**
> file plot_footprint_region()

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

try:
    # Plots a footprint region.
    api_response = api_instance.plot_footprint_region()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint_region: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/jpeg, image/png, image/gif, image/bmp, application/pdf, application/postscript, windows/metafile

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint_region_advanced**
> file plot_footprint_region_advanced()

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

try:
    # Plots a footprint region.
    api_response = api_instance.plot_footprint_region_advanced()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint_region_advanced: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: image/jpeg, image/png, image/gif, image/bmp, application/pdf, application/postscript, windows/metafile
 - **Accept**: image/jpeg, image/png, image/gif, image/bmp, application/pdf, application/postscript, windows/metafile

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_footprint_region_shape**
> RestError set_footprint_region_shape(region_name)

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
    api_response = api_instance.set_footprint_region_shape(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->set_footprint_region_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**RestError**](RestError.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

