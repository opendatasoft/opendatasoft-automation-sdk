# PostApikeysApikeyUidRevokeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** |  | [optional] 

## Example

```python
from opendatasoft_automation.models.post_apikeys_apikey_uid_revoke_request import PostApikeysApikeyUidRevokeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostApikeysApikeyUidRevokeRequest from a JSON string
post_apikeys_apikey_uid_revoke_request_instance = PostApikeysApikeyUidRevokeRequest.from_json(json)
# print the JSON string representation of the object
print(PostApikeysApikeyUidRevokeRequest.to_json())

# convert the object into a dict
post_apikeys_apikey_uid_revoke_request_dict = post_apikeys_apikey_uid_revoke_request_instance.to_dict()
# create an instance of PostApikeysApikeyUidRevokeRequest from a dict
post_apikeys_apikey_uid_revoke_request_form_dict = post_apikeys_apikey_uid_revoke_request.from_dict(post_apikeys_apikey_uid_revoke_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


