from concurrent.futures import Future
from enum import Enum
from typing import Any, Callable, Dict, List, Tuple, Union

from easyforms import server

# Dict values are the value of the final data type (which is why it is 'Any')
DataValues = Dict[str, Any]
# When tuple, first is value, Second is display - otherwise it is both
Options = List[Union[Tuple[Any, str], str]]

# Takes username and password as params
# Returns empty list (bad username/password) or list of security groups allowed
# -or- True - logged in with full access or False bad username/password
LoginFunc = Callable[[str, str], Union[List[str], bool]]
OptionsFunc = Callable[[DataValues], Options]
# Blank return means passed validation, otherwise string is error msg
ValidateFunc = Callable[[Any, DataValues], str]
# First param is text to display, Second is % progress
ProgressFunc = Callable[[str, int], None]
# First return type is when using concurrent futures allowing cancellation
# Second is for synchronous processing returning true for sucess, false for failure
SubmitFunc = Callable[[DataValues, ProgressFunc], Union[Future, bool]]


class DataType(Enum):
    TEXT = 1
    NUMBER = 2
    BOOL = 3


class Control(Enum):
    TEXTFIELD = 1  # TEXT, NUMBER
    DROPDOWN = 2  # TEXT, NUMBER, BOOL
    CHECKBOXES = 3  # BOOL, NUMBER, BOOL
    RADIO_BUTTONS = 4  # BOOL (2 only), NUMBER


def run(login_func: LoginFunc, pages: List["Page"], ip="127.0.0.1", port=8080):
    server.run(ip, port)


class DataField:
    def __init__(
        self,
        label: str,
        name: str,
        desc: str = "",
        dataType: DataType = DataType.TEXT,
        default: Any = None,
        control: Control = Control.TEXTFIELD,
        multivalue: bool = False,
        required: bool = True,
        editable: bool = True,
        options: Union[OptionsFunc, Options] = [],
        validate: Union[ValidateFunc, Tuple[str, str]] = ("", ""),  # Regex + message
    ):
        pass


class Page:
    def __init__(
        self,
        section: str,
        title: str,
        fields: List[DataField],
        submit_func: SubmitFunc,
        group: str = "",  # Security group
    ):
        pass
