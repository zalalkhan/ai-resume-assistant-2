"""Lets the tests run even if streamlit / google-genai are not installed."""
import sys
import types
from unittest.mock import MagicMock

try:
    import streamlit  # noqa: F401
except ImportError:
    sys.modules["streamlit"] = MagicMock()

try:
    from google import genai  # noqa: F401
except ImportError:
    google = types.ModuleType("google")
    genai_stub = MagicMock()
    google.genai = genai_stub
    genai_stub.types = MagicMock()
    sys.modules.update({"google": google, "google.genai": genai_stub,
                        "google.genai.types": genai_stub.types})
