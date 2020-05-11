import typing as t
import os
import logging
from sbt_client import SbtClient


PLUGIN_DIR = "./project/plugins.sbt"


def create_client() -> SbtClient:
    logging.basicConfig(level=logging.DEBUG, filename="sbt-client.log")
    working_directory = os.getcwd()
    return SbtClient(working_directory)


def require_plugin(required_plugin: str) -> bool:
    with open(PLUGIN_DIR, "r") as f:
        installed = f.read()
        return _require_plugin(required_plugin, installed)


def require_plugins(required_plugins: t.List[str]) -> bool:
    with open(PLUGIN_DIR, "r") as f:
        installed = f.read()
        return all(_require_plugin(plugin, installed) for plugin in required_plugins)


def _require_plugin(required_plugin: str, installed_plugins: str) -> bool:
    if required_plugin not in installed_plugins:
        print(
            f"No {required_plugin} plugin found in {PLUGIN_DIR},"
            "please make sure it is installed."
        )
        return False
    return True
