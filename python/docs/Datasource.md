# Datasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from opendatasoft_automation.models.datasource import Datasource

# TODO update the JSON string below
json = "{}"
# create an instance of Datasource from a JSON string
datasource_instance = Datasource.from_json(json)
# print the JSON string representation of the object
print(Datasource.to_json())

# convert the object into a dict
datasource_dict = datasource_instance.to_dict()
# create an instance of Datasource from a dict
datasource_from_dict = Datasource.from_dict(datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


