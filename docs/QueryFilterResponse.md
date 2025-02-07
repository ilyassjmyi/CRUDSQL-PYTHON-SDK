# QueryFilterResponse

Paginated response containing filtered entities and metadata Used for both simple list operations and complex filtered queries

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **object** | @Description Array of entities matching the filter conditions @Description For relationship queries, includes related entities based on the filter | [optional] 
**page** | **int** | @Description Current page number (1-based indexing) @Description Example: page&#x3D;2 returns the second page of results | [optional] 
**page_size** | **int** | @Description Number of items per page (default may vary) @Description Example: page_size&#x3D;20 returns 20 items per page | [optional] 
**total** | **int** | @Description Total number of records matching the filter conditions @Description Used for calculating pagination metadata | [optional] 
**total_pages** | **int** | @Description Total number of pages based on total records and page size @Description Calculated as ceil(total/page_size) | [optional] 

## Example

```python
from openapi_client.models.query_filter_response import QueryFilterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QueryFilterResponse from a JSON string
query_filter_response_instance = QueryFilterResponse.from_json(json)
# print the JSON string representation of the object
print(QueryFilterResponse.to_json())

# convert the object into a dict
query_filter_response_dict = query_filter_response_instance.to_dict()
# create an instance of QueryFilterResponse from a dict
query_filter_response_from_dict = QueryFilterResponse.from_dict(query_filter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


