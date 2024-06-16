# opendatasoft_automation.HarvesterSchedulesApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_harvester_schedule**](HarvesterSchedulesApi.md#create_harvester_schedule) | **POST** /harvesters/{harvester_uid}/schedules/ | Create harvester schedule
[**delete_harvester_schedule**](HarvesterSchedulesApi.md#delete_harvester_schedule) | **DELETE** /harvesters/{harvester_uid}/schedules/{schedule_uid}/ | Delete harvester schedule
[**list_harvester_schedules**](HarvesterSchedulesApi.md#list_harvester_schedules) | **GET** /harvesters/{harvester_uid}/schedules/ | List harvester schedules
[**retrieve_harvester_schedule**](HarvesterSchedulesApi.md#retrieve_harvester_schedule) | **GET** /harvesters/{harvester_uid}/schedules/{schedule_uid}/ | Retrieve a harvester schedule
[**update_harvester_schedule**](HarvesterSchedulesApi.md#update_harvester_schedule) | **PUT** /harvesters/{harvester_uid}/schedules/{schedule_uid}/ | Update harvester schedule


# **create_harvester_schedule**
> HarvesterSchedule create_harvester_schedule(harvester_uid, harvester_schedule=harvester_schedule)

Create harvester schedule

Create a harvester schedule. A harvester can only have one schedule.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.harvester_schedule import HarvesterSchedule
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
    api_instance = opendatasoft_automation.HarvesterSchedulesApi(api_client)
    harvester_uid = 'harvester_uid' # str | 
    harvester_schedule = opendatasoft_automation.HarvesterSchedule() # HarvesterSchedule |  (optional)

    try:
        # Create harvester schedule
        api_response = api_instance.create_harvester_schedule(harvester_uid, harvester_schedule=harvester_schedule)
        print("The response of HarvesterSchedulesApi->create_harvester_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HarvesterSchedulesApi->create_harvester_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **harvester_uid** | **str**|  | 
 **harvester_schedule** | [**HarvesterSchedule**](HarvesterSchedule.md)|  | [optional] 

### Return type

[**HarvesterSchedule**](HarvesterSchedule.md)

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

# **delete_harvester_schedule**
> delete_harvester_schedule(harvester_uid, schedule_uid)

Delete harvester schedule

Delete a harvester schedule.

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
    api_instance = opendatasoft_automation.HarvesterSchedulesApi(api_client)
    harvester_uid = 'harvester_uid' # str | 
    schedule_uid = 'harvester_uid' # str | 

    try:
        # Delete harvester schedule
        api_instance.delete_harvester_schedule(harvester_uid, schedule_uid)
    except Exception as e:
        print("Exception when calling HarvesterSchedulesApi->delete_harvester_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **harvester_uid** | **str**|  | 
 **schedule_uid** | **str**|  | 

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

# **list_harvester_schedules**
> ListHarvesterSchedules200Response list_harvester_schedules(harvester_uid, limit=limit, offset=offset)

List harvester schedules

List harvester schedules.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_harvester_schedules200_response import ListHarvesterSchedules200Response
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
    api_instance = opendatasoft_automation.HarvesterSchedulesApi(api_client)
    harvester_uid = 'harvester_uid' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List harvester schedules
        api_response = api_instance.list_harvester_schedules(harvester_uid, limit=limit, offset=offset)
        print("The response of HarvesterSchedulesApi->list_harvester_schedules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HarvesterSchedulesApi->list_harvester_schedules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **harvester_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListHarvesterSchedules200Response**](ListHarvesterSchedules200Response.md)

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

# **retrieve_harvester_schedule**
> HarvesterSchedule retrieve_harvester_schedule(harvester_uid, schedule_uid)

Retrieve a harvester schedule

Retrieve a harvester schedule.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.harvester_schedule import HarvesterSchedule
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
    api_instance = opendatasoft_automation.HarvesterSchedulesApi(api_client)
    harvester_uid = 'harvester_uid' # str | 
    schedule_uid = 'harvester_uid' # str | 

    try:
        # Retrieve a harvester schedule
        api_response = api_instance.retrieve_harvester_schedule(harvester_uid, schedule_uid)
        print("The response of HarvesterSchedulesApi->retrieve_harvester_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HarvesterSchedulesApi->retrieve_harvester_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **harvester_uid** | **str**|  | 
 **schedule_uid** | **str**|  | 

### Return type

[**HarvesterSchedule**](HarvesterSchedule.md)

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

# **update_harvester_schedule**
> HarvesterSchedule update_harvester_schedule(harvester_uid, schedule_uid, harvester_schedule=harvester_schedule)

Update harvester schedule

Update a harvester schedule.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.harvester_schedule import HarvesterSchedule
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
    api_instance = opendatasoft_automation.HarvesterSchedulesApi(api_client)
    harvester_uid = 'harvester_uid' # str | 
    schedule_uid = 'harvester_uid' # str | 
    harvester_schedule = opendatasoft_automation.HarvesterSchedule() # HarvesterSchedule |  (optional)

    try:
        # Update harvester schedule
        api_response = api_instance.update_harvester_schedule(harvester_uid, schedule_uid, harvester_schedule=harvester_schedule)
        print("The response of HarvesterSchedulesApi->update_harvester_schedule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HarvesterSchedulesApi->update_harvester_schedule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **harvester_uid** | **str**|  | 
 **schedule_uid** | **str**|  | 
 **harvester_schedule** | [**HarvesterSchedule**](HarvesterSchedule.md)|  | [optional] 

### Return type

[**HarvesterSchedule**](HarvesterSchedule.md)

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

