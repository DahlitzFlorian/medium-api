"""
Alternative Medium API.

An alternative Medium API for interacting with user specific data.
"""
import colorlog


__version__ = "0.0.1"

_handler = colorlog.StreamHandler()
_handler.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(message)s"))

logger = colorlog.getLogger(__name__)
logger.addHandler(_handler)
