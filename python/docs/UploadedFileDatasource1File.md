# UploadedFileDatasource1File


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | Unique identifier for the file | [readonly] 
**filename** | **str** |  | [readonly] 
**mimetype** | **str** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from opendatasoft_automation.models.uploaded_file_datasource1_file import UploadedFileDatasource1File

# TODO update the JSON string below
json = "{}"
# create an instance of UploadedFileDatasource1File from a JSON string
uploaded_file_datasource1_file_instance = UploadedFileDatasource1File.from_json(json)
# print the JSON string representation of the object
print(UploadedFileDatasource1File.to_json())

# convert the object into a dict
uploaded_file_datasource1_file_dict = uploaded_file_datasource1_file_instance.to_dict()
# create an instance of UploadedFileDatasource1File from a dict
uploaded_file_datasource1_file_from_dict = UploadedFileDatasource1File.from_dict(uploaded_file_datasource1_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


