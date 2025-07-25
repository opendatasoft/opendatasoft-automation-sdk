# opendatasoft_automation.UsersApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /users/{username}/ | Delete user
[**get_user**](UsersApi.md#get_user) | **GET** /users/{username}/ | Retrieve user
[**get_users**](UsersApi.md#get_users) | **GET** /users/ | List users
[**invite_users**](UsersApi.md#invite_users) | **POST** /users/invite/ | Invite users
[**provision_users**](UsersApi.md#provision_users) | **POST** /users/provision/ | Provision users
[**update_user**](UsersApi.md#update_user) | **PUT** /users/{username}/ | Update user
[**users_export**](UsersApi.md#users_export) | **GET** /users/export/ | Export users


# **delete_user**
> delete_user(username)

Delete user

Removes the requested user from the domain. If the user is the only domain administrator left, the call will fail and an error specifying that the removal of the only domain administrator is not allowed will be returned.

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
    api_instance = opendatasoft_automation.UsersApi(api_client)
    username = 'louise.data' # str | 

    try:
        # Delete user
        api_instance.delete_user(username)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **get_user**
> User get_user(username, expand=expand)

Retrieve user

Retrieve user

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user import User
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
    api_instance = opendatasoft_automation.UsersApi(api_client)
    username = 'louise.data' # str | 
    expand = 'groups' # str | The list of fields to expand. (optional)

    try:
        # Retrieve user
        api_response = api_instance.get_user(username, expand=expand)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **expand** | **str**| The list of fields to expand. | [optional] 

### Return type

[**User**](User.md)

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

# **get_users**
> GetUsers200Response get_users(search=search, sort=sort, permissions=permissions, all_permissions=all_permissions, limit=limit, offset=offset)

List users

List users

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.get_users200_response import GetUsers200Response
from opendatasoft_automation.models.permission import Permission
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
    api_instance = opendatasoft_automation.UsersApi(api_client)
    search = 'alice' # str | full-text search among username, first name, last name and email (optional)
    sort = ['sort_example'] # List[str] | sort results according to username, first name or last_name (optional)
    permissions = [opendatasoft_automation.Permission()] # List[Permission] | filter according to permissions granted directly to the users (optional)
    all_permissions = [opendatasoft_automation.Permission()] # List[Permission] | filter according to permissions, whether granted directly or via a group (optional)
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List users
        api_response = api_instance.get_users(search=search, sort=sort, permissions=permissions, all_permissions=all_permissions, limit=limit, offset=offset)
        print("The response of UsersApi->get_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| full-text search among username, first name, last name and email | [optional] 
 **sort** | [**List[str]**](str.md)| sort results according to username, first name or last_name | [optional] 
 **permissions** | [**List[Permission]**](Permission.md)| filter according to permissions granted directly to the users | [optional] 
 **all_permissions** | [**List[Permission]**](Permission.md)| filter according to permissions, whether granted directly or via a group | [optional] 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**GetUsers200Response**](GetUsers200Response.md)

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

# **invite_users**
> Dict[str, InviteUsers200ResponseValue] invite_users(user=user)

Invite users

This bulk endpoint creates an account for each of the given users and sends them an email so that they can log in. Each item in the payload must contain at least an email address, and may contain additional fields, such as groups and permissions. Returned body is an object in which each key is the number of the requested user in the payload ("0" = first user) and value contains a status_code ("success" or "error") and either "data" corresponding to the user or "error" describing the error.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.invite_users200_response_value import InviteUsers200ResponseValue
from opendatasoft_automation.models.user import User
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
    api_instance = opendatasoft_automation.UsersApi(api_client)
    user = [opendatasoft_automation.User()] # List[User] |  (optional)

    try:
        # Invite users
        api_response = api_instance.invite_users(user=user)
        print("The response of UsersApi->invite_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->invite_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**List[User]**](User.md)|  | [optional] 

### Return type

[**Dict[str, InviteUsers200ResponseValue]**](InviteUsers200ResponseValue.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_users**
> Dict[str, InviteUsers200ResponseValue] provision_users(provision_users_request=provision_users_request)

Provision users

This bulk endpoint creates an account for each of the given users using the given identity provider. Each item in the payload must contain at least an identity provider, and may contain additional fields, such as groups and permissions. Returned body is an object in which each key is the number of the requested user in the payload ("0" = first user) and value contains a status_code ("success" or "error") and either "data" corresponding to the user or "error" describing the error.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.invite_users200_response_value import InviteUsers200ResponseValue
from opendatasoft_automation.models.provision_users_request import ProvisionUsersRequest
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
    api_instance = opendatasoft_automation.UsersApi(api_client)
    provision_users_request = opendatasoft_automation.ProvisionUsersRequest() # ProvisionUsersRequest |  (optional)

    try:
        # Provision users
        api_response = api_instance.provision_users(provision_users_request=provision_users_request)
        print("The response of UsersApi->provision_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->provision_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provision_users_request** | [**ProvisionUsersRequest**](ProvisionUsersRequest.md)|  | [optional] 

### Return type

[**Dict[str, InviteUsers200ResponseValue]**](InviteUsers200ResponseValue.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(username, user=user)

Update user

Updates a user properties

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user import User
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
    api_instance = opendatasoft_automation.UsersApi(api_client)
    username = 'louise.data' # str | 
    user = opendatasoft_automation.User() # User |  (optional)

    try:
        # Update user
        api_response = api_instance.update_user(username, user=user)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

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

# **users_export**
> List[User] users_export(subdomains=subdomains, delimiter=delimiter)

Export users

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import opendatasoft_automation
from opendatasoft_automation.models.user import User
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
    api_instance = opendatasoft_automation.UsersApi(api_client)
    subdomains = 'subdomains_example' # str | Subdomains to include in the CSV (requires the permission to export subdomains) (optional)
    delimiter = ',' # str | Field separator (optional) (default to ',')

    try:
        # Export users
        api_response = api_instance.users_export(subdomains=subdomains, delimiter=delimiter)
        print("The response of UsersApi->users_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subdomains** | **str**| Subdomains to include in the CSV (requires the permission to export subdomains) | [optional] 
 **delimiter** | **str**| Field separator | [optional] [default to &#39;,&#39;]

### Return type

[**List[User]**](User.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

