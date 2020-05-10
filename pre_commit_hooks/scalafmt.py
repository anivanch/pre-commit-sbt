import asyncio
from sbt_client import (
    SbtMessageLevel,
    colored_result,
)
import logging
from .common import create_client


async def _main() -> int:
    client = create_client()
    await client.connect()
    check_result = await client.execute("scalafmtCheck")
    logging.info(f"CHECK RESULT: {check_result}")
    for message in colored_result(check_result):
        print(message)
    if SbtMessageLevel.ERROR in check_result:
        return 1
    fmt_result = await client.execute("scalafmt")
    for message in colored_result(fmt_result):
        print(message)
    if SbtMessageLevel.ERROR in fmt_result:
        return 1
    return 0


def main() -> int:
    return asyncio.run(_main())


if __name__ == "__main__":
    exit(main())
