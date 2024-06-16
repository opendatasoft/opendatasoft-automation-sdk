# FTPDatasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relative_url** | **str** |  | [optional] 
**connection** | [**FTPDatasource1Connection**](FTPDatasource1Connection.md) |  | 

## Example

```python
from opendatasoft_automation.models.ftp_datasource import FTPDatasource

# TODO update the JSON string below
json = "{}"
# create an instance of FTPDatasource from a JSON string
ftp_datasource_instance = FTPDatasource.from_json(json)
# print the JSON string representation of the object
print(FTPDatasource.to_json())

# convert the object into a dict
ftp_datasource_dict = ftp_datasource_instance.to_dict()
# create an instance of FTPDatasource from a dict
ftp_datasource_form_dict = ftp_datasource.from_dict(ftp_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


