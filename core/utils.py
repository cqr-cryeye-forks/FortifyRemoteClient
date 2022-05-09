from typing import TypedDict

from core.data.classes import CommandStatus


class ErrorMessage(TypedDict):
    result: str
    status: CommandStatus


def print_result_message(message: ErrorMessage):
    print(f"{message.get('result', message)}: {message.get('status', 'Command Result')}")
