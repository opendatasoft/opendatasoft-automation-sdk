# AmazonS3Connection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**headers** | [**List[HTTPConnectionAllOfHeaders]**](HTTPConnectionAllOfHeaders.md) |  | [optional] 
**auth** | [**AmazonS3Auth**](AmazonS3Auth.md) |  | [optional] 

## Example

```python
from opendatasoft_automation.models.amazon_s3_connection import AmazonS3Connection

# TODO update the JSON string below
json = "{}"
# create an instance of AmazonS3Connection from a JSON string
amazon_s3_connection_instance = AmazonS3Connection.from_json(json)
# print the JSON string representation of the object
print(AmazonS3Connection.to_json())

# convert the object into a dict
amazon_s3_connection_dict = amazon_s3_connection_instance.to_dict()
# create an instance of AmazonS3Connection from a dict
amazon_s3_connection_form_dict = amazon_s3_connection.from_dict(amazon_s3_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


