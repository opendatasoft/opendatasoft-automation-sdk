# ListDatasourceConnectionGroupSecurity200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_count** | **int** |  | [optional] 
**next** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**results** | [**List[GroupSecurity]**](GroupSecurity.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.list_datasource_connection_group_security200_response import ListDatasourceConnectionGroupSecurity200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatasourceConnectionGroupSecurity200Response from a JSON string
list_datasource_connection_group_security200_response_instance = ListDatasourceConnectionGroupSecurity200Response.from_json(json)
# print the JSON string representation of the object
print(ListDatasourceConnectionGroupSecurity200Response.to_json())

# convert the object into a dict
list_datasource_connection_group_security200_response_dict = list_datasource_connection_group_security200_response_instance.to_dict()
# create an instance of ListDatasourceConnectionGroupSecurity200Response from a dict
list_datasource_connection_group_security200_response_from_dict = ListDatasourceConnectionGroupSecurity200Response.from_dict(list_datasource_connection_group_security200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


