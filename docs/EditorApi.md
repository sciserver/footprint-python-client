# footprint.EditorApi

All URIs are relative to *http://localhost/dobos/footprint-v2.0/Api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**c_hull_regions**](EditorApi.md#c_hull_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/chull | Generate the convex hull of the regions.
[**copy_region**](EditorApi.md#copy_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/copy | Copy a region.
[**create_region**](EditorApi.md#create_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName} | Create a new region.
[**delete_footprint**](EditorApi.md#delete_footprint) | **DELETE** V1/Editor.svc/footprint | Delete footprint and reset the editor.
[**delete_region**](EditorApi.md#delete_region) | **DELETE** V1/Editor.svc/footprint/regions/{regionName} | Delete a region.
[**download_footprint**](EditorApi.md#download_footprint) | **GET** V1/Editor.svc/footprint/raw | Returns the footprint in raw format text or binary.
[**download_footprint_outline**](EditorApi.md#download_footprint_outline) | **GET** V1/Editor.svc/footprint/outline/raw | Returns the outline of the footprint.
[**download_region**](EditorApi.md#download_region) | **GET** V1/Editor.svc/footprint/regions/{regionName}/raw | Returns the shape description of the footprint region.
[**download_region_outline**](EditorApi.md#download_region_outline) | **GET** V1/Editor.svc/footprint/regions/{regionName}/outline/raw | Returns the outline of the footprint.
[**get_footprint**](EditorApi.md#get_footprint) | **GET** V1/Editor.svc/footprint | Returns the header information of the edited footprint
[**get_footprint_outline_points**](EditorApi.md#get_footprint_outline_points) | **GET** V1/Editor.svc/footprint/outline/points | Returns the points of the outline of the footprint.
[**get_region**](EditorApi.md#get_region) | **GET** V1/Editor.svc/footprint/regions/{regionName} | Returns the header information of a region.
[**get_region_outline_points**](EditorApi.md#get_region_outline_points) | **GET** V1/Editor.svc/footprint/regions/{regionName}/outline/points | Returns the points of the outline of the region.
[**grow_region**](EditorApi.md#grow_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/grow | Grow region.
[**intersect_regions**](EditorApi.md#intersect_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/intersect | Compute the intersection of regions.
[**list_regions**](EditorApi.md#list_regions) | **GET** V1/Editor.svc/footprint/regions | List regions.
[**modify_footprint**](EditorApi.md#modify_footprint) | **PATCH** V1/Editor.svc/footprint | Modified the properties of the footprint in the editor.
[**modify_region**](EditorApi.md#modify_region) | **PATCH** V1/Editor.svc/footprint/regions/{regionName} | Modify a region.
[**plot_footprint**](EditorApi.md#plot_footprint) | **GET** V1/Editor.svc/footprint/plot | Plots the footprint
[**plot_footprint_advanced**](EditorApi.md#plot_footprint_advanced) | **POST** V1/Editor.svc/footprint/plot | Plots the footprint, with advanced parameters
[**plot_region**](EditorApi.md#plot_region) | **GET** V1/Editor.svc/footprint/regions/{regionName}/plot | Plots the region
[**plot_region_advanced**](EditorApi.md#plot_region_advanced) | **POST** V1/Editor.svc/footprint/regions/{regionName}/plot | Plots the footprint, with advanced parameters
[**rename_region**](EditorApi.md#rename_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/rename | Renames a region.
[**subtract_regions**](EditorApi.md#subtract_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/subtract | Compute the difference of regions.
[**union_regions**](EditorApi.md#union_regions) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/union | Compute the union of regions.
[**upload_region**](EditorApi.md#upload_region) | **PUT** V1/Editor.svc/footprint/regions/{regionName}/raw | Upload a region binary or other representation


# **c_hull_regions**
> RegionResponse c_hull_regions(region_name, request)

Generate the convex hull of the regions.

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Generate the convex hull of the regions.
    api_response = api_instance.c_hull_regions(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->c_hull_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copy_region**
> RegionResponse copy_region(region_name, request)

Copy a region.

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Copy a region.
    api_response = api_instance.copy_region(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->copy_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_region**
> RegionResponse create_region(region_name, request)

Create a new region.

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Create a new region.
    api_response = api_instance.create_region(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->create_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

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

# **delete_region**
> RestError delete_region(region_name)

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
    api_response = api_instance.delete_region(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->delete_region: %s\n" % e)
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

# **download_footprint**
> file download_footprint(accept)

Returns the footprint in raw format text or binary.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
accept = 'text/plain' # str | File format mime type. (default to text/plain)

try:
    # Returns the footprint in raw format text or binary.
    api_response = api_instance.download_footprint(accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->download_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| File format mime type. | [default to text/plain]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_footprint_outline**
> file download_footprint_outline(accept)

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
accept = 'text/plain' # str | File format mime type. (default to text/plain)

try:
    # Returns the outline of the footprint.
    api_response = api_instance.download_footprint_outline(accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->download_footprint_outline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| File format mime type. | [default to text/plain]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_region**
> file download_region(region_name, accept)

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
accept = 'text/plain' # str | File format mime type. (default to text/plain)

try:
    # Returns the shape description of the footprint region.
    api_response = api_instance.download_region(region_name, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->download_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **accept** | **str**| File format mime type. | [default to text/plain]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_region_outline**
> file download_region_outline(region_name, accept)

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
accept = 'text/plain' # str | File format mime type. (default to text/plain)

try:
    # Returns the outline of the footprint.
    api_response = api_instance.download_region_outline(region_name, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->download_region_outline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **accept** | **str**| File format mime type. | [default to text/plain]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_footprint_outline_points**
> list[Point] get_footprint_outline_points(sys=sys, rep=rep, resolution=resolution, reduce=reduce, limit=limit)

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
sys = 'sys_example' # str | null (optional)
rep = 'rep_example' # str | null (optional)
resolution = 'resolution_example' # str | null (optional)
reduce = 'reduce_example' # str | null (optional)
limit = 'limit_example' # str | null (optional)

try:
    # Returns the points of the outline of the footprint.
    api_response = api_instance.get_footprint_outline_points(sys=sys, rep=rep, resolution=resolution, reduce=reduce, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_footprint_outline_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sys** | **str**| null | [optional] 
 **rep** | **str**| null | [optional] 
 **resolution** | **str**| null | [optional] 
 **reduce** | **str**| null | [optional] 
 **limit** | **str**| null | [optional] 

### Return type

[**list[Point]**](Point.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_region**
> RegionResponse get_region(region_name)

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
    api_response = api_instance.get_region(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_region_outline_points**
> list[Point] get_region_outline_points(region_name, sys=sys, rep=rep, resolution=resolution, reduce=reduce, limit=limit)

Returns the points of the outline of the region.

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
sys = 'sys_example' # str | null (optional)
rep = 'rep_example' # str | null (optional)
resolution = 'resolution_example' # str | null (optional)
reduce = 'reduce_example' # str | null (optional)
limit = 'limit_example' # str | null (optional)

try:
    # Returns the points of the outline of the region.
    api_response = api_instance.get_region_outline_points(region_name, sys=sys, rep=rep, resolution=resolution, reduce=reduce, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->get_region_outline_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **sys** | **str**| null | [optional] 
 **rep** | **str**| null | [optional] 
 **resolution** | **str**| null | [optional] 
 **reduce** | **str**| null | [optional] 
 **limit** | **str**| null | [optional] 

### Return type

[**list[Point]**](Point.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **grow_region**
> RegionResponse grow_region(region_name, request, radius=radius)

Grow region.

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
request = footprint.RegionRequest() # RegionRequest | null
radius = 'radius_example' # str | null (optional)

try:
    # Grow region.
    api_response = api_instance.grow_region(region_name, request, radius=radius)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->grow_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 
 **radius** | **str**| null | [optional] 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **intersect_regions**
> RegionResponse intersect_regions(region_name, request)

Compute the intersection of regions.

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Compute the intersection of regions.
    api_response = api_instance.intersect_regions(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->intersect_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_regions**
> RegionListResponse list_regions(region_name=region_name, _from=_from, max=max)

List regions.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
region_name = 'region_name_example' # str | null (optional)
_from = '_from_example' # str | null (optional)
max = 'max_example' # str | null (optional)

try:
    # List regions.
    api_response = api_instance.list_regions(region_name=region_name, _from=_from, max=max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->list_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | [optional] 
 **_from** | **str**| null | [optional] 
 **max** | **str**| null | [optional] 

### Return type

[**RegionListResponse**](RegionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_footprint**
> FootprintResponse modify_footprint(footprint)

Modified the properties of the footprint in the editor.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.EditorApi()
footprint = footprint.FootprintRequest() # FootprintRequest | null

try:
    # Modified the properties of the footprint in the editor.
    api_response = api_instance.modify_footprint(footprint)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->modify_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **footprint** | [**FootprintRequest**](FootprintRequest.md)| null | 

### Return type

[**FootprintResponse**](FootprintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_region**
> RegionResponse modify_region(region_name, request)

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Modify a region.
    api_response = api_instance.modify_region(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->modify_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint**
> file plot_footprint(accept, projection=projection, sys=sys, lon=lon, lat=lat, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)

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
accept = 'image/png' # str | File format mime type. (default to image/png)
projection = 'projection_example' # str | null (optional)
sys = 'sys_example' # str | null (optional)
lon = 'lon_example' # str | null (optional)
lat = 'lat_example' # str | null (optional)
width = 'width_example' # str | null (optional)
height = 'height_example' # str | null (optional)
color_theme = 'color_theme_example' # str | null (optional)
auto_zoom = 'auto_zoom_example' # str | null (optional)
auto_rotate = 'auto_rotate_example' # str | null (optional)
grid = 'grid_example' # str | null (optional)
degree_style = 'degree_style_example' # str | null (optional)

try:
    # Plots the footprint
    api_response = api_instance.plot_footprint(accept, projection=projection, sys=sys, lon=lon, lat=lat, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | **str**| File format mime type. | [default to image/png]
 **projection** | **str**| null | [optional] 
 **sys** | **str**| null | [optional] 
 **lon** | **str**| null | [optional] 
 **lat** | **str**| null | [optional] 
 **width** | **str**| null | [optional] 
 **height** | **str**| null | [optional] 
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_footprint_advanced**
> file plot_footprint_advanced(plot, accept)

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
plot = footprint.PlotRequest() # PlotRequest | null
accept = 'image/png' # str | File format mime type. (default to image/png)

try:
    # Plots the footprint, with advanced parameters
    api_response = api_instance.plot_footprint_advanced(plot, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_footprint_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plot** | [**PlotRequest**](PlotRequest.md)| null | 
 **accept** | **str**| File format mime type. | [default to image/png]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_region**
> file plot_region(region_name, accept, projection=projection, sys=sys, lon=lon, lat=lat, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)

Plots the region

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
accept = 'image/png' # str | File format mime type. (default to image/png)
projection = 'projection_example' # str | null (optional)
sys = 'sys_example' # str | null (optional)
lon = 'lon_example' # str | null (optional)
lat = 'lat_example' # str | null (optional)
width = 'width_example' # str | null (optional)
height = 'height_example' # str | null (optional)
color_theme = 'color_theme_example' # str | null (optional)
auto_zoom = 'auto_zoom_example' # str | null (optional)
auto_rotate = 'auto_rotate_example' # str | null (optional)
grid = 'grid_example' # str | null (optional)
degree_style = 'degree_style_example' # str | null (optional)

try:
    # Plots the region
    api_response = api_instance.plot_region(region_name, accept, projection=projection, sys=sys, lon=lon, lat=lat, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **accept** | **str**| File format mime type. | [default to image/png]
 **projection** | **str**| null | [optional] 
 **sys** | **str**| null | [optional] 
 **lon** | **str**| null | [optional] 
 **lat** | **str**| null | [optional] 
 **width** | **str**| null | [optional] 
 **height** | **str**| null | [optional] 
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

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_region_advanced**
> file plot_region_advanced(region_name, plot, accept)

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
region_name = 'region_name_example' # str | null
plot = footprint.PlotRequest() # PlotRequest | null
accept = 'image/png' # str | File format mime type. (default to image/png)

try:
    # Plots the footprint, with advanced parameters
    api_response = api_instance.plot_region_advanced(region_name, plot, accept)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->plot_region_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **plot** | [**PlotRequest**](PlotRequest.md)| null | 
 **accept** | **str**| File format mime type. | [default to image/png]

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_region**
> RegionResponse rename_region(region_name, request)

Renames a region.

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Renames a region.
    api_response = api_instance.rename_region(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->rename_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subtract_regions**
> RegionResponse subtract_regions(region_name, request)

Compute the difference of regions.

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Compute the difference of regions.
    api_response = api_instance.subtract_regions(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->subtract_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **union_regions**
> RegionResponse union_regions(region_name, request)

Compute the union of regions.

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
request = footprint.RegionRequest() # RegionRequest | null

try:
    # Compute the union of regions.
    api_response = api_instance.union_regions(region_name, request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->union_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **request** | [**RegionRequest**](RegionRequest.md)| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_region**
> RegionResponse upload_region(region_name, content_type, region)

Upload a region binary or other representation

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
content_type = 'text/plain' # str | File format mime type. (default to text/plain)
region = '/path/to/file.txt' # file | null

try:
    # Upload a region binary or other representation
    api_response = api_instance.upload_region(region_name, content_type, region)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EditorApi->upload_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**| null | 
 **content_type** | **str**| File format mime type. | [default to text/plain]
 **region** | **file**| null | 

### Return type

[**RegionResponse**](RegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

