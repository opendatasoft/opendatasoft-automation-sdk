# Connection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] [readonly] 
**type** | **str** |  | 
**is_reusable** | **bool** | Defines if the connection can be reused across multiple datasets | [optional] 
**can_reuse** | **bool** | Defines if the current user has the permission to reuse this connection | [optional] [readonly] 
**can_manage** | **bool** | Defines if the current user has the permission to manage this connection | [optional] [readonly] 
**dataset_count** | **float** | Number of datasets using this connection | [optional] [readonly] 
**user_count** | **float** | Number of users with explicit access to this connection | [optional] [readonly] 
**group_count** | **float** | Number of user groups with explicit access to this connection | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.connection import Connection

# TODO update the JSON string below
json = "{}"
# create an instance of Connection from a JSON string
connection_instance = Connection.from_json(json)
# print the JSON string representation of the object
print(Connection.to_json())

# convert the object into a dict
connection_dict = connection_instance.to_dict()
# create an instance of Connection from a dict
connection_from_dict = Connection.from_dict(connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


