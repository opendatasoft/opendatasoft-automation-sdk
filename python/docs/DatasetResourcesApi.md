# opendatasoft_automation.DatasetResourcesApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clean_resource_cache**](DatasetResourcesApi.md#clean_resource_cache) | **POST** /datasets/{dataset_uid}/resources/{resource_uid}/clean_cache/ | Clean cache of resource
[**create_dataset_resource**](DatasetResourcesApi.md#create_dataset_resource) | **POST** /datasets/{dataset_uid}/resources/ | Create dataset resource
[**delete_dataset_resource**](DatasetResourcesApi.md#delete_dataset_resource) | **DELETE** /datasets/{dataset_uid}/resources/{resource_uid}/ | Delete dataset resource
[**delete_recover_data_resource**](DatasetResourcesApi.md#delete_recover_data_resource) | **POST** /datasets/{dataset_uid}/resources/{resource_uid}/delete_recover_data/ | Delete realtime recovered data
[**disable_resource**](DatasetResourcesApi.md#disable_resource) | **POST** /datasets/{dataset_uid}/resources/{resource_uid}/disable/ | Disable realtime resource
[**download_dataset_resource_file**](DatasetResourcesApi.md#download_dataset_resource_file) | **GET** /datasets/{dataset_uid}/resources/files/{file_uid}/download/ | Download dataset resource file
[**enable_resource**](DatasetResourcesApi.md#enable_resource) | **POST** /datasets/{dataset_uid}/resources/{resource_uid}/enable/ | Enable realtime resource
[**guess_unsaved_resource_extractor_params**](DatasetResourcesApi.md#guess_unsaved_resource_extractor_params) | **POST** /datasets/{dataset_uid}/resources/guess_extractor_params/ | Guess unsaved resource extractor parameters
[**guess_unsaved_resource_extractors**](DatasetResourcesApi.md#guess_unsaved_resource_extractors) | **POST** /datasets/{dataset_uid}/resources/guess_extractors/ | Guess unsaved resource extractors
[**list_dataset_resources**](DatasetResourcesApi.md#list_dataset_resources) | **GET** /datasets/{dataset_uid}/resources/ | List dataset resources
[**list_extractors**](DatasetResourcesApi.md#list_extractors) | **GET** /extractors/ | List extractors
[**recover_resource**](DatasetResourcesApi.md#recover_resource) | **POST** /datasets/{dataset_uid}/resources/{resource_uid}/recover/ | Recover realtime data
[**resource_guess_extractor_params**](DatasetResourcesApi.md#resource_guess_extractor_params) | **GET** /datasets/{dataset_uid}/resources/{resource_uid}/guess_extractors_params/ | Guess resource extractor parameters
[**resource_guess_extractors**](DatasetResourcesApi.md#resource_guess_extractors) | **GET** /datasets/{dataset_uid}/resources/{resource_uid}/guess_extractors/ | Guess resource extractors
[**resource_preview**](DatasetResourcesApi.md#resource_preview) | **GET** /datasets/{dataset_uid}/resources/{resource_uid}/preview/ | Preview resource records
[**resource_renew_api_key**](DatasetResourcesApi.md#resource_renew_api_key) | **POST** /datasets/{dataset_uid}/resources/{resource_uid}/renew_api_key/ | Renew realtime resource API key
[**resource_unsaved_preview**](DatasetResourcesApi.md#resource_unsaved_preview) | **POST** /datasets/{dataset_uid}/resources/preview/ | Preview unsaved resource records
[**retrieve_dataset_resource**](DatasetResourcesApi.md#retrieve_dataset_resource) | **GET** /datasets/{dataset_uid}/resources/{resource_uid}/ | Retrieve dataset resource
[**retrieve_dataset_resource_file**](DatasetResourcesApi.md#retrieve_dataset_resource_file) | **GET** /datasets/{dataset_uid}/resources/files/{file_uid}/ | Retrieve dataset resource file
[**update_dataset_resource**](DatasetResourcesApi.md#update_dataset_resource) | **PUT** /datasets/{dataset_uid}/resources/{resource_uid}/ | Update dataset resource
[**upload_resource_file**](DatasetResourcesApi.md#upload_resource_file) | **POST** /datasets/{dataset_uid}/resources/files/ | Upload resource file


# **clean_resource_cache**
> clean_resource_cache(dataset_uid, resource_uid)

Clean cache of resource

Clean the cache of a given resource.

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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Clean cache of resource
        api_instance.clean_resource_cache(dataset_uid, resource_uid)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->clean_resource_cache: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

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
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dataset_resource**
> Resource create_dataset_resource(dataset_uid, resource=resource)

Create dataset resource

Create a new resource for the dataset. For now the supported resources in the API are HTTP, (s)FTP, uploaded files, S3, Azure Blob Storage, dataset federation, Snowflake, JCDecaux, Sharepoint and Google Drive.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource = {"type":"csvfile","title":"fromages.csv","params":{"doublequote":true,"encoding":"utf-8","first_row_no":1,"headers_first_row":true,"separator":";"},"datasource":{"type":"http","connection":{"type":"http","url":"https://my-server.com","auth":null},"headers":[{"name":"header-name","value":"header-value"}],"relative_url":"/fromages.csv"}} # Resource |  (optional)

    try:
        # Create dataset resource
        api_response = api_instance.create_dataset_resource(dataset_uid, resource=resource)
        print("The response of DatasetResourcesApi->create_dataset_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->create_dataset_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource** | [**Resource**](Resource.md)|  | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_resource**
> delete_dataset_resource(dataset_uid, resource_uid)

Delete dataset resource

Delete one dataset resource specified by its `uid`.

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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Delete dataset resource
        api_instance.delete_dataset_resource(dataset_uid, resource_uid)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->delete_dataset_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

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

# **delete_recover_data_resource**
> Resource delete_recover_data_resource(dataset_uid, resource_uid)

Delete realtime recovered data

Delete the recovered data of a realtime resource. The dataset must be published.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Delete realtime recovered data
        api_response = api_instance.delete_recover_data_resource(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->delete_recover_data_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->delete_recover_data_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**Resource**](Resource.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid dataset status |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_resource**
> Resource disable_resource(dataset_uid, resource_uid)

Disable realtime resource

Disable a realtime resource

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Disable realtime resource
        api_response = api_instance.disable_resource(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->disable_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->disable_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**Resource**](Resource.md)

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

# **download_dataset_resource_file**
> bytearray download_dataset_resource_file(dataset_uid, file_uid)

Download dataset resource file

Download a dataset resource file

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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    file_uid = 'fromages.csv' # str | 

    try:
        # Download dataset resource file
        api_response = api_instance.download_dataset_resource_file(dataset_uid, file_uid)
        print("The response of DatasetResourcesApi->download_dataset_resource_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->download_dataset_resource_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **file_uid** | **str**|  | 

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
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_resource**
> Resource enable_resource(dataset_uid, resource_uid)

Enable realtime resource

Enable a realtime resource

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Enable realtime resource
        api_response = api_instance.enable_resource(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->enable_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->enable_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**Resource**](Resource.md)

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

# **guess_unsaved_resource_extractor_params**
> GuessUnsavedResourceExtractorParams200Response guess_unsaved_resource_extractor_params(dataset_uid, guess_unsaved_resource_extractor_params_request=guess_unsaved_resource_extractor_params_request)

Guess unsaved resource extractor parameters

Guess the extractor parameters

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.guess_unsaved_resource_extractor_params200_response import GuessUnsavedResourceExtractorParams200Response
from opendatasoft_automation.models.guess_unsaved_resource_extractor_params_request import GuessUnsavedResourceExtractorParamsRequest
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    guess_unsaved_resource_extractor_params_request = opendatasoft_automation.GuessUnsavedResourceExtractorParamsRequest() # GuessUnsavedResourceExtractorParamsRequest |  (optional)

    try:
        # Guess unsaved resource extractor parameters
        api_response = api_instance.guess_unsaved_resource_extractor_params(dataset_uid, guess_unsaved_resource_extractor_params_request=guess_unsaved_resource_extractor_params_request)
        print("The response of DatasetResourcesApi->guess_unsaved_resource_extractor_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->guess_unsaved_resource_extractor_params: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **guess_unsaved_resource_extractor_params_request** | [**GuessUnsavedResourceExtractorParamsRequest**](GuessUnsavedResourceExtractorParamsRequest.md)|  | [optional] 

### Return type

[**GuessUnsavedResourceExtractorParams200Response**](GuessUnsavedResourceExtractorParams200Response.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **guess_unsaved_resource_extractors**
> List[Extractor] guess_unsaved_resource_extractors(dataset_uid, guess_unsaved_resource_extractors_request=guess_unsaved_resource_extractors_request)

Guess unsaved resource extractors

Guess the resource extractors

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.extractor import Extractor
from opendatasoft_automation.models.guess_unsaved_resource_extractors_request import GuessUnsavedResourceExtractorsRequest
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    guess_unsaved_resource_extractors_request = opendatasoft_automation.GuessUnsavedResourceExtractorsRequest() # GuessUnsavedResourceExtractorsRequest |  (optional)

    try:
        # Guess unsaved resource extractors
        api_response = api_instance.guess_unsaved_resource_extractors(dataset_uid, guess_unsaved_resource_extractors_request=guess_unsaved_resource_extractors_request)
        print("The response of DatasetResourcesApi->guess_unsaved_resource_extractors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->guess_unsaved_resource_extractors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **guess_unsaved_resource_extractors_request** | [**GuessUnsavedResourceExtractorsRequest**](GuessUnsavedResourceExtractorsRequest.md)|  | [optional] 

### Return type

[**List[Extractor]**](Extractor.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dataset_resources**
> ListDatasetResources200Response list_dataset_resources(dataset_uid, limit=limit, offset=offset, expand=expand)

List dataset resources

List all resources that are linked to a dataset.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_dataset_resources200_response import ListDatasetResources200Response
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)
    expand = 'expand_example' # str | The list of fields to expand. (optional)

    try:
        # List dataset resources
        api_response = api_instance.list_dataset_resources(dataset_uid, limit=limit, offset=offset, expand=expand)
        print("The response of DatasetResourcesApi->list_dataset_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->list_dataset_resources: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 
 **expand** | **str**| The list of fields to expand. | [optional] 

### Return type

[**ListDatasetResources200Response**](ListDatasetResources200Response.md)

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

# **list_extractors**
> List[Extractor] list_extractors()

List extractors

List available extractors

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.extractor import Extractor
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)

    try:
        # List extractors
        api_response = api_instance.list_extractors()
        print("The response of DatasetResourcesApi->list_extractors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->list_extractors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Extractor]**](Extractor.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recover_resource**
> Resource recover_resource(dataset_uid, resource_uid)

Recover realtime data

Recover the data of a realtime resource. The dataset must be published.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Recover realtime data
        api_response = api_instance.recover_resource(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->recover_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->recover_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**Resource**](Resource.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid dataset status |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_guess_extractor_params**
> ResourceGuessExtractorParams200Response resource_guess_extractor_params(dataset_uid, resource_uid)

Guess resource extractor parameters

Guess the resource extractor parameters

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource_guess_extractor_params200_response import ResourceGuessExtractorParams200Response
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Guess resource extractor parameters
        api_response = api_instance.resource_guess_extractor_params(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->resource_guess_extractor_params:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->resource_guess_extractor_params: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**ResourceGuessExtractorParams200Response**](ResourceGuessExtractorParams200Response.md)

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

# **resource_guess_extractors**
> List[Extractor] resource_guess_extractors(dataset_uid, resource_uid)

Guess resource extractors

Guess the resource extractors

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.extractor import Extractor
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Guess resource extractors
        api_response = api_instance.resource_guess_extractors(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->resource_guess_extractors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->resource_guess_extractors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**List[Extractor]**](Extractor.md)

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

# **resource_preview**
> InlineObject6 resource_preview(dataset_uid, resource_uid)

Preview resource records

In order to test a resource configuration, it can be useful to preview the data. This endpoint uses the configuration of a resource specified by its `uid` to generate a preview.

The preview is composed of the fields definitions and the content of the first records up to 20.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.inline_object6 import InlineObject6
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Preview resource records
        api_response = api_instance.resource_preview(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->resource_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->resource_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**InlineObject6**](InlineObject6.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource records preview |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resource_renew_api_key**
> Resource resource_renew_api_key(dataset_uid, resource_uid)

Renew realtime resource API key

Renew a realtime resource API key

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 

    try:
        # Renew realtime resource API key
        api_response = api_instance.resource_renew_api_key(dataset_uid, resource_uid)
        print("The response of DatasetResourcesApi->resource_renew_api_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->resource_renew_api_key: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 

### Return type

[**Resource**](Resource.md)

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

# **resource_unsaved_preview**
> InlineObject6 resource_unsaved_preview(dataset_uid, resource_unsaved_preview_request=resource_unsaved_preview_request)

Preview unsaved resource records

In order to test a resource configuration, it can be useful to preview the data. This endpoint uses a resource configuration passed in the payload to generate a preview.

The preview is composed of the fields definitions and the content of the first records up to 20.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.inline_object6 import InlineObject6
from opendatasoft_automation.models.resource_unsaved_preview_request import ResourceUnsavedPreviewRequest
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_unsaved_preview_request = opendatasoft_automation.ResourceUnsavedPreviewRequest() # ResourceUnsavedPreviewRequest |  (optional)

    try:
        # Preview unsaved resource records
        api_response = api_instance.resource_unsaved_preview(dataset_uid, resource_unsaved_preview_request=resource_unsaved_preview_request)
        print("The response of DatasetResourcesApi->resource_unsaved_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->resource_unsaved_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_unsaved_preview_request** | [**ResourceUnsavedPreviewRequest**](ResourceUnsavedPreviewRequest.md)|  | [optional] 

### Return type

[**InlineObject6**](InlineObject6.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource records preview |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_dataset_resource**
> Resource retrieve_dataset_resource(dataset_uid, resource_uid, expand=expand)

Retrieve dataset resource

Retrieve one dataset resource specified by its `uid`.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 
    expand = 'expand_example' # str | The list of fields to expand. (optional)

    try:
        # Retrieve dataset resource
        api_response = api_instance.retrieve_dataset_resource(dataset_uid, resource_uid, expand=expand)
        print("The response of DatasetResourcesApi->retrieve_dataset_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->retrieve_dataset_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 
 **expand** | **str**| The list of fields to expand. | [optional] 

### Return type

[**Resource**](Resource.md)

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

# **retrieve_dataset_resource_file**
> DatasetFile retrieve_dataset_resource_file(dataset_uid, file_uid)

Retrieve dataset resource file

Retrieve a dataset resource uploaded file

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_file import DatasetFile
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    file_uid = 'fromages.csv' # str | 

    try:
        # Retrieve dataset resource file
        api_response = api_instance.retrieve_dataset_resource_file(dataset_uid, file_uid)
        print("The response of DatasetResourcesApi->retrieve_dataset_resource_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->retrieve_dataset_resource_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **file_uid** | **str**|  | 

### Return type

[**DatasetFile**](DatasetFile.md)

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

# **update_dataset_resource**
> Resource update_dataset_resource(dataset_uid, resource_uid, resource=resource)

Update dataset resource

Update one dataset resource specified by its `uid`.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.resource import Resource
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    resource_uid = 're_qf2hyt' # str | 
    resource = {"type":"csvfile","title":"fromages.csv","params":{"doublequote":true,"encoding":"utf-8","first_row_no":1,"headers_first_row":true,"separator":";"},"datasource":{"type":"http","connection":{"uid":"co_qf2hyt"},"headers":[{"name":"header-name","value":"header-value"}],"relative_url":"/fromages.csv"}} # Resource |  (optional)

    try:
        # Update dataset resource
        api_response = api_instance.update_dataset_resource(dataset_uid, resource_uid, resource=resource)
        print("The response of DatasetResourcesApi->update_dataset_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->update_dataset_resource: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **resource_uid** | **str**|  | 
 **resource** | [**Resource**](Resource.md)|  | [optional] 

### Return type

[**Resource**](Resource.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_resource_file**
> DatasetFile upload_resource_file(dataset_uid, file)

Upload resource file

Upload a file to be used in a dataset resource. The HTTP request must be a multipart request with a `file` property.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_file import DatasetFile
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
    api_instance = opendatasoft_automation.DatasetResourcesApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    file = None # bytearray | 

    try:
        # Upload resource file
        api_response = api_instance.upload_resource_file(dataset_uid, file)
        print("The response of DatasetResourcesApi->upload_resource_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetResourcesApi->upload_resource_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**DatasetFile**](DatasetFile.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

