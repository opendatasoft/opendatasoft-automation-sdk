# opendatasoft_automation.DatasetVersionsApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dataset_versions**](DatasetVersionsApi.md#list_dataset_versions) | **GET** /datasets/{dataset_uid}/versions/ | List all versions
[**restore_version**](DatasetVersionsApi.md#restore_version) | **POST** /datasets/{dataset_uid}/versions/{version_uid}/restore/ | Restore version
[**retrieve_dataset_version**](DatasetVersionsApi.md#retrieve_dataset_version) | **GET** /datasets/{dataset_uid}/versions/{version_uid}/ | Retrieve version


# **list_dataset_versions**
> ListDatasetVersions200Response list_dataset_versions(dataset_uid, limit=limit, offset=offset)

List all versions

List the dataset versions.

**Note:** only the last 20 versions of a dataset are stored in the platform database.
For this reason, the API response will contain at most 20 results.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_dataset_versions200_response import ListDatasetVersions200Response
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
    api_instance = opendatasoft_automation.DatasetVersionsApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List all versions
        api_response = api_instance.list_dataset_versions(dataset_uid, limit=limit, offset=offset)
        print("The response of DatasetVersionsApi->list_dataset_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetVersionsApi->list_dataset_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListDatasetVersions200Response**](ListDatasetVersions200Response.md)

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

# **restore_version**
> Dataset restore_version(version_uid, dataset_uid)

Restore version

Restores a dataset to the selected version. Restoring a version will not erase the versions history, but rather create a new version encapsulating the restoration.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset import Dataset
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
    api_instance = opendatasoft_automation.DatasetVersionsApi(api_client)
    version_uid = 'ch_qf2hyt' # str | 
    dataset_uid = 'da_qf2hyt' # str | 

    try:
        # Restore version
        api_response = api_instance.restore_version(version_uid, dataset_uid)
        print("The response of DatasetVersionsApi->restore_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetVersionsApi->restore_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_uid** | **str**|  | 
 **dataset_uid** | **str**|  | 

### Return type

[**Dataset**](Dataset.md)

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

# **retrieve_dataset_version**
> DatasetVersion retrieve_dataset_version(version_uid, dataset_uid)

Retrieve version

Retrieve a dataset version.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_version import DatasetVersion
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
    api_instance = opendatasoft_automation.DatasetVersionsApi(api_client)
    version_uid = 'ch_qf2hyt' # str | 
    dataset_uid = 'da_qf2hyt' # str | 

    try:
        # Retrieve version
        api_response = api_instance.retrieve_dataset_version(version_uid, dataset_uid)
        print("The response of DatasetVersionsApi->retrieve_dataset_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetVersionsApi->retrieve_dataset_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version_uid** | **str**|  | 
 **dataset_uid** | **str**|  | 

### Return type

[**DatasetVersion**](DatasetVersion.md)

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

