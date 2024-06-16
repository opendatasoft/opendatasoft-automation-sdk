# opendatasoft_automation.DatasetFeedbacksApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_dataset_feedback**](DatasetFeedbacksApi.md#archive_dataset_feedback) | **POST** /datasets/{dataset_uid}/feedbacks/{feedback_uid}/archive/ | Archive a dataset feedback
[**list_dataset_feedbacks**](DatasetFeedbacksApi.md#list_dataset_feedbacks) | **GET** /datasets/{dataset_uid}/feedbacks/ | List all dataset feedbacks
[**retrieve_dataset_feedback**](DatasetFeedbacksApi.md#retrieve_dataset_feedback) | **GET** /datasets/{dataset_uid}/feedbacks/{feedback_uid}/ | Retrieve a dataset feedback


# **archive_dataset_feedback**
> DatasetFeedback archive_dataset_feedback(dataset_uid, feedback_uid)

Archive a dataset feedback

Archive a dataset feedback

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_feedback import DatasetFeedback
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
    api_instance = opendatasoft_automation.DatasetFeedbacksApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    feedback_uid = 'df_qf2hyt' # str | Unique identifier for the feedback

    try:
        # Archive a dataset feedback
        api_response = api_instance.archive_dataset_feedback(dataset_uid, feedback_uid)
        print("The response of DatasetFeedbacksApi->archive_dataset_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetFeedbacksApi->archive_dataset_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **feedback_uid** | **str**| Unique identifier for the feedback | 

### Return type

[**DatasetFeedback**](DatasetFeedback.md)

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

# **list_dataset_feedbacks**
> ListDatasetFeedbacks200Response list_dataset_feedbacks(dataset_uid, record_id=record_id, is_archived=is_archived, sort=sort)

List all dataset feedbacks

List all dataset feedbacks. Archived feedbacks aren't listed by default, use the `is_archived` parameter to query them.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_dataset_feedbacks200_response import ListDatasetFeedbacks200Response
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
    api_instance = opendatasoft_automation.DatasetFeedbacksApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    record_id = 'record_id_example' # str | Find feedbacks made on a record with this id (optional)
    is_archived = True # bool | If true, list only archived feedbacks (optional)
    sort = '-created_at' # str | Sort by date of submission (optional) (default to '-created_at')

    try:
        # List all dataset feedbacks
        api_response = api_instance.list_dataset_feedbacks(dataset_uid, record_id=record_id, is_archived=is_archived, sort=sort)
        print("The response of DatasetFeedbacksApi->list_dataset_feedbacks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetFeedbacksApi->list_dataset_feedbacks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **record_id** | **str**| Find feedbacks made on a record with this id | [optional] 
 **is_archived** | **bool**| If true, list only archived feedbacks | [optional] 
 **sort** | **str**| Sort by date of submission | [optional] [default to &#39;-created_at&#39;]

### Return type

[**ListDatasetFeedbacks200Response**](ListDatasetFeedbacks200Response.md)

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

# **retrieve_dataset_feedback**
> DatasetFeedback retrieve_dataset_feedback(dataset_uid, feedback_uid)

Retrieve a dataset feedback

Retrieve a dataset feedback

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.dataset_feedback import DatasetFeedback
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
    api_instance = opendatasoft_automation.DatasetFeedbacksApi(api_client)
    dataset_uid = 'da_qf2hyt' # str | 
    feedback_uid = 'df_qf2hyt' # str | Unique identifier for the feedback

    try:
        # Retrieve a dataset feedback
        api_response = api_instance.retrieve_dataset_feedback(dataset_uid, feedback_uid)
        print("The response of DatasetFeedbacksApi->retrieve_dataset_feedback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasetFeedbacksApi->retrieve_dataset_feedback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset_uid** | **str**|  | 
 **feedback_uid** | **str**| Unique identifier for the feedback | 

### Return type

[**DatasetFeedback**](DatasetFeedback.md)

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

