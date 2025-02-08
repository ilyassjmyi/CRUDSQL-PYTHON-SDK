# coding: utf-8

"""
    CrudSQL API

    A powerful dynamic CRUD API engine that automatically generates RESTful endpoints for your data models CrudSQL provides automatic CRUD operations, filtering, pagination, and sorting capabilities for any data model. Features: - Automatic REST API generation - Dynamic model support - Complex filtering and querying - Pagination and sorting - Swagger documentation - Multiple database support (SQL & NoSQL)

    The version of the OpenAPI document: 1.0.0
    Contact: taqi@mobix.biz
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt,field_validator,RootModel
from typing import Any, ClassVar, Dict, List, Optional,Union
from typing import Optional, Set
from typing_extensions import Self


class EntityData(RootModel):
    """
    Custom model to handle both single entity and multiple entities
    """
    root: Union[Dict[str, Any], List[Dict[str, Any]]]

    @field_validator('root')
    @classmethod
    def validate_root(cls, v):
        # Ensure we have either a dict or a list of dicts
        if isinstance(v, dict):
            return v
        elif isinstance(v, list):
            if not all(isinstance(item, dict) for item in v):
                raise ValueError("All items in list must be dictionaries")
            return v
        raise ValueError("Data must be either a dictionary or a list of dictionaries")

    def __getitem__(self, item):
        return self.root[item]

    def dict(self, *args, **kwargs):
        return self.root
EntityData.model_rebuild()


class QueryFilterResponse(BaseModel):
    """
    Paginated response containing filtered entities and metadata Used for both simple list operations and complex filtered queries
    """ # noqa: E501
    data: Optional[Union[Dict[str, Any], List[Dict[str, Any]]]] = Field(
        default=None, 
        description="Entity or array of entities matching the filter conditions"
    )   
    page: Optional[StrictInt] = Field(default=None, description="@Description Current page number (1-based indexing) @Description Example: page=2 returns the second page of results")
    page_size: Optional[StrictInt] = Field(default=None, description="@Description Number of items per page (default may vary) @Description Example: page_size=20 returns 20 items per page")
    total: Optional[StrictInt] = Field(default=None, description="@Description Total number of records matching the filter conditions @Description Used for calculating pagination metadata")
    total_pages: Optional[StrictInt] = Field(default=None, description="@Description Total number of pages based on total records and page size @Description Calculated as ceil(total/page_size)")
    __properties: ClassVar[List[str]] = ["data", "page", "page_size", "total", "total_pages"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        arbitrary_types_allowed=True,

    )
    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of QueryFilterResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QueryFilterResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": obj.get("data"),
            "page": obj.get("page"),
            "page_size": obj.get("page_size"),
            "total": obj.get("total"),
            "total_pages": obj.get("total_pages")
        })
        return _obj


QueryFilterResponse.model_rebuild()