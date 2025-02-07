# openapi_client.SchemaApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_schema_get**](SchemaApi.md#model_schema_get) | **GET** /{model}/schema | Get model schema


# **model_schema_get**
> ApiModelSchema model_schema_get(model)

Get model schema

Returns the schema information for a specific model including fields and relationships

### Example


```python
import openapi_client
from openapi_client.models.api_model_schema import ApiModelSchema
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to /api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "/api"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SchemaApi(api_client)
    model = 'model_example' # str | Model name

    try:
        # Get model schema
        api_response = api_instance.model_schema_get(model)
        print("The response of SchemaApi->model_schema_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemaApi->model_schema_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model name | 

### Return type

[**ApiModelSchema**](ApiModelSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

