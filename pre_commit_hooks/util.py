from colorama import Fore, Style
from sbt_client import SbtMessageLevel, ExecutionResult


def print_execution_result(result: ExecutionResult) -> None:
    for level in (SbtMessageLevel.INFO, SbtMessageLevel.WARNING, SbtMessageLevel.ERROR):
        level_str = _print_level(level)
        messages = result[level]
        if messages:
            for message in messages:
                print(f"{level_str} {message}")


def _print_level(level: SbtMessageLevel) -> str:
    if level is SbtMessageLevel.ERROR:
        return Fore.RED + "[ERROR]" + Style.RESET_ALL
    if level is SbtMessageLevel.WARNING:
        return Fore.YELLOW + "[WARNING]" + Style.RESET_ALL
    if level is SbtMessageLevel.INFO:
        return Fore.GREEN + "[INFO]" + Style.RESET_ALL
    return Style.DIM + "[DEBUG]" + Style.RESET_ALL
