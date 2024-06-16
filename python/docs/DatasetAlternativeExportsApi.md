# opendatasoft_automation.DatasetAlternativeExportsApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset_alternative_export**](DatasetAlternativeExportsApi.md#create_dataset_alternative_export) | **POST** /datasets/{dataset_uid}/alternative_exports/ | Create dataset alternative export
[**delete_dataset_alternative_export**](DatasetAlternativeExportsApi.md#delete_dataset_alternative_export) | **DELETE** /datasets/{dataset_uid}/alternative_exports/{export_uid}/ | Delete dataset alternative export
[**download_dataset_alternative_exports**](DatasetAlternativeExportsApi.md#download_dataset_alternative_exports) | **GET** /datasets/{dataset_uid}/alternative_exports/{export_uid}/download/ | Download dataset alternative export
[**list_dataset_alternative_exports**](DatasetAlternativeExportsApi.md#list_dataset_alternative_exports) | **GET** /datasets/{dataset_uid}/alternative_exports/ | List dataset alternative exports
[**retrieve_dataset_alternative_export**](DatasetAlternativeExportsApi.md#retrieve_dataset_alternative_export) | **GET** /datasets/{dataset_uid}/alternative_exports/{export_uid}/ | Retrieve dataset alternative export
[**update_dataset_alternative_export**](DatasetAlternativeExportsApi.md#update_dataset_alternative_export) | **PUT** /datasets/{dataset_uid}/alternative_exports/{export_uid}/ | Update dataset alternative export


# **create_dataset_alternative_export**
> DatasetAlternativeExport create_dataset_alternative_export(dataset_uid, title, type, file, description=description)

Create dataset alternative export

Create a dataset alternative export

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_alternative_export import DatasetAlternativeExport
from opendatasoft_automation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_automation.Configuration(
    host = "https://documentation-resources.opendatasoft.com/api/automation/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderAPIKey
configuration.api_key['HeaderAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderAPIKey'] = 'Bearer'

# Configure API key authorization: QueryAPIKey
configuration.api_key['QueryAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['QueryAPIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with opendatasoft_automation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_automation.DatasetAlternativeExportsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    title = 'title_example' # str | 
    type = 'type_example' # str | 
    file = None # bytearray | 
    description = 'description_example' # str |  (optional)

    try:
        # Create dataset alternative export
        api_response = api_instance.create_dataset_alternative_export(dataset_uid, title, type, file, description=description)
        print("The response of DatasetAlternativeExportsApi->create_dataset_alternative_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetAlternativeExportsApi->create_dataset_alternative_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **title** | **str**|  | 
 **type** | **str**|  | 
 **file** | **bytearray**|  | 
 **description** | **str**|  | [optional] 

### Return type

[**DatasetAlternativeExport**](DatasetAlternativeExport.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_alternative_export**
> delete_dataset_alternative_export(dataset_uid, export_uid)

Delete dataset alternative export

Delete a dataset alternative export

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_automation.Configuration(
    host = "https://documentation-resources.opendatasoft.com/api/automation/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderAPIKey
configuration.api_key['HeaderAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderAPIKey'] = 'Bearer'

# Configure API key authorization: QueryAPIKey
configuration.api_key['QueryAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['QueryAPIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with opendatasoft_automation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_automation.DatasetAlternativeExportsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    export_uid = 'ae_qf2hyt' # str | 

    try:
        # Delete dataset alternative export
        api_instance.delete_dataset_alternative_export(dataset_uid, export_uid)
    except Exception as e:
        print("Exception when calling DatasetAlternativeExportsApi->delete_dataset_alternative_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **export_uid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dataset_alternative_exports**
> bytearray download_dataset_alternative_exports(dataset_uid, export_uid)

Download dataset alternative export

Download the uploaded file alternative export or be redirected to the URL alternative export.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_automation.Configuration(
    host = "https://documentation-resources.opendatasoft.com/api/automation/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderAPIKey
configuration.api_key['HeaderAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderAPIKey'] = 'Bearer'

# Configure API key authorization: QueryAPIKey
configuration.api_key['QueryAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['QueryAPIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with opendatasoft_automation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_automation.DatasetAlternativeExportsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    export_uid = 'ae_qf2hyt' # str | 

    try:
        # Download dataset alternative export
        api_response = api_instance.download_dataset_alternative_exports(dataset_uid, export_uid)
        print("The response of DatasetAlternativeExportsApi->download_dataset_alternative_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetAlternativeExportsApi->download_dataset_alternative_exports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **export_uid** | **str**|  | 

### Return type

**bytearray**

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-disposition - attachment; filename&#x3D;\&quot;{filename}\&quot;; filename*&#x3D;UTF-8&#39;&#39;{filename} <br>  |
**303** | Redirection |  * Location - {url} <br>  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_alternative_exports**
> ListDatasetAlternativeExports200Response list_dataset_alternative_exports(dataset_uid, limit=limit, offset=offset)

List dataset alternative exports

List dataset alternative exports

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_dataset_alternative_exports200_response import ListDatasetAlternativeExports200Response
from opendatasoft_automation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_automation.Configuration(
    host = "https://documentation-resources.opendatasoft.com/api/automation/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderAPIKey
configuration.api_key['HeaderAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderAPIKey'] = 'Bearer'

# Configure API key authorization: QueryAPIKey
configuration.api_key['QueryAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['QueryAPIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with opendatasoft_automation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_automation.DatasetAlternativeExportsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List dataset alternative exports
        api_response = api_instance.list_dataset_alternative_exports(dataset_uid, limit=limit, offset=offset)
        print("The response of DatasetAlternativeExportsApi->list_dataset_alternative_exports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetAlternativeExportsApi->list_dataset_alternative_exports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListDatasetAlternativeExports200Response**](ListDatasetAlternativeExports200Response.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dataset_alternative_export**
> DatasetAlternativeExport retrieve_dataset_alternative_export(dataset_uid, export_uid)

Retrieve dataset alternative export

Retrieve a dataset alternative export

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_alternative_export import DatasetAlternativeExport
from opendatasoft_automation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_automation.Configuration(
    host = "https://documentation-resources.opendatasoft.com/api/automation/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderAPIKey
configuration.api_key['HeaderAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderAPIKey'] = 'Bearer'

# Configure API key authorization: QueryAPIKey
configuration.api_key['QueryAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['QueryAPIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with opendatasoft_automation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_automation.DatasetAlternativeExportsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    export_uid = 'ae_qf2hyt' # str | 

    try:
        # Retrieve dataset alternative export
        api_response = api_instance.retrieve_dataset_alternative_export(dataset_uid, export_uid)
        print("The response of DatasetAlternativeExportsApi->retrieve_dataset_alternative_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetAlternativeExportsApi->retrieve_dataset_alternative_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **export_uid** | **str**|  | 

### Return type

[**DatasetAlternativeExport**](DatasetAlternativeExport.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_alternative_export**
> DatasetAlternativeExport update_dataset_alternative_export(dataset_uid, export_uid, update_dataset_alternative_export_request=update_dataset_alternative_export_request)

Update dataset alternative export

Update a dataset alternative export

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_alternative_export import DatasetAlternativeExport
from opendatasoft_automation.models.update_dataset_alternative_export_request import UpdateDatasetAlternativeExportRequest
from opendatasoft_automation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = opendatasoft_automation.Configuration(
    host = "https://documentation-resources.opendatasoft.com/api/automation/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: HeaderAPIKey
configuration.api_key['HeaderAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['HeaderAPIKey'] = 'Bearer'

# Configure API key authorization: QueryAPIKey
configuration.api_key['QueryAPIKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['QueryAPIKey'] = 'Bearer'

# Enter a context with an instance of the API client
with opendatasoft_automation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = opendatasoft_automation.DatasetAlternativeExportsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    export_uid = 'ae_qf2hyt' # str | 
    update_dataset_alternative_export_request = opendatasoft_automation.UpdateDatasetAlternativeExportRequest() # UpdateDatasetAlternativeExportRequest |  (optional)

    try:
        # Update dataset alternative export
        api_response = api_instance.update_dataset_alternative_export(dataset_uid, export_uid, update_dataset_alternative_export_request=update_dataset_alternative_export_request)
        print("The response of DatasetAlternativeExportsApi->update_dataset_alternative_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetAlternativeExportsApi->update_dataset_alternative_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **export_uid** | **str**|  | 
 **update_dataset_alternative_export_request** | [**UpdateDatasetAlternativeExportRequest**](UpdateDatasetAlternativeExportRequest.md)|  | [optional] 

### Return type

[**DatasetAlternativeExport**](DatasetAlternativeExport.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

