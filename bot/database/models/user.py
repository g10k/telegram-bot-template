# ruff: noqa: TCH001, TCH003, A003, F821
from __future__ import annotations

from sqlalchemy.orm import Mapped, mapped_column

from bot.database.models.base import Base, big_int_pk, created_at


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[big_int_pk]
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    language_code: Mapped[str | None]
    referrer: Mapped[str | None]
    created_at: Mapped[created_at]

    is_admin: Mapped[bool] = mapped_column(default=False)
    is_suspicious: Mapped[bool] = mapped_column(default=False)
    is_block: Mapped[bool] = mapped_column(default=False)
    is_premium: Mapped[bool] = mapped_column(default=False)


# # ruff: noqa: TCH001, TCH003, A003, F821
# from __future__ import annotations
#
# from sqlalchemy.orm import Mapped,
#
# from bot.database.models.base import Base, big_int_pk, created_at

def foo():
    pass


class TokenModel(Base):
    __tablename__ = "kb_tokens"

    id: Mapped[big_int_pk]
    token: Mapped[str]
    description: Mapped[str | None]
    # username: Mapped[str | None]
    # language_code: Mapped[str | None]
    # referrer: Mapped[str | None]
    created_at: Mapped[created_at]

    # is_admin: Mapped[bool] = mapped_column(default=False)
    # is_suspicious: Mapped[bool] = mapped_column(default=False)
    # is_block: Mapped[bool] = mapped_column(default=False)
    # is_premium: Mapped[bool] = mapped_column(default=False)
