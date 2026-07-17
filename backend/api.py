"""
api.py

Purpose:
    Expose the Enterprise Knowledge Assistant through a REST API.
"""

from fastapi import FastAPI

app = FastAPI(
    title="Enterprise Knowledge Assistant",
    version="1.0",
)