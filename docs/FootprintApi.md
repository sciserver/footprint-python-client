# footprint.FootprintApi

All URIs are relative to *http://localhost/dobos/footprint-v2.0/Api/V1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_user_footprint**](FootprintApi.md#copy_user_footprint) | **POST** /users/{owner}/footprints/{name}?op&#x3D;copy | Copy from and existing footprint.
[**create_user_footprint**](FootprintApi.md#create_user_footprint) | **POST** /users/{owner}/footprints/{name} | Create new footprint.
[**create_user_footprint_region**](FootprintApi.md#create_user_footprint_region) | **POST** /users/{owner}/footprints/{name}/regions/{regionName} | Create new region under an existing footprint.
[**delete_user_footprint**](FootprintApi.md#delete_user_footprint) | **DELETE** /users/{owner}/footprints/{name} | Delete footprint.
[**delete_user_footprint_region**](FootprintApi.md#delete_user_footprint_region) | **DELETE** /users/{owner}/footprints/{name}/regions/{regionName} | Delete a region under an existing footprint.
[**find_footprints**](FootprintApi.md#find_footprints) | **GET** /footprints?owner&#x3D;{owner}&amp;name&#x3D;{name}&amp;from&#x3D;{from}&amp;max&#x3D;{max} | Returns the list of footprints of the user.
[**find_user_footprint_regions**](FootprintApi.md#find_user_footprint_regions) | **GET** /users/{owner}/footprints/{name}/regions?regionName&#x3D;{regionName}&amp;from&#x3D;{from}&amp;max&#x3D;{max} | Returns the list of the regions of a footprint.
[**find_user_footprints**](FootprintApi.md#find_user_footprints) | **GET** /users/{owner}/footprints?name&#x3D;{name}&amp;from&#x3D;{from}&amp;max&#x3D;{max} | Returns the list of footprints of the user.
[**get_user_footprint**](FootprintApi.md#get_user_footprint) | **GET** /users/{owner}/footprints/{name} | Returns the header information of a footprint.
[**get_user_footprint_outline**](FootprintApi.md#get_user_footprint_outline) | **GET** /users/{owner}/footprints/{name}/outline | Returns the outline a footprint.
[**get_user_footprint_outline_points**](FootprintApi.md#get_user_footprint_outline_points) | **GET** /users/{owner}/footprints/{name}/outline/points?res&#x3D;{resolution} | Returns the points of the outline of a footprint.
[**get_user_footprint_region**](FootprintApi.md#get_user_footprint_region) | **GET** /users/{owner}/footprints/{name}/regions/{regionName} | Returns the header information of a region.
[**get_user_footprint_region_outline**](FootprintApi.md#get_user_footprint_region_outline) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/outline | Returns the outline a footprint.
[**get_user_footprint_region_outline_points**](FootprintApi.md#get_user_footprint_region_outline_points) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/outline/points?res&#x3D;{resolution} | Returns the points of the outline of a footprint.
[**get_user_footprint_region_shape**](FootprintApi.md#get_user_footprint_region_shape) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/shape | Returns the shape description of a footprint.
[**get_user_footprint_region_thumbnail**](FootprintApi.md#get_user_footprint_region_thumbnail) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/thumbnail | Get the thumbnail of a footprint.
[**get_user_footprint_shape**](FootprintApi.md#get_user_footprint_shape) | **GET** /users/{owner}/footprints/{name}/shape | Returns the shape description of a footprint.
[**get_user_footprint_thumbnail**](FootprintApi.md#get_user_footprint_thumbnail) | **GET** /users/{owner}/footprints/{name}/thumbnail | Get the thumbnail of a footprint.
[**modify_user_footprint**](FootprintApi.md#modify_user_footprint) | **PATCH** /users/{owner}/footprints/{name} | Modify existing footprint.
[**modify_user_footprint_region**](FootprintApi.md#modify_user_footprint_region) | **PUT** /users/{owner}/footprints/{name}/regions/{regionName} | Modify a region under an existing footprint.
[**plot_user_footprint**](FootprintApi.md#plot_user_footprint) | **GET** /users/{owner}/footprints/{name}/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle} | Plots a footprint
[**plot_user_footprint_advanced**](FootprintApi.md#plot_user_footprint_advanced) | **POST** /users/{owner}/footprints/{name}/plot | Plots a footprint, with advanced parameters
[**plot_user_footprint_region**](FootprintApi.md#plot_user_footprint_region) | **GET** /users/{owner}/footprints/{name}/regions/{regionName}/plot?proj&#x3D;{projection}&amp;sys&#x3D;{sys}&amp;ra&#x3D;{ra}&amp;dec&#x3D;{dec}&amp;b&#x3D;{b}&amp;l&#x3D;{l}&amp;width&#x3D;{width}&amp;height&#x3D;{height}&amp;theme&#x3D;{colorTheme}&amp;zoom&#x3D;{autoZoom}&amp;rotate&#x3D;{autoRotate}&amp;grid&#x3D;{grid}&amp;degStyle&#x3D;{degreeStyle} | Plots a footprint.
[**plot_user_footprint_region_advanced**](FootprintApi.md#plot_user_footprint_region_advanced) | **POST** /users/{owner}/footprints/{name}/regions/{regionName}/plot | Plots a footprint.
[**set_user_footprint_region_shape**](FootprintApi.md#set_user_footprint_region_shape) | **POST** /users/{owner}/footprints/{name}/regions/{regionName}/shape | Upload region shape binary or other representation


# **copy_user_footprint**
> DefinitionFootprintResponse copy_user_footprint(owner, name)

Copy from and existing footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Copy from and existing footprint.
    api_response = api_instance.copy_user_footprint(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->copy_user_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**DefinitionFootprintResponse**](DefinitionFootprintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_footprint**
> DefinitionFootprintResponse create_user_footprint(owner, name)

Create new footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Create new footprint.
    api_response = api_instance.create_user_footprint(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->create_user_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**DefinitionFootprintResponse**](DefinitionFootprintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_footprint_region**
> DefinitionFootprintRegionResponse create_user_footprint_region(owner, name, region_name)

Create new region under an existing footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Create new region under an existing footprint.
    api_response = api_instance.create_user_footprint_region(owner, name, region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->create_user_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

[**DefinitionFootprintRegionResponse**](DefinitionFootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_footprint**
> delete_user_footprint(owner, name)

Delete footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Delete footprint.
    api_instance.delete_user_footprint(owner, name)
except ApiException as e:
    print("Exception when calling FootprintApi->delete_user_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_footprint_region**
> delete_user_footprint_region(owner, name, region_name)

Delete a region under an existing footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Delete a region under an existing footprint.
    api_instance.delete_user_footprint_region(owner, name, region_name)
except ApiException as e:
    print("Exception when calling FootprintApi->delete_user_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_footprints**
> DefinitionFootprintListResponse find_footprints(owner=owner, name=name, _from=_from, max=max)

Returns the list of footprints of the user.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null (optional)
name = 'name_example' # str | null (optional)
_from = 56 # int | null (optional)
max = 56 # int | null (optional)

try:
    # Returns the list of footprints of the user.
    api_response = api_instance.find_footprints(owner=owner, name=name, _from=_from, max=max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->find_footprints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | [optional] 
 **name** | **str**| null | [optional] 
 **_from** | **int**| null | [optional] 
 **max** | **int**| null | [optional] 

### Return type

[**DefinitionFootprintListResponse**](DefinitionFootprintListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_footprint_regions**
> DefinitionFootprintRegionListResponse find_user_footprint_regions(owner, name, region_name=region_name, _from=_from, max=max)

Returns the list of the regions of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null (optional)
_from = 56 # int | null (optional)
max = 56 # int | null (optional)

try:
    # Returns the list of the regions of a footprint.
    api_response = api_instance.find_user_footprint_regions(owner, name, region_name=region_name, _from=_from, max=max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->find_user_footprint_regions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | [optional] 
 **_from** | **int**| null | [optional] 
 **max** | **int**| null | [optional] 

### Return type

[**DefinitionFootprintRegionListResponse**](DefinitionFootprintRegionListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_footprints**
> DefinitionFootprintListResponse find_user_footprints(owner, name=name, _from=_from, max=max)

Returns the list of footprints of the user.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null (optional)
_from = 56 # int | null (optional)
max = 56 # int | null (optional)

try:
    # Returns the list of footprints of the user.
    api_response = api_instance.find_user_footprints(owner, name=name, _from=_from, max=max)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->find_user_footprints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | [optional] 
 **_from** | **int**| null | [optional] 
 **max** | **int**| null | [optional] 

### Return type

[**DefinitionFootprintListResponse**](DefinitionFootprintListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint**
> DefinitionFootprintResponse get_user_footprint(owner, name)

Returns the header information of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Returns the header information of a footprint.
    api_response = api_instance.get_user_footprint(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**DefinitionFootprintResponse**](DefinitionFootprintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_outline**
> file get_user_footprint_outline(owner, name)

Returns the outline a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Returns the outline a footprint.
    api_response = api_instance.get_user_footprint_outline(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_outline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_outline_points**
> file get_user_footprint_outline_points(owner, name, resolution=resolution)

Returns the points of the outline of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
resolution = 1.2 # float | null (optional)

try:
    # Returns the points of the outline of a footprint.
    api_response = api_instance.get_user_footprint_outline_points(owner, name, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_outline_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **resolution** | **float**| null | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_region**
> DefinitionFootprintRegionResponse get_user_footprint_region(owner, name, region_name)

Returns the header information of a region.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Returns the header information of a region.
    api_response = api_instance.get_user_footprint_region(owner, name, region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

[**DefinitionFootprintRegionResponse**](DefinitionFootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_region_outline**
> file get_user_footprint_region_outline(owner, name, region_name)

Returns the outline a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Returns the outline a footprint.
    api_response = api_instance.get_user_footprint_region_outline(owner, name, region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_region_outline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_region_outline_points**
> file get_user_footprint_region_outline_points(owner, name, region_name, resolution=resolution)

Returns the points of the outline of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null
resolution = 1.2 # float | null (optional)

try:
    # Returns the points of the outline of a footprint.
    api_response = api_instance.get_user_footprint_region_outline_points(owner, name, region_name, resolution=resolution)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_region_outline_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
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

# **get_user_footprint_region_shape**
> file get_user_footprint_region_shape(owner, name, region_name)

Returns the shape description of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Returns the shape description of a footprint.
    api_response = api_instance.get_user_footprint_region_shape(owner, name, region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_region_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_region_thumbnail**
> file get_user_footprint_region_thumbnail(owner, name, region_name)

Get the thumbnail of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Get the thumbnail of a footprint.
    api_response = api_instance.get_user_footprint_region_thumbnail(owner, name, region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_region_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_shape**
> file get_user_footprint_shape(owner, name)

Returns the shape description of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Returns the shape description of a footprint.
    api_response = api_instance.get_user_footprint_shape(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_footprint_thumbnail**
> file get_user_footprint_thumbnail(owner, name)

Get the thumbnail of a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Get the thumbnail of a footprint.
    api_response = api_instance.get_user_footprint_thumbnail(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->get_user_footprint_thumbnail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user_footprint**
> DefinitionFootprintResponse modify_user_footprint(owner, name)

Modify existing footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Modify existing footprint.
    api_response = api_instance.modify_user_footprint(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->modify_user_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**DefinitionFootprintResponse**](DefinitionFootprintResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user_footprint_region**
> DefinitionFootprintRegionResponse modify_user_footprint_region(owner, name, region_name)

Modify a region under an existing footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Modify a region under an existing footprint.
    api_response = api_instance.modify_user_footprint_region(owner, name, region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->modify_user_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

[**DefinitionFootprintRegionResponse**](DefinitionFootprintRegionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_user_footprint**
> file plot_user_footprint(owner, name, projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)

Plots a footprint

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
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
    # Plots a footprint
    api_response = api_instance.plot_user_footprint(owner, name, projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->plot_user_footprint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
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

# **plot_user_footprint_advanced**
> file plot_user_footprint_advanced(owner, name)

Plots a footprint, with advanced parameters

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null

try:
    # Plots a footprint, with advanced parameters
    api_response = api_instance.plot_user_footprint_advanced(owner, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->plot_user_footprint_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plot_user_footprint_region**
> file plot_user_footprint_region(owner, name, region_name, projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)

Plots a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
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
    # Plots a footprint.
    api_response = api_instance.plot_user_footprint_region(owner, name, region_name, projection=projection, sys=sys, ra=ra, dec=dec, b=b, l=l, width=width, height=height, color_theme=color_theme, auto_zoom=auto_zoom, auto_rotate=auto_rotate, grid=grid, degree_style=degree_style)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->plot_user_footprint_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
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

# **plot_user_footprint_region_advanced**
> file plot_user_footprint_region_advanced(owner, name, region_name)

Plots a footprint.

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Plots a footprint.
    api_response = api_instance.plot_user_footprint_region_advanced(owner, name, region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FootprintApi->plot_user_footprint_region_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_footprint_region_shape**
> set_user_footprint_region_shape(owner, name, region_name)

Upload region shape binary or other representation

### Example
```python
from __future__ import print_function
import time
import footprint
from footprint.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = footprint.FootprintApi()
owner = 'owner_example' # str | null
name = 'name_example' # str | null
region_name = 'region_name_example' # str | null

try:
    # Upload region shape binary or other representation
    api_instance.set_user_footprint_region_shape(owner, name, region_name)
except ApiException as e:
    print("Exception when calling FootprintApi->set_user_footprint_region_shape: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**| null | 
 **name** | **str**| null | 
 **region_name** | **str**| null | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

