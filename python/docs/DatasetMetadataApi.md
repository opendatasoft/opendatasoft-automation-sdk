# openapi_client.DatasetMetadataApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_template_field_dataset_metadata**](DatasetMetadataApi.md#delete_template_field_dataset_metadata) | **DELETE** /datasets/{dataset_uid}/metadata/{template_name}/{template_field_name}/ | Delete a metadata
[**list_all_dataset_metadata**](DatasetMetadataApi.md#list_all_dataset_metadata) | **GET** /datasets/{dataset_uid}/metadata/ | List all dataset metadata
[**list_template_dataset_metadata**](DatasetMetadataApi.md#list_template_dataset_metadata) | **GET** /datasets/{dataset_uid}/metadata/{template_name}/ | List a template&#39;s dataset metadata
[**retrieve_template_field_dataset_metadata**](DatasetMetadataApi.md#retrieve_template_field_dataset_metadata) | **GET** /datasets/{dataset_uid}/metadata/{template_name}/{template_field_name}/ | Retrieve a metadata
[**update_all_dataset_metadata**](DatasetMetadataApi.md#update_all_dataset_metadata) | **PUT** /datasets/{dataset_uid}/metadata/ | Update all dataset metadata
[**update_template_dataset_metadata**](DatasetMetadataApi.md#update_template_dataset_metadata) | **PUT** /datasets/{dataset_uid}/metadata/{template_name}/ | Update a template&#39;s dataset metadata
[**update_template_field_dataset_metadata**](DatasetMetadataApi.md#update_template_field_dataset_metadata) | **PUT** /datasets/{dataset_uid}/metadata/{template_name}/{template_field_name}/ | Update a metadata


# **delete_template_field_dataset_metadata**
> delete_template_field_dataset_metadata(dataset_uid, template_name, template_field_name)

Delete a metadata

Delete the metadata with the given name within the given template.

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
    api_instance = openapi_client.DatasetMetadataApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    template_name = 'template_name' # str | Metadata template name
    template_field_name = 'field_name' # str | Metadata template field name

    try:
        # Delete a metadata
        api_instance.delete_template_field_dataset_metadata(dataset_uid, template_name, template_field_name)
    except Exception as e:
        print("Exception when calling DatasetMetadataApi->delete_template_field_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **template_name** | **str**| Metadata template name | 
 **template_field_name** | **str**| Metadata template field name | 

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

# **list_all_dataset_metadata**
> DatasetMetadata list_all_dataset_metadata(dataset_uid)

List all dataset metadata

Returns the set of metadata for the dataset with the given UID.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_metadata import DatasetMetadata
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
    api_instance = openapi_client.DatasetMetadataApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 

    try:
        # List all dataset metadata
        api_response = api_instance.list_all_dataset_metadata(dataset_uid)
        print("The response of DatasetMetadataApi->list_all_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetMetadataApi->list_all_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 

### Return type

[**DatasetMetadata**](DatasetMetadata.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_template_dataset_metadata**
> DatasetMetadataTemplate list_template_dataset_metadata(dataset_uid, template_name)

List a template's dataset metadata

Returns the set of metadata within the given template for the dataset.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_metadata_template import DatasetMetadataTemplate
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
    api_instance = openapi_client.DatasetMetadataApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    template_name = 'template_name' # str | Metadata template name

    try:
        # List a template's dataset metadata
        api_response = api_instance.list_template_dataset_metadata(dataset_uid, template_name)
        print("The response of DatasetMetadataApi->list_template_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetMetadataApi->list_template_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **template_name** | **str**| Metadata template name | 

### Return type

[**DatasetMetadataTemplate**](DatasetMetadataTemplate.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_template_field_dataset_metadata**
> DatasetMetadataValue retrieve_template_field_dataset_metadata(dataset_uid, template_name, template_field_name)

Retrieve a metadata

Retrieve the metadata with the given name within the given template.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_metadata_value import DatasetMetadataValue
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
    api_instance = openapi_client.DatasetMetadataApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    template_name = 'template_name' # str | Metadata template name
    template_field_name = 'field_name' # str | Metadata template field name

    try:
        # Retrieve a metadata
        api_response = api_instance.retrieve_template_field_dataset_metadata(dataset_uid, template_name, template_field_name)
        print("The response of DatasetMetadataApi->retrieve_template_field_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetMetadataApi->retrieve_template_field_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **template_name** | **str**| Metadata template name | 
 **template_field_name** | **str**| Metadata template field name | 

### Return type

[**DatasetMetadataValue**](DatasetMetadataValue.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_all_dataset_metadata**
> DatasetMetadata update_all_dataset_metadata(dataset_uid, dataset_metadata=dataset_metadata)

Update all dataset metadata

Update all dataset metadata at once. This operation replaces the dataset metadata with the given payload: if a  metadata is omitted, it will be removed from the dataset.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_metadata import DatasetMetadata
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
    api_instance = openapi_client.DatasetMetadataApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    dataset_metadata = openapi_client.DatasetMetadata() # DatasetMetadata |  (optional)

    try:
        # Update all dataset metadata
        api_response = api_instance.update_all_dataset_metadata(dataset_uid, dataset_metadata=dataset_metadata)
        print("The response of DatasetMetadataApi->update_all_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetMetadataApi->update_all_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **dataset_metadata** | [**DatasetMetadata**](DatasetMetadata.md)|  | [optional] 

### Return type

[**DatasetMetadata**](DatasetMetadata.md)

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

# **update_template_dataset_metadata**
> DatasetMetadataTemplate update_template_dataset_metadata(dataset_uid, template_name, dataset_metadata_template=dataset_metadata_template)

Update a template's dataset metadata

Update dataset metadata within a given template. This operation replaces the dataset metadata with the given payload:  if a metadata is omitted, it will be removed from the dataset.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_metadata_template import DatasetMetadataTemplate
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
    api_instance = openapi_client.DatasetMetadataApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    template_name = 'template_name' # str | Metadata template name
    dataset_metadata_template = openapi_client.DatasetMetadataTemplate() # DatasetMetadataTemplate |  (optional)

    try:
        # Update a template's dataset metadata
        api_response = api_instance.update_template_dataset_metadata(dataset_uid, template_name, dataset_metadata_template=dataset_metadata_template)
        print("The response of DatasetMetadataApi->update_template_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetMetadataApi->update_template_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **template_name** | **str**| Metadata template name | 
 **dataset_metadata_template** | [**DatasetMetadataTemplate**](DatasetMetadataTemplate.md)|  | [optional] 

### Return type

[**DatasetMetadataTemplate**](DatasetMetadataTemplate.md)

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

# **update_template_field_dataset_metadata**
> DatasetMetadataValue update_template_field_dataset_metadata(dataset_uid, template_name, template_field_name, dataset_metadata_value=dataset_metadata_value)

Update a metadata

Update the metadata with the given name within the given template.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.dataset_metadata_value import DatasetMetadataValue
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
    api_instance = openapi_client.DatasetMetadataApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    template_name = 'template_name' # str | Metadata template name
    template_field_name = 'field_name' # str | Metadata template field name
    dataset_metadata_value = openapi_client.DatasetMetadataValue() # DatasetMetadataValue |  (optional)

    try:
        # Update a metadata
        api_response = api_instance.update_template_field_dataset_metadata(dataset_uid, template_name, template_field_name, dataset_metadata_value=dataset_metadata_value)
        print("The response of DatasetMetadataApi->update_template_field_dataset_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetMetadataApi->update_template_field_dataset_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **template_name** | **str**| Metadata template name | 
 **template_field_name** | **str**| Metadata template field name | 
 **dataset_metadata_value** | [**DatasetMetadataValue**](DatasetMetadataValue.md)|  | [optional] 

### Return type

[**DatasetMetadataValue**](DatasetMetadataValue.md)

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

