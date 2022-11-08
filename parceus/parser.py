from typing import List, Any

from argument import Argument


class Parser:

    def __init__(self, description: str) -> None:
        self.__arguments: List[Argument] = []

        self.__description: str = description


    def add_argument(
        self,
        *flags: List[str],
        arg_type: type = Any,
        multiple_args: bool = False,
        action: str = "",
        metavar: str = None,
        help_message: str = ""
    ) -> "Parser":
        """Doc here
        """

        self.__arguments.append(
            Argument(
                *flags,
                arg_type=arg_type,
                multiple_args=multiple_args,
                action=action,
                metavar=metavar,
                help_message=help_message,
            )
        )

        return self
