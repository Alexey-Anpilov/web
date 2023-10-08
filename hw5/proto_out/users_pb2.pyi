from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserInfo(_message.Message):
    __slots__ = ["name", "email"]
    class FullName(_message.Message):
        __slots__ = ["first_name", "last_name", "second_name"]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        SECOND_NAME_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        last_name: str
        second_name: str
        def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., second_name: _Optional[str] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    name: UserInfo.FullName
    email: str
    def __init__(self, name: _Optional[_Union[UserInfo.FullName, _Mapping]] = ..., email: _Optional[str] = ...) -> None: ...

class UserAddr(_message.Message):
    __slots__ = ["addr"]
    ADDR_FIELD_NUMBER: _ClassVar[int]
    addr: str
    def __init__(self, addr: _Optional[str] = ...) -> None: ...
