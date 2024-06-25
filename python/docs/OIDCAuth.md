# OIDCAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**scope** | **str** |  | 
**token_endpoint** | **str** |  | 
**grant_type** | **str** |  | 
**code** | **str** |  | [optional] 
**claims** | **object** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.oidc_auth import OIDCAuth

# TODO update the JSON string below
json = "{}"
# create an instance of OIDCAuth from a JSON string
oidc_auth_instance = OIDCAuth.from_json(json)
# print the JSON string representation of the object
print(OIDCAuth.to_json())

# convert the object into a dict
oidc_auth_dict = oidc_auth_instance.to_dict()
# create an instance of OIDCAuth from a dict
oidc_auth_from_dict = OIDCAuth.from_dict(oidc_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


