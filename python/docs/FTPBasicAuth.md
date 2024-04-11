# FTPBasicAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** | The password for the user. The API returns null to hide this sensitive value. | 

## Example

```python
from openapi_client.models.ftp_basic_auth import FTPBasicAuth

# TODO update the JSON string below
json = "{}"
# create an instance of FTPBasicAuth from a JSON string
ftp_basic_auth_instance = FTPBasicAuth.from_json(json)
# print the JSON string representation of the object
print(FTPBasicAuth.to_json())

# convert the object into a dict
ftp_basic_auth_dict = ftp_basic_auth_instance.to_dict()
# create an instance of FTPBasicAuth from a dict
ftp_basic_auth_form_dict = ftp_basic_auth.from_dict(ftp_basic_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

