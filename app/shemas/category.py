import re

from pydantic import validator

from app.shemas.base import CustombaseModel


class category(CustombaseModel):
    name: str
    slug: str

    @validator("slug")
    def validate_slug(cls, value):
        if not re.match("^([a-z]|-|_)+$", value):
            raise ValueError("Invalid slug")
        return value
