# QueryQueryFilter

Filter conditions for querying entities using complex expressions Supports logical operations (AND, OR, NOT), field comparisons, and relationship filtering Example: { \"expressions\": [ {\"field\": \"age\", \"operator\": \"gte\", \"value\": 18}, { \"operator\": \"AND\", \"expressions\": [ {\"field\": \"status\", \"operator\": \"eq\", \"value\": \"active\"} ] } ] }

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expressions** | **List[object]** | @Description Array of expressions to filter entities @Description Each expression can be a FieldExpression, LogicalExpression, or RelationshipExpression | [optional] 

## Example

```python
from openapi_client.models.query_query_filter import QueryQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of QueryQueryFilter from a JSON string
query_query_filter_instance = QueryQueryFilter.from_json(json)
# print the JSON string representation of the object
print(QueryQueryFilter.to_json())

# convert the object into a dict
query_query_filter_dict = query_query_filter_instance.to_dict()
# create an instance of QueryQueryFilter from a dict
query_query_filter_from_dict = QueryQueryFilter.from_dict(query_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


