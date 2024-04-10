# openapi_client.StudioPagesSecurityApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_studio_page_group_security**](StudioPagesSecurityApi.md#create_studio_page_group_security) | **POST** /studio_pages/{studio_page_uid}/security/groups/ | Create group ruleset
[**create_studio_page_user_security**](StudioPagesSecurityApi.md#create_studio_page_user_security) | **POST** /studio_pages/{studio_page_uid}/security/users/ | Create user ruleset
[**delete_studio_page_group_security**](StudioPagesSecurityApi.md#delete_studio_page_group_security) | **DELETE** /studio_pages/{studio_page_uid}/security/groups/{group_uid}/ | Delete group ruleset
[**delete_studio_page_user_security**](StudioPagesSecurityApi.md#delete_studio_page_user_security) | **DELETE** /studio_pages/{studio_page_uid}/security/users/{username}/ | Delete user ruleset
[**list_studio_page_group_security**](StudioPagesSecurityApi.md#list_studio_page_group_security) | **GET** /studio_pages/{studio_page_uid}/security/groups/ | List group rulesets
[**list_studio_page_user_security**](StudioPagesSecurityApi.md#list_studio_page_user_security) | **GET** /studio_pages/{studio_page_uid}/security/users/ | List user rulesets
[**retrieve_studio_page_group_security**](StudioPagesSecurityApi.md#retrieve_studio_page_group_security) | **GET** /studio_pages/{studio_page_uid}/security/groups/{group_uid}/ | Retrieve group ruleset
[**retrieve_studio_page_user_security**](StudioPagesSecurityApi.md#retrieve_studio_page_user_security) | **GET** /studio_pages/{studio_page_uid}/security/users/{username}/ | Retrieve user ruleset
[**update_studio_page_group_security**](StudioPagesSecurityApi.md#update_studio_page_group_security) | **PUT** /studio_pages/{studio_page_uid}/security/groups/{group_uid}/ | Update group ruleset
[**update_studio_page_user_security**](StudioPagesSecurityApi.md#update_studio_page_user_security) | **PUT** /studio_pages/{studio_page_uid}/security/users/{username}/ | Update user ruleset


# **create_studio_page_group_security**
> GroupSecurity3 create_studio_page_group_security(studio_page_uid, group_security3=group_security3)

Create group ruleset

Create a studio page group level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.group_security3 import GroupSecurity3
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    group_security3 = openapi_client.GroupSecurity3() # GroupSecurity3 |  (optional)

    try:
        # Create group ruleset
        api_response = api_instance.create_studio_page_group_security(studio_page_uid, group_security3=group_security3)
        print("The response of StudioPagesSecurityApi->create_studio_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->create_studio_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **group_security3** | [**GroupSecurity3**](GroupSecurity3.md)|  | [optional] 

### Return type

[**GroupSecurity3**](GroupSecurity3.md)

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

# **create_studio_page_user_security**
> UserSecurity3 create_studio_page_user_security(studio_page_uid, user_security3=user_security3)

Create user ruleset

Create a studio page user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.user_security3 import UserSecurity3
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    user_security3 = openapi_client.UserSecurity3() # UserSecurity3 |  (optional)

    try:
        # Create user ruleset
        api_response = api_instance.create_studio_page_user_security(studio_page_uid, user_security3=user_security3)
        print("The response of StudioPagesSecurityApi->create_studio_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->create_studio_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **user_security3** | [**UserSecurity3**](UserSecurity3.md)|  | [optional] 

### Return type

[**UserSecurity3**](UserSecurity3.md)

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

# **delete_studio_page_group_security**
> delete_studio_page_group_security(studio_page_uid, group_uid)

Delete group ruleset

Delete a studio page group level security ruleset

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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    group_uid = 'group_identifier' # str | 

    try:
        # Delete group ruleset
        api_instance.delete_studio_page_group_security(studio_page_uid, group_uid)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->delete_studio_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
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

# **delete_studio_page_user_security**
> delete_studio_page_user_security(studio_page_uid, username)

Delete user ruleset

Delete a studio page user-level security ruleset

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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    username = 'louise.data' # str | 

    try:
        # Delete user ruleset
        api_instance.delete_studio_page_user_security(studio_page_uid, username)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->delete_studio_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
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

# **list_studio_page_group_security**
> ListStudioPageGroupSecurity200Response list_studio_page_group_security(studio_page_uid, limit=limit, offset=offset)

List group rulesets

List the studio page group level security rulesets

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.list_studio_page_group_security200_response import ListStudioPageGroupSecurity200Response
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List group rulesets
        api_response = api_instance.list_studio_page_group_security(studio_page_uid, limit=limit, offset=offset)
        print("The response of StudioPagesSecurityApi->list_studio_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->list_studio_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListStudioPageGroupSecurity200Response**](ListStudioPageGroupSecurity200Response.md)

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

# **list_studio_page_user_security**
> ListStudioPageUserSecurity200Response list_studio_page_user_security(studio_page_uid, limit=limit, offset=offset)

List user rulesets

List the studio page user-level security rulesets

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.list_studio_page_user_security200_response import ListStudioPageUserSecurity200Response
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List user rulesets
        api_response = api_instance.list_studio_page_user_security(studio_page_uid, limit=limit, offset=offset)
        print("The response of StudioPagesSecurityApi->list_studio_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->list_studio_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListStudioPageUserSecurity200Response**](ListStudioPageUserSecurity200Response.md)

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

# **retrieve_studio_page_group_security**
> GroupSecurity3 retrieve_studio_page_group_security(studio_page_uid, group_uid)

Retrieve group ruleset

Retrieve a studio page group level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.group_security3 import GroupSecurity3
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    group_uid = 'group_identifier' # str | 

    try:
        # Retrieve group ruleset
        api_response = api_instance.retrieve_studio_page_group_security(studio_page_uid, group_uid)
        print("The response of StudioPagesSecurityApi->retrieve_studio_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->retrieve_studio_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **group_uid** | **str**|  | 

### Return type

[**GroupSecurity3**](GroupSecurity3.md)

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

# **retrieve_studio_page_user_security**
> UserSecurity3 retrieve_studio_page_user_security(studio_page_uid, username)

Retrieve user ruleset

Retrieve a studio page user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.user_security3 import UserSecurity3
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    username = 'louise.data' # str | 

    try:
        # Retrieve user ruleset
        api_response = api_instance.retrieve_studio_page_user_security(studio_page_uid, username)
        print("The response of StudioPagesSecurityApi->retrieve_studio_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->retrieve_studio_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**UserSecurity3**](UserSecurity3.md)

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

# **update_studio_page_group_security**
> GroupSecurity3 update_studio_page_group_security(studio_page_uid, group_uid, group_security3=group_security3)

Update group ruleset

Update a studio page group level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.group_security3 import GroupSecurity3
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    group_uid = 'group_identifier' # str | 
    group_security3 = openapi_client.GroupSecurity3() # GroupSecurity3 |  (optional)

    try:
        # Update group ruleset
        api_response = api_instance.update_studio_page_group_security(studio_page_uid, group_uid, group_security3=group_security3)
        print("The response of StudioPagesSecurityApi->update_studio_page_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->update_studio_page_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **group_uid** | **str**|  | 
 **group_security3** | [**GroupSecurity3**](GroupSecurity3.md)|  | [optional] 

### Return type

[**GroupSecurity3**](GroupSecurity3.md)

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

# **update_studio_page_user_security**
> UserSecurity3 update_studio_page_user_security(studio_page_uid, username, user_security3=user_security3)

Update user ruleset

Update a studio page user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.user_security3 import UserSecurity3
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
    api_instance = openapi_client.StudioPagesSecurityApi(api_client)
    studio_page_uid = 'sp_qf2hyt' # str | 
    username = 'louise.data' # str | 
    user_security3 = openapi_client.UserSecurity3() # UserSecurity3 |  (optional)

    try:
        # Update user ruleset
        api_response = api_instance.update_studio_page_user_security(studio_page_uid, username, user_security3=user_security3)
        print("The response of StudioPagesSecurityApi->update_studio_page_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StudioPagesSecurityApi->update_studio_page_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_page_uid** | **str**|  | 
 **username** | **str**|  | 
 **user_security3** | [**UserSecurity3**](UserSecurity3.md)|  | [optional] 

### Return type

[**UserSecurity3**](UserSecurity3.md)

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

