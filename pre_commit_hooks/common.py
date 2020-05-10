import os
import logging
from sbt_client import SbtClient


def create_client() -> SbtClient:
    logging.basicConfig(level=logging.DEBUG, filename="sbt-client.log")
    print("HYA")
    working_directory = os.getcwd()
    return SbtClient(working_directory)
