from pydantic import BaseModel


class CustombaseModel(BaseModel):
    def dict(*args, **kwargs):
        d = super().dict(*args, **kwargs)
        d = {k: v for k, v in d.items() if v is not None}
        return d
