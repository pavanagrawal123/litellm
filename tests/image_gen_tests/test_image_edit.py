# What this tests?
## This tests the litellm support for the openai /generations endpoint

import logging
import os
import sys
import traceback


sys.path.insert(
    0, os.path.abspath("../..")
)  # Adds the parent directory to the system path

from dotenv import load_dotenv
from openai.types.image import Image
from litellm.caching import InMemoryCache

logging.basicConfig(level=logging.DEBUG)
load_dotenv()
import asyncio
import os
import pytest

import litellm
import json
import tempfile
from base_image_generation_test import BaseImageGenTest
import logging
from litellm._logging import verbose_logger
import requests
from io import BytesIO

verbose_logger.setLevel(logging.DEBUG)


@pytest.fixture
def image_url():
    # URL of the image
    image_url = "https://litellm-listing.s3.amazonaws.com/litellm_logo.png"

    # Fetch the image from the URL
    response = requests.get(image_url)
    print(response)
    response.raise_for_status()  # Ensure the request was successful

    # Load the image into a file-like object
    image_file = BytesIO(response.content)

    return image_file


def test_openai_image_edit_openai_sdk(image_url):
    from openai import OpenAI

    client = OpenAI()
    response = client.images.create_variation(image=image_url, n=2, size="1024x1024")
    print(response)


def test_openai_image_edit_litellm_sdk(image_url):
    from litellm import image_variation

    image_variation(image=image_url, n=2, size="1024x1024")


def test_topaz_image_edit():
    pass
