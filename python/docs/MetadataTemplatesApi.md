# openapi_client.MetadataTemplatesApi

All URIs are relative to *https://documentation-resources.opendatasoft.com/api/automation/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_metadata_template**](MetadataTemplatesApi.md#create_metadata_template) | **POST** /metadata/templates/ | Create metadata template
[**delete_metadata_template**](MetadataTemplatesApi.md#delete_metadata_template) | **DELETE** /metadata/templates/{template_name}/ | Delete a metadata template
[**get_metadata_field_values_suggestion**](MetadataTemplatesApi.md#get_metadata_field_values_suggestion) | **GET** /metadata/templates/{template_name}/fields/{template_field_name}/suggest/ | Suggest field choices
[**get_metadata_fields_list**](MetadataTemplatesApi.md#get_metadata_fields_list) | **GET** /metadata/templates/{template_name}/fields/ | List template&#39;s fields
[**get_metadata_fields_retrieve**](MetadataTemplatesApi.md#get_metadata_fields_retrieve) | **GET** /metadata/templates/{template_name}/fields/{template_field_name}/ | Retrieve metadata template field
[**list_metadata_templates**](MetadataTemplatesApi.md#list_metadata_templates) | **GET** /metadata/templates/ | List metadata templates
[**retrieve_metadata_templates**](MetadataTemplatesApi.md#retrieve_metadata_templates) | **GET** /metadata/templates/{template_name}/ | Retrieve a metadata template
[**update_metadata_template**](MetadataTemplatesApi.md#update_metadata_template) | **PUT** /metadata/templates/{template_name}/ | Update metadata template


# **create_metadata_template**
> CreatableOrEditableMetadataTemplate create_metadata_template(creatable_or_editable_metadata_template=creatable_or_editable_metadata_template)

Create metadata template

You can only create `basic` and `admin` metadata templates.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.creatable_or_editable_metadata_template import CreatableOrEditableMetadataTemplate
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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    creatable_or_editable_metadata_template = openapi_client.CreatableOrEditableMetadataTemplate() # CreatableOrEditableMetadataTemplate |  (optional)

    try:
        # Create metadata template
        api_response = api_instance.create_metadata_template(creatable_or_editable_metadata_template=creatable_or_editable_metadata_template)
        print("The response of MetadataTemplatesApi->create_metadata_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->create_metadata_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **creatable_or_editable_metadata_template** | [**CreatableOrEditableMetadataTemplate**](CreatableOrEditableMetadataTemplate.md)|  | [optional] 

### Return type

[**CreatableOrEditableMetadataTemplate**](CreatableOrEditableMetadataTemplate.md)

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

# **delete_metadata_template**
> delete_metadata_template(template_name)

Delete a metadata template

Only non-system templates of type `basic` or `admin` can be removed.

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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    template_name = 'template_name' # str | Metadata template name

    try:
        # Delete a metadata template
        api_instance.delete_metadata_template(template_name)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->delete_metadata_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| Metadata template name | 

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

# **get_metadata_field_values_suggestion**
> MetadataTemplateFieldSuggestions get_metadata_field_values_suggestion(template_name, template_field_name, query, count=count)

Suggest field choices

List suggestions (\"choices\") for the provided template field name.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.metadata_template_field_suggestions import MetadataTemplateFieldSuggestions
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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    template_name = 'template_name' # str | Metadata template name
    template_field_name = 'field_name' # str | Metadata template field name
    query = 'query_example' # str | The query to perform to the service providing the suggestions. Most likely, it will be a prefix of what you're looking for. 
    count = 3.4 # float | Number of results which will be provided in the response. (optional)

    try:
        # Suggest field choices
        api_response = api_instance.get_metadata_field_values_suggestion(template_name, template_field_name, query, count=count)
        print("The response of MetadataTemplatesApi->get_metadata_field_values_suggestion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->get_metadata_field_values_suggestion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| Metadata template name | 
 **template_field_name** | **str**| Metadata template field name | 
 **query** | **str**| The query to perform to the service providing the suggestions. Most likely, it will be a prefix of what you&#39;re looking for.  | 
 **count** | **float**| Number of results which will be provided in the response. | [optional] 

### Return type

[**MetadataTemplateFieldSuggestions**](MetadataTemplateFieldSuggestions.md)

### Authorization

[HeaderAPIKey](../README.md#HeaderAPIKey), [QueryAPIKey](../README.md#QueryAPIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Validation error |  -  |
**404** | Not found |  -  |
**0** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_fields_list**
> GetMetadataFieldsList200Response get_metadata_fields_list(template_name, limit=limit, offset=offset)

List template's fields

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.get_metadata_fields_list200_response import GetMetadataFieldsList200Response
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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    template_name = 'template_name' # str | Metadata template name
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)

    try:
        # List template's fields
        api_response = api_instance.get_metadata_fields_list(template_name, limit=limit, offset=offset)
        print("The response of MetadataTemplatesApi->get_metadata_fields_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->get_metadata_fields_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| Metadata template name | 
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 

### Return type

[**GetMetadataFieldsList200Response**](GetMetadataFieldsList200Response.md)

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

# **get_metadata_fields_retrieve**
> MetadataTemplateField get_metadata_fields_retrieve(template_name, template_field_name)

Retrieve metadata template field

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.metadata_template_field import MetadataTemplateField
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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    template_name = 'template_name' # str | Metadata template name
    template_field_name = 'field_name' # str | Metadata template field name

    try:
        # Retrieve metadata template field
        api_response = api_instance.get_metadata_fields_retrieve(template_name, template_field_name)
        print("The response of MetadataTemplatesApi->get_metadata_fields_retrieve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->get_metadata_fields_retrieve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| Metadata template name | 
 **template_field_name** | **str**| Metadata template field name | 

### Return type

[**MetadataTemplateField**](MetadataTemplateField.md)

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

# **list_metadata_templates**
> ListMetadataTemplates200Response list_metadata_templates(limit=limit, offset=offset, is_active=is_active, type=type)

List metadata templates

List all metadata templates of the current domain.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.list_metadata_templates200_response import ListMetadataTemplates200Response
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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    limit = 20 # float | The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \"limit\" set to 0 to get only the metadata (\"results\" property will contain an empty array). (optional) (default to 20)
    offset = 0 # float | The number of results to skip before beginning the listing in case of a paginated response (optional)
    is_active = True # bool | If provided and True then it will list only all activated templates. If provided and False it lists non-activated templates. If not provided then it will lists both activated and non-activated templates.  (optional)
    type = 'type_example' # str |  (optional)

    try:
        # List metadata templates
        api_response = api_instance.list_metadata_templates(limit=limit, offset=offset, is_active=is_active, type=type)
        print("The response of MetadataTemplatesApi->list_metadata_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->list_metadata_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| The maximum number of results returned by the API when the response is paginated. Tip: You can make a request with the parameter \&quot;limit\&quot; set to 0 to get only the metadata (\&quot;results\&quot; property will contain an empty array). | [optional] [default to 20]
 **offset** | **float**| The number of results to skip before beginning the listing in case of a paginated response | [optional] 
 **is_active** | **bool**| If provided and True then it will list only all activated templates. If provided and False it lists non-activated templates. If not provided then it will lists both activated and non-activated templates.  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**ListMetadataTemplates200Response**](ListMetadataTemplates200Response.md)

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

# **retrieve_metadata_templates**
> MetadataTemplate retrieve_metadata_templates(template_name)

Retrieve a metadata template

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.metadata_template import MetadataTemplate
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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    template_name = 'template_name' # str | Metadata template name

    try:
        # Retrieve a metadata template
        api_response = api_instance.retrieve_metadata_templates(template_name)
        print("The response of MetadataTemplatesApi->retrieve_metadata_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->retrieve_metadata_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| Metadata template name | 

### Return type

[**MetadataTemplate**](MetadataTemplate.md)

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

# **update_metadata_template**
> CreatableOrEditableMetadataTemplate update_metadata_template(template_name, creatable_or_editable_metadata_template=creatable_or_editable_metadata_template)

Update metadata template

Only non-system templates of type `basic` and `admin` can be fully editable. Other templates may be enabled. Templates with `is_system=true` and `is_always_active=true` are exceptions and can't be disabled.

### Example

* Api Key Authentication (HeaderAPIKey):
* Api Key Authentication (QueryAPIKey):

```python
import openapi_client
from openapi_client.models.creatable_or_editable_metadata_template import CreatableOrEditableMetadataTemplate
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
    api_instance = openapi_client.MetadataTemplatesApi(api_client)
    template_name = 'template_name' # str | Metadata template name
    creatable_or_editable_metadata_template = openapi_client.CreatableOrEditableMetadataTemplate() # CreatableOrEditableMetadataTemplate |  (optional)

    try:
        # Update metadata template
        api_response = api_instance.update_metadata_template(template_name, creatable_or_editable_metadata_template=creatable_or_editable_metadata_template)
        print("The response of MetadataTemplatesApi->update_metadata_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetadataTemplatesApi->update_metadata_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_name** | **str**| Metadata template name | 
 **creatable_or_editable_metadata_template** | [**CreatableOrEditableMetadataTemplate**](CreatableOrEditableMetadataTemplate.md)|  | [optional] 

### Return type

[**CreatableOrEditableMetadataTemplate**](CreatableOrEditableMetadataTemplate.md)

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

