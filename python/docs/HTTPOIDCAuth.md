# HTTPOIDCAuth


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
from opendatasoft_automation.models.httpoidc_auth import HTTPOIDCAuth

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPOIDCAuth from a JSON string
httpoidc_auth_instance = HTTPOIDCAuth.from_json(json)
# print the JSON string representation of the object
print(HTTPOIDCAuth.to_json())

# convert the object into a dict
httpoidc_auth_dict = httpoidc_auth_instance.to_dict()
# create an instance of HTTPOIDCAuth from a dict
httpoidc_auth_from_dict = HTTPOIDCAuth.from_dict(httpoidc_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


