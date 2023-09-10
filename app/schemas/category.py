import re

from pydantic import validator
from schemas.base import CustombaseModel


class Category(CustombaseModel):
    name: str
    slug: str

    @validator("slug")
    def validate_slug(cls, value):
        if not re.match(r"^([a-z]|-|_)+$", value):
            raise ValueError("Invalid slug")
        return value
