from fastapi import Depends
from sqlalchemy.orm import Session

from .base import Base, SessionLocal, engine  # noqa


class GetDB:  # Context Manager
    def __init__(self):
        self.db = SessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


def get_db():  # Dependency
    with GetDB() as db:
        yield db


from .crud import (create_admin, create_notification_reminder,  # noqa
                   create_user, delete_notification_reminder, get_admin,
                   get_admins, get_jwt_secret_key, get_notification_reminder,
                   get_or_create_inbound, get_system_usage, get_user,
                   get_user_by_id, get_users, get_users_count, remove_admin,
                   remove_user, update_admin, update_user, update_user_status)
from .models import JWT, System, User  # noqa

__all__ = [
    "get_or_create_inbound",
    "get_user",
    "get_user_by_id",
    "get_users",
    "get_users_count",
    "create_user",
    "remove_user",
    "update_user",
    "update_user_status",
    "get_system_usage",
    "get_jwt_secret_key",
    "get_admin",
    "create_admin",
    "update_admin",
    "remove_admin",
    "get_admins",
    "create_notification_reminder",
    "delete_notification_reminder",
    "get_notification_reminder",

    "GetDB",
    "get_db",

    "User",
    "System",
    "JWT",

    "Base",
    "Session",
]
