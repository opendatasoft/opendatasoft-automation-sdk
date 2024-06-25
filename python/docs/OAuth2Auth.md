# OAuth2Auth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**scope** | **str** |  | 
**token_endpoint** | **str** |  | 
**grant_type** | **str** |  | 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.o_auth2_auth import OAuth2Auth

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth2Auth from a JSON string
o_auth2_auth_instance = OAuth2Auth.from_json(json)
# print the JSON string representation of the object
print(OAuth2Auth.to_json())

# convert the object into a dict
o_auth2_auth_dict = o_auth2_auth_instance.to_dict()
# create an instance of OAuth2Auth from a dict
o_auth2_auth_from_dict = OAuth2Auth.from_dict(o_auth2_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


