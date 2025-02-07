# ApiRelationshipSchema

Schema information for a model relationship

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the relationship | [optional] 
**related_model** | **str** | Name of the related model | [optional] 
**type** | **str** | Type of relationship (hasOne, hasMany) | [optional] 

## Example

```python
from openapi_client.models.api_relationship_schema import ApiRelationshipSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRelationshipSchema from a JSON string
api_relationship_schema_instance = ApiRelationshipSchema.from_json(json)
# print the JSON string representation of the object
print(ApiRelationshipSchema.to_json())

# convert the object into a dict
api_relationship_schema_dict = api_relationship_schema_instance.to_dict()
# create an instance of ApiRelationshipSchema from a dict
api_relationship_schema_from_dict = ApiRelationshipSchema.from_dict(api_relationship_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


