# DatasetGroupSecurity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**security** | [**DatasetSecurity**](DatasetSecurity.md) |  | [optional] 
**permissions** | **List[str]** | List of special permissions granted to the target. | [optional] 
**group** | [**DatasetGroupSecurityGroup**](DatasetGroupSecurityGroup.md) |  | 

## Example

```python
from opendatasoft_automation.models.dataset_group_security import DatasetGroupSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of DatasetGroupSecurity from a JSON string
dataset_group_security_instance = DatasetGroupSecurity.from_json(json)
# print the JSON string representation of the object
print(DatasetGroupSecurity.to_json())

# convert the object into a dict
dataset_group_security_dict = dataset_group_security_instance.to_dict()
# create an instance of DatasetGroupSecurity from a dict
dataset_group_security_form_dict = dataset_group_security.from_dict(dataset_group_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


