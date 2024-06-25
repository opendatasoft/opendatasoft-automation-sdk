# AmazonS3Datasource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**headers** | [**List[HTTPDatasource1Headers]**](HTTPDatasource1Headers.md) |  | [optional] 
**connection** | [**AmazonS3DatasourceAllOfConnection**](AmazonS3DatasourceAllOfConnection.md) |  | 

## Example

```python
from opendatasoft_automation.models.amazon_s3_datasource import AmazonS3Datasource

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonS3Datasource from a JSON string
amazon_s3_datasource_instance = AmazonS3Datasource.from_json(json)
# print the JSON string representation of the object
print(AmazonS3Datasource.to_json())

# convert the object into a dict
amazon_s3_datasource_dict = amazon_s3_datasource_instance.to_dict()
# create an instance of AmazonS3Datasource from a dict
amazon_s3_datasource_from_dict = AmazonS3Datasource.from_dict(amazon_s3_datasource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


