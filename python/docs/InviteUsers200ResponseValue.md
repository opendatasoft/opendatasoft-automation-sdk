# InviteUsers200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **str** |  | [optional] 
**data** | [**User**](User.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.invite_users200_response_value import InviteUsers200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of InviteUsers200ResponseValue from a JSON string
invite_users200_response_value_instance = InviteUsers200ResponseValue.from_json(json)
# print the JSON string representation of the object
print(InviteUsers200ResponseValue.to_json())

# convert the object into a dict
invite_users200_response_value_dict = invite_users200_response_value_instance.to_dict()
# create an instance of InviteUsers200ResponseValue from a dict
invite_users200_response_value_form_dict = invite_users200_response_value.from_dict(invite_users200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


