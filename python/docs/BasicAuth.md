# BasicAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** | The password for the user. The API returns null to hide this sensitive value. | 

## Example

```python
from opendatasoft_automation.models.basic_auth import BasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of BasicAuth from a JSON string
basic_auth_instance = BasicAuth.from_json(json)
# print the JSON string representation of the object
print(BasicAuth.to_json())

# convert the object into a dict
basic_auth_dict = basic_auth_instance.to_dict()
# create an instance of BasicAuth from a dict
basic_auth_form_dict = basic_auth.from_dict(basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


