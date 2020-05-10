import os
import logging
from sbt_client import SbtClient


def create_client() -> SbtClient:
    logging.basicConfig(level=logging.DEBUG, filename="sbt-client.log")
    working_directory = os.getcwd()
    return SbtClient(working_directory)
