from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class VersionBase(BaseModel):
    product: Optional[str] = None
    version: Optional[str] = None
    desc: Optional[str] = None
    release_time: Optional[int] = None

# Properties to receive via API on creation
class VersionCreate(VersionBase):
    pass

# Properties to receive via API on update
class VersionUpdate(VersionBase):
    pass

class VersionInDBBase(VersionBase):
    id: Optional[int] = None
    status: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Version(VersionInDBBase):
    pass

