"""Входная точка в приложение."""

from fastapi import FastAPI

from .access import access_routes
from .core import AppCreator

app: FastAPI = AppCreator().add_health_routes().include_routers([access_routes]).get_app()
