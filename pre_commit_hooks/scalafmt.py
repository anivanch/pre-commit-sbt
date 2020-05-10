import asyncio
from sbt_client import (
    SbtMessageLevel,
    iterate_messages,
)
from .common import create_client


async def _main() -> int:
    client = create_client()
    await client.connect()
    check_result = await client.execute("scalafmtCheck")
    if SbtMessageLevel.ERROR in check_result.levels:
        for message in iterate_messages(check_result):
            print(message)
        return 1
    fmt_result = await client.execute("scalafmt")
    if SbtMessageLevel.ERROR in fmt_result.levels:
        for message in iterate_messages(fmt_result):
            print(message)
        return 1
    return 0


def main() -> int:
    return asyncio.run(_main())


if __name__ == "__main__":
    exit(main())
