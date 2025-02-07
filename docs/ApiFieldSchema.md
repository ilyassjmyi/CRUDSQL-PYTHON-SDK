# ApiFieldSchema

Schema information for a model field

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the field | [optional] 
**operators** | **List[str]** | List of supported operators for this field | [optional] 
**type** | **str** | Type of the field (e.g., string, int) | [optional] 

## Example

```python
from openapi_client.models.api_field_schema import ApiFieldSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApiFieldSchema from a JSON string
api_field_schema_instance = ApiFieldSchema.from_json(json)
# print the JSON string representation of the object
print(ApiFieldSchema.to_json())

# convert the object into a dict
api_field_schema_dict = api_field_schema_instance.to_dict()
# create an instance of ApiFieldSchema from a dict
api_field_schema_from_dict = ApiFieldSchema.from_dict(api_field_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


