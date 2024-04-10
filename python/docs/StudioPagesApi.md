# openapi_client.StudioPagesApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_studio_page**](StudioPagesApi.md#create_studio_page) | **POST** /studio_pages/ | Create page
[**delete_studio_page**](StudioPagesApi.md#delete_studio_page) | **DELETE** /studio_pages/{studio_page_uid}/ | Delete page
[**list_studio_pages**](StudioPagesApi.md#list_studio_pages) | **GET** /studio_pages/ | List pages
[**publish_studio_page**](StudioPagesApi.md#publish_studio_page) | **POST** /studio_pages/{studio_page_uid}/publish/ | Publish page
[**retrieve_studio_page**](StudioPagesApi.md#retrieve_studio_page) | **GET** /studio_pages/{studio_page_uid}/ | Retrieve page
[**unpublish_studio_page**](StudioPagesApi.md#unpublish_studio_page) | **POST** /studio_pages/{studio_page_uid}/unpublish/ | Unpublish page
[**update_studio_page**](StudioPagesApi.md#update_studio_page) | **PUT** /studio_pages/{studio_page_uid}/ | Update page


# **create_studio_page**
> StudioPage create_studio_page(studio_page=studio_page)

Create page

Create a studio page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.studio_page import StudioPage
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
    api_instance = openapi_client.StudioPagesApi(api_client)
    studio_page = openapi_client.StudioPage() # StudioPage |  (optional)

    try:
        # Create page
        api_response = api_instance.create_studio_page(studio_page=studio_page)
        print("The response of StudioPagesApi->create_studio_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesApi->create_studio_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page** | [**StudioPage**](StudioPage.md)|  | [optional] 

### Return type

[**StudioPage**](StudioPage.md)

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
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_studio_page**
> delete_studio_page(studio_page_uid)

Delete page

Delete a studio page

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
    api_instance = openapi_client.StudioPagesApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 

    try:
        # Delete page
        api_instance.delete_studio_page(studio_page_uid)
    except Exception as e:
        print("Exception when calling StudioPagesApi->delete_studio_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 

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

# **list_studio_pages**
> ListStudioPages200Response list_studio_pages(limit=limit, offset=offset)

List pages

List studio pages

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.list_studio_pages200_response import ListStudioPages200Response
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
    api_instance = openapi_client.StudioPagesApi(api_client)
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List pages
        api_response = api_instance.list_studio_pages(limit=limit, offset=offset)
        print("The response of StudioPagesApi->list_studio_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesApi->list_studio_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListStudioPages200Response**](ListStudioPages200Response.md)

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

# **publish_studio_page**
> PublishDataset200Response publish_studio_page(studio_page_uid)

Publish page

Publish a studio page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.publish_dataset200_response import PublishDataset200Response
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
    api_instance = openapi_client.StudioPagesApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 

    try:
        # Publish page
        api_response = api_instance.publish_studio_page(studio_page_uid)
        print("The response of StudioPagesApi->publish_studio_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesApi->publish_studio_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 

### Return type

[**PublishDataset200Response**](PublishDataset200Response.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The action has been performed |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_studio_page**
> StudioPage retrieve_studio_page(studio_page_uid)

Retrieve page

Retrieve a studio page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.studio_page import StudioPage
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
    api_instance = openapi_client.StudioPagesApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 

    try:
        # Retrieve page
        api_response = api_instance.retrieve_studio_page(studio_page_uid)
        print("The response of StudioPagesApi->retrieve_studio_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesApi->retrieve_studio_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 

### Return type

[**StudioPage**](StudioPage.md)

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

# **unpublish_studio_page**
> PublishDataset200Response unpublish_studio_page(studio_page_uid)

Unpublish page

Unpublish a studio page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.publish_dataset200_response import PublishDataset200Response
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
    api_instance = openapi_client.StudioPagesApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 

    try:
        # Unpublish page
        api_response = api_instance.unpublish_studio_page(studio_page_uid)
        print("The response of StudioPagesApi->unpublish_studio_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesApi->unpublish_studio_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 

### Return type

[**PublishDataset200Response**](PublishDataset200Response.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The action has been performed |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_studio_page**
> StudioPage update_studio_page(studio_page_uid, studio_page=studio_page)

Update page

Update a studio page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.studio_page import StudioPage
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
    api_instance = openapi_client.StudioPagesApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    studio_page = openapi_client.StudioPage() # StudioPage |  (optional)

    try:
        # Update page
        api_response = api_instance.update_studio_page(studio_page_uid, studio_page=studio_page)
        print("The response of StudioPagesApi->update_studio_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesApi->update_studio_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **studio_page** | [**StudioPage**](StudioPage.md)|  | [optional] 

### Return type

[**StudioPage**](StudioPage.md)

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

