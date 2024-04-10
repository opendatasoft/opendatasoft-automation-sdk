# SharepointOIDCAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nonce** | **str** |  | 
**grant_type** | **str** |  | 
**code** | **str** |  | 
**claims** | **object** |  | [readonly] 

## Example

```python
from openapi_client.models.sharepoint_oidc_auth import SharepointOIDCAuth

# TODO update the JSON string below
json = "{}"
# create an instance of SharepointOIDCAuth from a JSON string
sharepoint_oidc_auth_instance = SharepointOIDCAuth.from_json(json)
# print the JSON string representation of the object
print(SharepointOIDCAuth.to_json())

# convert the object into a dict
sharepoint_oidc_auth_dict = sharepoint_oidc_auth_instance.to_dict()
# create an instance of SharepointOIDCAuth from a dict
sharepoint_oidc_auth_form_dict = sharepoint_oidc_auth.from_dict(sharepoint_oidc_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


