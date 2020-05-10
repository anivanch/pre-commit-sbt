import asyncio
from sbt_client import (
    SbtMessageLevel,
    colored_result,
)
from .common import create_client


async def _main() -> int:
    client = create_client()
    await client.connect()
    result = await client.execute("scalastyle")
    for message in colored_result(result):
        print(message)
    if SbtMessageLevel.ERROR in result:
        return 1
    return 0


def main() -> int:
    return asyncio.run(_main())


if __name__ == "__main__":
    exit(main())
