"""
Alternative Medium API.

An alternative Medium API for interacting with user specific data.
"""

import platform

from pathlib import Path
from selenium import webdriver


__version__ = "0.0.1"


def _get_executable_path():
    os_mapping = {
        "Windows": "windows",
        "Darwin": "macosx",
        "Linux": "linux"
    }

    os_type = platform.system()

    if os_type not in os_mapping:
        raise EnvironmentError("Unsupported system type: {}".format(os_type))

    os_info = os_mapping[os_type]
    filename = "phantomjs-" + os_info

    if os_type == 'Windows':
        filename += ".exe"

    path = Path(__file__).resolve().parent / "phantomjs" / filename

    return str(path)


browser = webdriver.PhantomJS(executable_path=_get_executable_path())
