# ruff: noqa: TCH001, TCH003, A003, F821
from __future__ import annotations

from sqlalchemy.orm import Mapped

from bot.database.models.base import Base, big_int_autoinc_pk, created_at


class TokenModel(Base):
    __tablename__ = "kb_tokens"
    # extend_existing = True

    # Чтобы не было этого прописываем __table_args__
    #   sqlalchemy.exc.InvalidRequestError: Table 'kb_tokens' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
    # __table_args__ = {'extend_existing': True}

    id: Mapped[big_int_autoinc_pk]
    token: Mapped[str]
    description: Mapped[str | None]
    created_at: Mapped[created_at]
