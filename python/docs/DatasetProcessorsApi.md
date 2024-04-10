# openapi_client.DatasetProcessorsApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset_processor**](DatasetProcessorsApi.md#create_dataset_processor) | **POST** /datasets/{dataset_uid}/processors/ | Append a new processor
[**delete_dataset_processor**](DatasetProcessorsApi.md#delete_dataset_processor) | **DELETE** /datasets/{dataset_uid}/processors/{processor_uid}/ | Delete a dataset processor
[**list_dataset_processors**](DatasetProcessorsApi.md#list_dataset_processors) | **GET** /datasets/{dataset_uid}/processors/ | List dataset processors
[**list_processors**](DatasetProcessorsApi.md#list_processors) | **GET** /processors/ | List processors
[**retrieve_dataset_processor**](DatasetProcessorsApi.md#retrieve_dataset_processor) | **GET** /datasets/{dataset_uid}/processors/{processor_uid}/ | Retrieve dataset processor
[**update_dataset_processor**](DatasetProcessorsApi.md#update_dataset_processor) | **PUT** /datasets/{dataset_uid}/processors/{processor_uid}/ | Update dataset processor


# **create_dataset_processor**
> DatasetProcessor create_dataset_processor(dataset_uid, dataset_processor=dataset_processor)

Append a new processor

Create a new processor for the dataset. The processor will be appended to the end of the processing stack.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_processor import DatasetProcessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatasetProcessorsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    dataset_processor = {"type":"string_replace","label":"replace old value with new value","field":"my_field","old":"old_value","new":"new_value"} # DatasetProcessor |  (optional)

    try:
        # Append a new processor
        api_response = api_instance.create_dataset_processor(dataset_uid, dataset_processor=dataset_processor)
        print("The response of DatasetProcessorsApi->create_dataset_processor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetProcessorsApi->create_dataset_processor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **dataset_processor** | [**DatasetProcessor**](DatasetProcessor.md)|  | [optional] 

### Return type

[**DatasetProcessor**](DatasetProcessor.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset_processor**
> delete_dataset_processor(dataset_uid, processor_uid)

Delete a dataset processor

Remove a processor from a dataset.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatasetProcessorsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    processor_uid = 'pr_qf2hyt' # str | 

    try:
        # Delete a dataset processor
        api_instance.delete_dataset_processor(dataset_uid, processor_uid)
    except Exception as e:
        print("Exception when calling DatasetProcessorsApi->delete_dataset_processor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **processor_uid** | **str**|  | 

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

# **list_dataset_processors**
> ListDatasetProcessors200Response list_dataset_processors(dataset_uid)

List dataset processors

List configured processors for a dataset. Please note that it reads in the order in which processors are applied.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.list_dataset_processors200_response import ListDatasetProcessors200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatasetProcessorsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 

    try:
        # List dataset processors
        api_response = api_instance.list_dataset_processors(dataset_uid)
        print("The response of DatasetProcessorsApi->list_dataset_processors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetProcessorsApi->list_dataset_processors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 

### Return type

[**ListDatasetProcessors200Response**](ListDatasetProcessors200Response.md)

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

# **list_processors**
> List[DatasetProcessor] list_processors()

List processors

List all processors available on domain.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_processor import DatasetProcessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatasetProcessorsApi(api_client)

    try:
        # List processors
        api_response = api_instance.list_processors()
        print("The response of DatasetProcessorsApi->list_processors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetProcessorsApi->list_processors: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[DatasetProcessor]**](DatasetProcessor.md)

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

# **retrieve_dataset_processor**
> DatasetProcessor retrieve_dataset_processor(dataset_uid, processor_uid)

Retrieve dataset processor

Retrieve a dataset processor

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_processor import DatasetProcessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatasetProcessorsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    processor_uid = 'pr_qf2hyt' # str | 

    try:
        # Retrieve dataset processor
        api_response = api_instance.retrieve_dataset_processor(dataset_uid, processor_uid)
        print("The response of DatasetProcessorsApi->retrieve_dataset_processor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetProcessorsApi->retrieve_dataset_processor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **processor_uid** | **str**|  | 

### Return type

[**DatasetProcessor**](DatasetProcessor.md)

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

# **update_dataset_processor**
> DatasetProcessor update_dataset_processor(dataset_uid, processor_uid, dataset_processor=dataset_processor)

Update dataset processor

Update a processor in a dataset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_processor import DatasetProcessor
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://documentation-resources.opendatasoft.com/api/automation/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DatasetProcessorsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    processor_uid = 'pr_qf2hyt' # str | 
    dataset_processor = {"type":"string_replace","label":"replace old value with new value","field":"my_field","old":"old_value","new":"new_value"} # DatasetProcessor |  (optional)

    try:
        # Update dataset processor
        api_response = api_instance.update_dataset_processor(dataset_uid, processor_uid, dataset_processor=dataset_processor)
        print("The response of DatasetProcessorsApi->update_dataset_processor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetProcessorsApi->update_dataset_processor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **processor_uid** | **str**|  | 
 **dataset_processor** | [**DatasetProcessor**](DatasetProcessor.md)|  | [optional] 

### Return type

[**DatasetProcessor**](DatasetProcessor.md)

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

