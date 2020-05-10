import os
import asyncio
import logging
from sbt_client import SbtClient, SbtMessageLevel
from pre_commit_hooks.util import print_execution_result


async def _main() -> int:
    logging.basicConfig(level=logging.DEBUG, filename="sbt-client.log")
    working_directory = os.getcwd()
    client = SbtClient(working_directory)
    await client.connect()
    check_result = await client.execute_many("clean", "scalafmtCheck")
    print_execution_result(check_result)
    if SbtMessageLevel.ERROR in check_result:
        return 1
    fmt_result = await client.execute("scalafmt")
    print_execution_result(fmt_result)
    if SbtMessageLevel.ERROR in fmt_result:
        return 1
    return 0


def main() -> int:
    return asyncio.run(_main())


if __name__ == "__main__":
    exit(main())
