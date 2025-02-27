# coding: utf-8

"""
    CrudSQL API

    A powerful dynamic CRUD API engine that automatically generates RESTful endpoints for your data models CrudSQL provides automatic CRUD operations, filtering, pagination, and sorting capabilities for any data model. Features: - Automatic REST API generation - Dynamic model support - Complex filtering and querying - Pagination and sorting - Swagger documentation - Multiple database support (SQL & NoSQL)

    The version of the OpenAPI document: 1.0.0
    Contact: taqi@mobix.biz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.schema_api import SchemaApi


class TestSchemaApi(unittest.TestCase):
    """SchemaApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SchemaApi()

    def tearDown(self) -> None:
        pass

    def test_model_schema_get(self) -> None:
        """Test case for model_schema_get

        Get model schema
        """
        pass


if __name__ == '__main__':
    unittest.main()
