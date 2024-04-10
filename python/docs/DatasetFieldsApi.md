# openapi_client.DatasetFieldsApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset_field_configurations**](DatasetFieldsApi.md#create_dataset_field_configurations) | **POST** /datasets/{dataset_uid}/fields/ | Append a new field configuration
[**destroy_dataset_field_configurations**](DatasetFieldsApi.md#destroy_dataset_field_configurations) | **DELETE** /datasets/{dataset_uid}/fields/{field_uid}/ | Destroy a field configuration
[**list_dataset_field_configurations**](DatasetFieldsApi.md#list_dataset_field_configurations) | **GET** /datasets/{dataset_uid}/fields/ | List dataset field configurations
[**retrieve_dataset_field_configuration**](DatasetFieldsApi.md#retrieve_dataset_field_configuration) | **GET** /datasets/{dataset_uid}/fields/{field_uid}/ | Retrieve dataset field configuration
[**update_dataset_field**](DatasetFieldsApi.md#update_dataset_field) | **PUT** /datasets/{dataset_uid}/fields/{field_uid}/ | Update dataset field configuration


# **create_dataset_field_configurations**
> DatasetFieldConfiguration create_dataset_field_configurations(dataset_uid, dataset_field_configuration=dataset_field_configuration)

Append a new field configuration

Create a new field configuration for the dataset. The processor will be appended to the end of the fields configuration stack.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_field_configuration import DatasetFieldConfiguration
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
    api_instance = openapi_client.DatasetFieldsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    dataset_field_configuration = {"type":"rename","label":"Renaming field original_field_id","from_name":"original_field_id","to_name":"new_field_id","field_label":"New user friendly label"} # DatasetFieldConfiguration | Create a field configuration in a dataset (optional)

    try:
        # Append a new field configuration
        api_response = api_instance.create_dataset_field_configurations(dataset_uid, dataset_field_configuration=dataset_field_configuration)
        print("The response of DatasetFieldsApi->create_dataset_field_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetFieldsApi->create_dataset_field_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **dataset_field_configuration** | [**DatasetFieldConfiguration**](DatasetFieldConfiguration.md)| Create a field configuration in a dataset | [optional] 

### Return type

[**DatasetFieldConfiguration**](DatasetFieldConfiguration.md)

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

# **destroy_dataset_field_configurations**
> destroy_dataset_field_configurations(dataset_uid, field_uid)

Destroy a field configuration

Remove a field configuration from a dataset

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
    api_instance = openapi_client.DatasetFieldsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    field_uid = 'pr_qf2hyt' # str | 

    try:
        # Destroy a field configuration
        api_instance.destroy_dataset_field_configurations(dataset_uid, field_uid)
    except Exception as e:
        print("Exception when calling DatasetFieldsApi->destroy_dataset_field_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **field_uid** | **str**|  | 

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

# **list_dataset_field_configurations**
> ListDatasetFieldConfigurations200Response list_dataset_field_configurations(dataset_uid)

List dataset field configurations

List fields configurations for a dataset. Please note that it reads in the order in which processors are applied.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.list_dataset_field_configurations200_response import ListDatasetFieldConfigurations200Response
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
    api_instance = openapi_client.DatasetFieldsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 

    try:
        # List dataset field configurations
        api_response = api_instance.list_dataset_field_configurations(dataset_uid)
        print("The response of DatasetFieldsApi->list_dataset_field_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetFieldsApi->list_dataset_field_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 

### Return type

[**ListDatasetFieldConfigurations200Response**](ListDatasetFieldConfigurations200Response.md)

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

# **retrieve_dataset_field_configuration**
> DatasetFieldConfiguration retrieve_dataset_field_configuration(dataset_uid, field_uid)

Retrieve dataset field configuration

Retrieve a dataset field configuration

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_field_configuration import DatasetFieldConfiguration
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
    api_instance = openapi_client.DatasetFieldsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    field_uid = 'pr_qf2hyt' # str | 

    try:
        # Retrieve dataset field configuration
        api_response = api_instance.retrieve_dataset_field_configuration(dataset_uid, field_uid)
        print("The response of DatasetFieldsApi->retrieve_dataset_field_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetFieldsApi->retrieve_dataset_field_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **field_uid** | **str**|  | 

### Return type

[**DatasetFieldConfiguration**](DatasetFieldConfiguration.md)

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

# **update_dataset_field**
> DatasetFieldConfiguration update_dataset_field(dataset_uid, field_uid, dataset_field_configuration=dataset_field_configuration)

Update dataset field configuration

Update a field configuration in a dataset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_field_configuration import DatasetFieldConfiguration
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
    api_instance = openapi_client.DatasetFieldsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    field_uid = 'pr_qf2hyt' # str | 
    dataset_field_configuration = {"type":"rename","label":"Renaming field original_field_id","from_name":"original_field_id","to_name":"new_field_id","field_label":"New user friendly label"} # DatasetFieldConfiguration |  (optional)

    try:
        # Update dataset field configuration
        api_response = api_instance.update_dataset_field(dataset_uid, field_uid, dataset_field_configuration=dataset_field_configuration)
        print("The response of DatasetFieldsApi->update_dataset_field:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetFieldsApi->update_dataset_field: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **field_uid** | **str**|  | 
 **dataset_field_configuration** | [**DatasetFieldConfiguration**](DatasetFieldConfiguration.md)|  | [optional] 

### Return type

[**DatasetFieldConfiguration**](DatasetFieldConfiguration.md)

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

