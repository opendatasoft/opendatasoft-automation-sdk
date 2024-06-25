# ODSOIDCAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** |  | 
**grant_type** | **str** |  | 
**code** | **str** |  | 
**claims** | **object** |  | [readonly] 

## Example

```python
from opendatasoft_automation.models.odsoidc_auth import ODSOIDCAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ODSOIDCAuth from a JSON string
odsoidc_auth_instance = ODSOIDCAuth.from_json(json)
# print the JSON string representation of the object
print(ODSOIDCAuth.to_json())

# convert the object into a dict
odsoidc_auth_dict = odsoidc_auth_instance.to_dict()
# create an instance of ODSOIDCAuth from a dict
odsoidc_auth_from_dict = ODSOIDCAuth.from_dict(odsoidc_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


