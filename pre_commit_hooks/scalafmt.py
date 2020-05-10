import os
import sys
import asyncio
import logging
from sbt_client import SbtClient, SbtError


async def _main() -> int:
    logging.basicConfig(level=logging.DEBUG, filename="sbt-client.log")
    working_directory = os.getcwd()
    client = SbtClient(working_directory)
    await client.connect()
    try:
        await client.execute("clean")
        await client.execute("scalafmtCheck")
        await client.execute("scalafmt")
    except SbtError as error:
        print(error, file=sys.stderr)
        return 0
    return 1


def main() -> int:
    return asyncio.run(_main())


if __name__ == "__main__":
    exit(main())
