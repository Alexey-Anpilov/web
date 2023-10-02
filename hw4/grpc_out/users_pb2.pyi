from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserId(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: int
    def __init__(self, user_id: _Optional[int] = ...) -> None: ...

class UserInfo(_message.Message):
    __slots__ = ["name", "email", "family"]
    class FullName(_message.Message):
        __slots__ = ["first_name", "last_name", "second_name"]
        FIRST_NAME_FIELD_NUMBER: _ClassVar[int]
        LAST_NAME_FIELD_NUMBER: _ClassVar[int]
        SECOND_NAME_FIELD_NUMBER: _ClassVar[int]
        first_name: str
        last_name: str
        second_name: str
        def __init__(self, first_name: _Optional[str] = ..., last_name: _Optional[str] = ..., second_name: _Optional[str] = ...) -> None: ...
    class FamilyEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: UserInfo.FullName
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[UserInfo.FullName, _Mapping]] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    name: UserInfo.FullName
    email: str
    family: _containers.MessageMap[str, UserInfo.FullName]
    def __init__(self, name: _Optional[_Union[UserInfo.FullName, _Mapping]] = ..., email: _Optional[str] = ..., family: _Optional[_Mapping[str, UserInfo.FullName]] = ...) -> None: ...

class AllUsersResponse(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _containers.RepeatedCompositeFieldContainer[UserInfo]
    def __init__(self, user: _Optional[_Iterable[_Union[UserInfo, _Mapping]]] = ...) -> None: ...

class AllUsersRequest(_message.Message):
    __slots__ = ["max_result"]
    MAX_RESULT_FIELD_NUMBER: _ClassVar[int]
    max_result: int
    def __init__(self, max_result: _Optional[int] = ...) -> None: ...
