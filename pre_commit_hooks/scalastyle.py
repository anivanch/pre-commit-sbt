import asyncio
from sbt_client import (
    SbtMessageLevel,
    iterate_messages,
)
from .common import (
    create_client,
    require_plugin,
)


async def _main() -> int:
    if not require_plugin("scalastyle-sbt-plugin"):
        return 1
    client = create_client()
    await client.connect()
    result = await client.execute("scalastyle")
    if SbtMessageLevel.ERROR in result.levels:
        for message in iterate_messages(result):
            print(message)
        return 1
    return 0


def main() -> int:
    return asyncio.run(_main())


if __name__ == "__main__":
    exit(main())
