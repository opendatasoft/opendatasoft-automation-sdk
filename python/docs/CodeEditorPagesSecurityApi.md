# opendatasoft_automation.CodeEditorPagesSecurityApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_code_editor_page_group_security**](CodeEditorPagesSecurityApi.md#create_code_editor_page_group_security) | **POST** /code_editor_pages/{page_slug}/security/groups/ | Create group ruleset
[**create_code_editor_page_user_security**](CodeEditorPagesSecurityApi.md#create_code_editor_page_user_security) | **POST** /code_editor_pages/{page_slug}/security/users/ | Create user ruleset
[**delete_code_editor_page_group_security**](CodeEditorPagesSecurityApi.md#delete_code_editor_page_group_security) | **DELETE** /code_editor_pages/{page_slug}/security/groups/{group_uid}/ | Delete group ruleset
[**delete_code_editor_page_user_security**](CodeEditorPagesSecurityApi.md#delete_code_editor_page_user_security) | **DELETE** /code_editor_pages/{page_slug}/security/users/{username}/ | Delete user ruleset
[**list_code_editor_page_group_security**](CodeEditorPagesSecurityApi.md#list_code_editor_page_group_security) | **GET** /code_editor_pages/{page_slug}/security/groups/ | List group rulesets
[**list_code_editor_page_user_security**](CodeEditorPagesSecurityApi.md#list_code_editor_page_user_security) | **GET** /code_editor_pages/{page_slug}/security/users/ | List user rulesets
[**retrieve_code_editor_page_group_security**](CodeEditorPagesSecurityApi.md#retrieve_code_editor_page_group_security) | **GET** /code_editor_pages/{page_slug}/security/groups/{group_uid}/ | Retrieve group ruleset
[**retrieve_code_editor_page_user_security**](CodeEditorPagesSecurityApi.md#retrieve_code_editor_page_user_security) | **GET** /code_editor_pages/{page_slug}/security/users/{username}/ | Retrieve user ruleset
[**update_code_editor_page_group_security**](CodeEditorPagesSecurityApi.md#update_code_editor_page_group_security) | **PUT** /code_editor_pages/{page_slug}/security/groups/{group_uid}/ | Update group ruleset
[**update_code_editor_page_user_security**](CodeEditorPagesSecurityApi.md#update_code_editor_page_user_security) | **PUT** /code_editor_pages/{page_slug}/security/users/{username}/ | Update user ruleset


# **create_code_editor_page_group_security**
> GroupSecurity2 create_code_editor_page_group_security(page_slug, group_security2=group_security2)

Create group ruleset

Create a code editor page group level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.group_security2 import GroupSecurity2
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    group_security2 = opendatasoft_automation.GroupSecurity2() # GroupSecurity2 |  (optional)

    try:
        # Create group ruleset
        api_response = api_instance.create_code_editor_page_group_security(page_slug, group_security2=group_security2)
        print("The response of CodeEditorPagesSecurityApi->create_code_editor_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->create_code_editor_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **group_security2** | [**GroupSecurity2**](GroupSecurity2.md)|  | [optional] 

### Return type

[**GroupSecurity2**](GroupSecurity2.md)

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

# **create_code_editor_page_user_security**
> UserSecurity2 create_code_editor_page_user_security(page_slug, user_security2=user_security2)

Create user ruleset

Create a code editor page user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user_security2 import UserSecurity2
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    user_security2 = opendatasoft_automation.UserSecurity2() # UserSecurity2 |  (optional)

    try:
        # Create user ruleset
        api_response = api_instance.create_code_editor_page_user_security(page_slug, user_security2=user_security2)
        print("The response of CodeEditorPagesSecurityApi->create_code_editor_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->create_code_editor_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **user_security2** | [**UserSecurity2**](UserSecurity2.md)|  | [optional] 

### Return type

[**UserSecurity2**](UserSecurity2.md)

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

# **delete_code_editor_page_group_security**
> delete_code_editor_page_group_security(page_slug, group_uid)

Delete group ruleset

Delete a code editor page group level security ruleset

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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    group_uid = 'group_identifier' # str | 

    try:
        # Delete group ruleset
        api_instance.delete_code_editor_page_group_security(page_slug, group_uid)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->delete_code_editor_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **group_uid** | **str**|  | 

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

# **delete_code_editor_page_user_security**
> delete_code_editor_page_user_security(page_slug, username)

Delete user ruleset

Delete a code editor page user-level security ruleset

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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    username = 'louise.data' # str | 

    try:
        # Delete user ruleset
        api_instance.delete_code_editor_page_user_security(page_slug, username)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->delete_code_editor_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **username** | **str**|  | 

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

# **list_code_editor_page_group_security**
> ListCodeEditorPageGroupSecurity200Response list_code_editor_page_group_security(page_slug, limit=limit, offset=offset)

List group rulesets

List the code editor page group level security rulesets

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_code_editor_page_group_security200_response import ListCodeEditorPageGroupSecurity200Response
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List group rulesets
        api_response = api_instance.list_code_editor_page_group_security(page_slug, limit=limit, offset=offset)
        print("The response of CodeEditorPagesSecurityApi->list_code_editor_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->list_code_editor_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListCodeEditorPageGroupSecurity200Response**](ListCodeEditorPageGroupSecurity200Response.md)

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

# **list_code_editor_page_user_security**
> ListCodeEditorPageUserSecurity200Response list_code_editor_page_user_security(page_slug, limit=limit, offset=offset)

List user rulesets

List the code editor page user-level permissions

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_code_editor_page_user_security200_response import ListCodeEditorPageUserSecurity200Response
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List user rulesets
        api_response = api_instance.list_code_editor_page_user_security(page_slug, limit=limit, offset=offset)
        print("The response of CodeEditorPagesSecurityApi->list_code_editor_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->list_code_editor_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListCodeEditorPageUserSecurity200Response**](ListCodeEditorPageUserSecurity200Response.md)

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

# **retrieve_code_editor_page_group_security**
> GroupSecurity2 retrieve_code_editor_page_group_security(page_slug, group_uid)

Retrieve group ruleset

Retrieve a code editor page group level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.group_security2 import GroupSecurity2
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    group_uid = 'group_identifier' # str | 

    try:
        # Retrieve group ruleset
        api_response = api_instance.retrieve_code_editor_page_group_security(page_slug, group_uid)
        print("The response of CodeEditorPagesSecurityApi->retrieve_code_editor_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->retrieve_code_editor_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **group_uid** | **str**|  | 

### Return type

[**GroupSecurity2**](GroupSecurity2.md)

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

# **retrieve_code_editor_page_user_security**
> UserSecurity2 retrieve_code_editor_page_user_security(page_slug, username)

Retrieve user ruleset

Retrieve a code editor page user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user_security2 import UserSecurity2
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    username = 'louise.data' # str | 

    try:
        # Retrieve user ruleset
        api_response = api_instance.retrieve_code_editor_page_user_security(page_slug, username)
        print("The response of CodeEditorPagesSecurityApi->retrieve_code_editor_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->retrieve_code_editor_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**UserSecurity2**](UserSecurity2.md)

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

# **update_code_editor_page_group_security**
> GroupSecurity2 update_code_editor_page_group_security(page_slug, group_uid, group_security2=group_security2)

Update group ruleset

Update a code editor page group level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.group_security2 import GroupSecurity2
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    group_uid = 'group_identifier' # str | 
    group_security2 = opendatasoft_automation.GroupSecurity2() # GroupSecurity2 |  (optional)

    try:
        # Update group ruleset
        api_response = api_instance.update_code_editor_page_group_security(page_slug, group_uid, group_security2=group_security2)
        print("The response of CodeEditorPagesSecurityApi->update_code_editor_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->update_code_editor_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **group_uid** | **str**|  | 
 **group_security2** | [**GroupSecurity2**](GroupSecurity2.md)|  | [optional] 

### Return type

[**GroupSecurity2**](GroupSecurity2.md)

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

# **update_code_editor_page_user_security**
> UserSecurity2 update_code_editor_page_user_security(page_slug, username, user_security2=user_security2)

Update user ruleset

Update a code editor page user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user_security2 import UserSecurity2
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
    api_instance = opendatasoft_automation.CodeEditorPagesSecurityApi(api_client)
    page_slug = 'page_slug' # str | 
    username = 'louise.data' # str | 
    user_security2 = opendatasoft_automation.UserSecurity2() # UserSecurity2 |  (optional)

    try:
        # Update user ruleset
        api_response = api_instance.update_code_editor_page_user_security(page_slug, username, user_security2=user_security2)
        print("The response of CodeEditorPagesSecurityApi->update_code_editor_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CodeEditorPagesSecurityApi->update_code_editor_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_slug** | **str**|  | 
 **username** | **str**|  | 
 **user_security2** | [**UserSecurity2**](UserSecurity2.md)|  | [optional] 

### Return type

[**UserSecurity2**](UserSecurity2.md)

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

