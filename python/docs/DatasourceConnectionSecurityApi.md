# opendatasoft_automation.DatasourceConnectionSecurityApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_datasource_connection_group_security**](DatasourceConnectionSecurityApi.md#create_datasource_connection_group_security) | **POST** /datasource_connections/{connection_uid}/security/groups/ | Create group ruleset
[**create_datasource_connection_user_security**](DatasourceConnectionSecurityApi.md#create_datasource_connection_user_security) | **POST** /datasource_connections/{connection_uid}/security/users/ | Create user ruleset
[**delete_datasource_connection_group_security**](DatasourceConnectionSecurityApi.md#delete_datasource_connection_group_security) | **DELETE** /datasource_connections/{connection_uid}/security/groups/{group_uid}/ | Delete group ruleset
[**delete_datasource_connection_user_security**](DatasourceConnectionSecurityApi.md#delete_datasource_connection_user_security) | **DELETE** /datasource_connections/{connection_uid}/security/users/{username}/ | Delete user ruleset
[**list_datasource_connection_group_security**](DatasourceConnectionSecurityApi.md#list_datasource_connection_group_security) | **GET** /datasource_connections/{connection_uid}/security/groups/ | List group rulesets
[**list_datasource_connection_user_security**](DatasourceConnectionSecurityApi.md#list_datasource_connection_user_security) | **GET** /datasource_connections/{connection_uid}/security/users/ | List user rulesets
[**retrieve_datasource_connection_group_security**](DatasourceConnectionSecurityApi.md#retrieve_datasource_connection_group_security) | **GET** /datasource_connections/{connection_uid}/security/groups/{group_uid}/ | Retrieve group ruleset
[**retrieve_datasource_connection_user_security**](DatasourceConnectionSecurityApi.md#retrieve_datasource_connection_user_security) | **GET** /datasource_connections/{connection_uid}/security/users/{username}/ | Retrieve user ruleset
[**update_datasource_connection_group_security**](DatasourceConnectionSecurityApi.md#update_datasource_connection_group_security) | **PUT** /datasource_connections/{connection_uid}/security/groups/{group_uid}/ | Update group ruleset
[**update_datasource_connection_user_security**](DatasourceConnectionSecurityApi.md#update_datasource_connection_user_security) | **PUT** /datasource_connections/{connection_uid}/security/users/{username}/ | Update user ruleset


# **create_datasource_connection_group_security**
> GroupSecurity create_datasource_connection_group_security(connection_uid, group_security=group_security)

Create group ruleset

Create a datasource connection group-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.group_security import GroupSecurity
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    group_security = opendatasoft_automation.GroupSecurity() # GroupSecurity |  (optional)

    try:
        # Create group ruleset
        api_response = api_instance.create_datasource_connection_group_security(connection_uid, group_security=group_security)
        print("The response of DatasourceConnectionSecurityApi->create_datasource_connection_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->create_datasource_connection_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **group_security** | [**GroupSecurity**](GroupSecurity.md)|  | [optional] 

### Return type

[**GroupSecurity**](GroupSecurity.md)

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

# **create_datasource_connection_user_security**
> UserSecurity create_datasource_connection_user_security(connection_uid, user_security=user_security)

Create user ruleset

Create a datasource connection user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user_security import UserSecurity
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    user_security = opendatasoft_automation.UserSecurity() # UserSecurity |  (optional)

    try:
        # Create user ruleset
        api_response = api_instance.create_datasource_connection_user_security(connection_uid, user_security=user_security)
        print("The response of DatasourceConnectionSecurityApi->create_datasource_connection_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->create_datasource_connection_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **user_security** | [**UserSecurity**](UserSecurity.md)|  | [optional] 

### Return type

[**UserSecurity**](UserSecurity.md)

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

# **delete_datasource_connection_group_security**
> delete_datasource_connection_group_security(connection_uid, group_uid)

Delete group ruleset

Delete a datasource connection group-level security ruleset

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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    group_uid = 'group_identifier' # str | 

    try:
        # Delete group ruleset
        api_instance.delete_datasource_connection_group_security(connection_uid, group_uid)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->delete_datasource_connection_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
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

# **delete_datasource_connection_user_security**
> delete_datasource_connection_user_security(connection_uid, username)

Delete user ruleset

Delete a datasource connection user-level security ruleset

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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    username = 'louise.data' # str | 

    try:
        # Delete user ruleset
        api_instance.delete_datasource_connection_user_security(connection_uid, username)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->delete_datasource_connection_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
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

# **list_datasource_connection_group_security**
> ListDatasourceConnectionGroupSecurity200Response list_datasource_connection_group_security(connection_uid, limit=limit, offset=offset)

List group rulesets

List the datasource connection group-level security rulesets

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_datasource_connection_group_security200_response import ListDatasourceConnectionGroupSecurity200Response
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List group rulesets
        api_response = api_instance.list_datasource_connection_group_security(connection_uid, limit=limit, offset=offset)
        print("The response of DatasourceConnectionSecurityApi->list_datasource_connection_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->list_datasource_connection_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListDatasourceConnectionGroupSecurity200Response**](ListDatasourceConnectionGroupSecurity200Response.md)

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

# **list_datasource_connection_user_security**
> ListDatasourceConnectionUserSecurity200Response list_datasource_connection_user_security(connection_uid, limit=limit, offset=offset)

List user rulesets

List the datasource connection user-level security rulesets

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.list_datasource_connection_user_security200_response import ListDatasourceConnectionUserSecurity200Response
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List user rulesets
        api_response = api_instance.list_datasource_connection_user_security(connection_uid, limit=limit, offset=offset)
        print("The response of DatasourceConnectionSecurityApi->list_datasource_connection_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->list_datasource_connection_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**ListDatasourceConnectionUserSecurity200Response**](ListDatasourceConnectionUserSecurity200Response.md)

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

# **retrieve_datasource_connection_group_security**
> GroupSecurity retrieve_datasource_connection_group_security(connection_uid, group_uid)

Retrieve group ruleset

Retrieve a datasource connection group-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.group_security import GroupSecurity
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    group_uid = 'group_identifier' # str | 

    try:
        # Retrieve group ruleset
        api_response = api_instance.retrieve_datasource_connection_group_security(connection_uid, group_uid)
        print("The response of DatasourceConnectionSecurityApi->retrieve_datasource_connection_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->retrieve_datasource_connection_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **group_uid** | **str**|  | 

### Return type

[**GroupSecurity**](GroupSecurity.md)

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

# **retrieve_datasource_connection_user_security**
> UserSecurity retrieve_datasource_connection_user_security(connection_uid, username)

Retrieve user ruleset

Retrieve a datasource connection user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user_security import UserSecurity
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    username = 'louise.data' # str | 

    try:
        # Retrieve user ruleset
        api_response = api_instance.retrieve_datasource_connection_user_security(connection_uid, username)
        print("The response of DatasourceConnectionSecurityApi->retrieve_datasource_connection_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->retrieve_datasource_connection_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **username** | **str**|  | 

### Return type

[**UserSecurity**](UserSecurity.md)

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

# **update_datasource_connection_group_security**
> GroupSecurity update_datasource_connection_group_security(connection_uid, group_uid, group_security=group_security)

Update group ruleset

Update a datasource connection group-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.group_security import GroupSecurity
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    group_uid = 'group_identifier' # str | 
    group_security = opendatasoft_automation.GroupSecurity() # GroupSecurity |  (optional)

    try:
        # Update group ruleset
        api_response = api_instance.update_datasource_connection_group_security(connection_uid, group_uid, group_security=group_security)
        print("The response of DatasourceConnectionSecurityApi->update_datasource_connection_group_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->update_datasource_connection_group_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **group_uid** | **str**|  | 
 **group_security** | [**GroupSecurity**](GroupSecurity.md)|  | [optional] 

### Return type

[**GroupSecurity**](GroupSecurity.md)

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

# **update_datasource_connection_user_security**
> UserSecurity update_datasource_connection_user_security(connection_uid, username, user_security=user_security)

Update user ruleset

Update a datasource connection user-level security ruleset

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user_security import UserSecurity
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
    api_instance = opendatasoft_automation.DatasourceConnectionSecurityApi(api_client)
    connection_uid = 'co_qf2hyt' # str | 
    username = 'louise.data' # str | 
    user_security = opendatasoft_automation.UserSecurity() # UserSecurity |  (optional)

    try:
        # Update user ruleset
        api_response = api_instance.update_datasource_connection_user_security(connection_uid, username, user_security=user_security)
        print("The response of DatasourceConnectionSecurityApi->update_datasource_connection_user_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatasourceConnectionSecurityApi->update_datasource_connection_user_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_uid** | **str**|  | 
 **username** | **str**|  | 
 **user_security** | [**UserSecurity**](UserSecurity.md)|  | [optional] 

### Return type

[**UserSecurity**](UserSecurity.md)

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

