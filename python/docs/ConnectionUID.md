# ConnectionUID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The UID of an existing connection to reuse. | 

## Example

```python
from opendatasoft_automation.models.connection_uid import ConnectionUID

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionUID from a JSON string
connection_uid_instance = ConnectionUID.from_json(json)
# print the JSON string representation of the object
print(ConnectionUID.to_json())

# convert the object into a dict
connection_uid_dict = connection_uid_instance.to_dict()
# create an instance of ConnectionUID from a dict
connection_uid_from_dict = ConnectionUID.from_dict(connection_uid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


