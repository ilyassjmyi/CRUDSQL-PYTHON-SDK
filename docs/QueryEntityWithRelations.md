# QueryEntityWithRelations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_entity** | **object** |  | [optional] 
**relations** | **Dict[str, List[object]]** |  | [optional] 

## Example

```python
from openapi_client.models.query_entity_with_relations import QueryEntityWithRelations

# TODO update the JSON string below
json = "{}"
# create an instance of QueryEntityWithRelations from a JSON string
query_entity_with_relations_instance = QueryEntityWithRelations.from_json(json)
# print the JSON string representation of the object
print(QueryEntityWithRelations.to_json())

# convert the object into a dict
query_entity_with_relations_dict = query_entity_with_relations_instance.to_dict()
# create an instance of QueryEntityWithRelations from a dict
query_entity_with_relations_from_dict = QueryEntityWithRelations.from_dict(query_entity_with_relations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


