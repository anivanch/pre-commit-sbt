import os
from sbt_client import SbtClient


def create_client() -> SbtClient:
    working_directory = os.getcwd()
    return SbtClient(working_directory)
