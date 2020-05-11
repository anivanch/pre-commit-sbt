import typing as t
import os
import logging
from sbt_client import SbtClient


PLUGIN_FILE = "./project/plugins.sbt"


def create_client() -> SbtClient:
    logging.basicConfig(level=logging.INFO)
    working_directory = os.getcwd()
    return SbtClient(working_directory)


def require_plugin(required_plugin: str) -> bool:
    with open(PLUGIN_FILE, "r") as f:
        installed = f.read()
        return _require_plugin(required_plugin, installed)


def require_plugins(required_plugins: t.List[str]) -> bool:
    with open(PLUGIN_FILE, "r") as f:
        installed = f.read()
        return all(_require_plugin(plugin, installed) for plugin in required_plugins)


def _require_plugin(required_plugin: str, installed_plugins: str) -> bool:
    if required_plugin not in installed_plugins:
        print(
            f"Plugin '{required_plugin}' not found in {PLUGIN_FILE}, "
            "please make sure it is installed and try again."
        )
        return False
    return True
