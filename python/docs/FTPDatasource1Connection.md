# FTPDatasource1Connection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** | The UID of an existing connection to reuse. | 

## Example

```python
from opendatasoft_automation.models.ftp_datasource1_connection import FTPDatasource1Connection

# TODO update the JSON string below
json = "{}"
# create an instance of FTPDatasource1Connection from a JSON string
ftp_datasource1_connection_instance = FTPDatasource1Connection.from_json(json)
# print the JSON string representation of the object
print(FTPDatasource1Connection.to_json())

# convert the object into a dict
ftp_datasource1_connection_dict = ftp_datasource1_connection_instance.to_dict()
# create an instance of FTPDatasource1Connection from a dict
ftp_datasource1_connection_from_dict = FTPDatasource1Connection.from_dict(ftp_datasource1_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


