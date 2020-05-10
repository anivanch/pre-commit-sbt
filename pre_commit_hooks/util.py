from sbt_client import SbtMessageLevel, ExecutionResult


def print_execution_result(result: ExecutionResult) -> None:
    for level in (SbtMessageLevel.INFO, SbtMessageLevel.WARNING, SbtMessageLevel.ERROR):
        messages = result[level]
        if messages:
            print(*messages)
