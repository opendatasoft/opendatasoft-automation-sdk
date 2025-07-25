# opendatasoft_automation.CodeEditorPagesApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_code_editor_page**](CodeEditorPagesApi.md#archive_code_editor_page) | **POST** /code_editor_pages/{page_slug}/archive/ | Archive page
[**bulk_delete_code_editor_page**](CodeEditorPagesApi.md#bulk_delete_code_editor_page) | **DELETE** /code_editor_pages/ | Delete multiple pages
[**create_code_editor_page**](CodeEditorPagesApi.md#create_code_editor_page) | **POST** /code_editor_pages/ | Create page
[**delete_code_editor_page**](CodeEditorPagesApi.md#delete_code_editor_page) | **DELETE** /code_editor_pages/{page_slug}/ | Delete page
[**list_code_editor_pages**](CodeEditorPagesApi.md#list_code_editor_pages) | **GET** /code_editor_pages/ | List pages
[**retrieve_code_editor_page**](CodeEditorPagesApi.md#retrieve_code_editor_page) | **GET** /code_editor_pages/{page_slug}/ | Retrieve page
[**unarchive_code_editor_page**](CodeEditorPagesApi.md#unarchive_code_editor_page) | **POST** /code_editor_pages/{page_slug}/unarchive/ | Unarchive page
[**update_code_editor_page**](CodeEditorPagesApi.md#update_code_editor_page) | **PUT** /code_editor_pages/{page_slug}/ | Update page


# **archive_code_editor_page**
> InlineObject3 archive_code_editor_page(page_slug)

Archive page

Archive a code editor page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.inline_object3 import InlineObject3
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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    page_slug = 'page_slug' # str | 

    try:
        # Archive page
        api_response = api_instance.archive_code_editor_page(page_slug)
        print("The response of CodeEditorPagesApi->archive_code_editor_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->archive_code_editor_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 

### Return type

[**InlineObject3**](InlineObject3.md)

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

# **bulk_delete_code_editor_page**
> List[str] bulk_delete_code_editor_page(slug=slug, search=search)

Delete multiple pages

Delete all code editor pages matching the search defined by the `search` and `slug` query parameters.

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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    slug = ['[\"slug1\",\"slug2\"]'] # List[str] | List of page slug to be removed. (optional)
    search = 'My Page Title' # str | A search term to delete matching pages. (optional)

    try:
        # Delete multiple pages
        api_response = api_instance.bulk_delete_code_editor_page(slug=slug, search=search)
        print("The response of CodeEditorPagesApi->bulk_delete_code_editor_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->bulk_delete_code_editor_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | [**List[str]**](str.md)| List of page slug to be removed. | [optional] 
 **search** | **str**| A search term to delete matching pages. | [optional] 

### Return type

**List[str]**

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

# **create_code_editor_page**
> CodeEditorPage create_code_editor_page(code_editor_page=code_editor_page)

Create page

Create a code editor page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.code_editor_page import CodeEditorPage
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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    code_editor_page = opendatasoft_automation.CodeEditorPage() # CodeEditorPage |  (optional)

    try:
        # Create page
        api_response = api_instance.create_code_editor_page(code_editor_page=code_editor_page)
        print("The response of CodeEditorPagesApi->create_code_editor_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->create_code_editor_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code_editor_page** | [**CodeEditorPage**](CodeEditorPage.md)|  | [optional] 

### Return type

[**CodeEditorPage**](CodeEditorPage.md)

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

# **delete_code_editor_page**
> delete_code_editor_page(page_slug)

Delete page

Delete a code editor page

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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    page_slug = 'page_slug' # str | 

    try:
        # Delete page
        api_instance.delete_code_editor_page(page_slug)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->delete_code_editor_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 

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

# **list_code_editor_pages**
> ListCodeEditorPages200Response list_code_editor_pages(limit=limit, offset=offset)

List pages

List code editor pages

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_code_editor_pages200_response import ListCodeEditorPages200Response
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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List pages
        api_response = api_instance.list_code_editor_pages(limit=limit, offset=offset)
        print("The response of CodeEditorPagesApi->list_code_editor_pages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->list_code_editor_pages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListCodeEditorPages200Response**](ListCodeEditorPages200Response.md)

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

# **retrieve_code_editor_page**
> CodeEditorPage retrieve_code_editor_page(page_slug)

Retrieve page

Retrieve a code editor page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.code_editor_page import CodeEditorPage
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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    page_slug = 'page_slug' # str | 

    try:
        # Retrieve page
        api_response = api_instance.retrieve_code_editor_page(page_slug)
        print("The response of CodeEditorPagesApi->retrieve_code_editor_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->retrieve_code_editor_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 

### Return type

[**CodeEditorPage**](CodeEditorPage.md)

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

# **unarchive_code_editor_page**
> InlineObject3 unarchive_code_editor_page(page_slug)

Unarchive page

Unarchive a code editor page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.inline_object3 import InlineObject3
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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    page_slug = 'page_slug' # str | 

    try:
        # Unarchive page
        api_response = api_instance.unarchive_code_editor_page(page_slug)
        print("The response of CodeEditorPagesApi->unarchive_code_editor_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->unarchive_code_editor_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 

### Return type

[**InlineObject3**](InlineObject3.md)

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

# **update_code_editor_page**
> CodeEditorPage update_code_editor_page(page_slug, code_editor_page=code_editor_page)

Update page

Update a code editor page

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.code_editor_page import CodeEditorPage
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
    api_instance = opendatasoft_automation.CodeEditorPagesApi(api_client)
    page_slug = 'page_slug' # str | 
    code_editor_page = opendatasoft_automation.CodeEditorPage() # CodeEditorPage |  (optional)

    try:
        # Update page
        api_response = api_instance.update_code_editor_page(page_slug, code_editor_page=code_editor_page)
        print("The response of CodeEditorPagesApi->update_code_editor_page:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesApi->update_code_editor_page: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **code_editor_page** | [**CodeEditorPage**](CodeEditorPage.md)|  | [optional] 

### Return type

[**CodeEditorPage**](CodeEditorPage.md)

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

