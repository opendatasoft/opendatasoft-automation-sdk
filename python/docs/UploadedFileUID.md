# UploadedFileUID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The UID of an existing uploaded file to reuse. | 

## Example

```python
from opendatasoft_automation.models.uploaded_file_uid import UploadedFileUID

# TODO update the JSON string below
json = "{}"
# create an instance of UploadedFileUID from a JSON string
uploaded_file_uid_instance = UploadedFileUID.from_json(json)
# print the JSON string representation of the object
print(UploadedFileUID.to_json())

# convert the object into a dict
uploaded_file_uid_dict = uploaded_file_uid_instance.to_dict()
# create an instance of UploadedFileUID from a dict
uploaded_file_uid_from_dict = UploadedFileUID.from_dict(uploaded_file_uid_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


