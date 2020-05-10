import os
import asyncio
import logging
from sbt_client import SbtClient


async def _main() -> int:
    logging.basicConfig(level=logging.INFO)
    working_directory = os.getcwd()
    client = SbtClient(working_directory)
    await client.execute("clean; scalafmt; scalafmtCheck;")
    return 1


def main() -> int:
    return asyncio.run(_main())


if __name__ == "__main__":
    exit(main())
