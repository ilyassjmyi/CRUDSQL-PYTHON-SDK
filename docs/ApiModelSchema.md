# ApiModelSchema

Schema information for a model including fields and relationships

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[ApiFieldSchema]**](ApiFieldSchema.md) | Fields contains information about each field in the model | [optional] 
**relationships** | [**List[ApiRelationshipSchema]**](ApiRelationshipSchema.md) | Relationships contains information about model relationships | [optional] 

## Example

```python
from openapi_client.models.api_model_schema import ApiModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApiModelSchema from a JSON string
api_model_schema_instance = ApiModelSchema.from_json(json)
# print the JSON string representation of the object
print(ApiModelSchema.to_json())

# convert the object into a dict
api_model_schema_dict = api_model_schema_instance.to_dict()
# create an instance of ApiModelSchema from a dict
api_model_schema_from_dict = ApiModelSchema.from_dict(api_model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


