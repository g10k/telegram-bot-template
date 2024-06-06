from sqlalchemy.ext.asyncio import AsyncSession

from bot.cache.redis import build_key, cached
from bot.database.models import TokenModel
from sqlalchemy import func, select, update
import datetime


@cached(key_builder=lambda session: build_key())
async def get_all_users(session: AsyncSession) -> list[TokenModel]:
    query = select(TokenModel)

    result = await session.execute(query)

    tokens = result.scalars()
    return list(tokens)


# def get_db_session() -> AsyncSession:
def get_db_session():
    from sqlalchemy.future import select
    from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
    from sqlalchemy.orm import sessionmaker

    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    # engine = create_engine("postgresql://tgbot:OGU6P2TNUEwxekD0OHe7@pgbouncer/bot_db")
    engine = create_engine("postgresql+asyncpg://tgbot:OGU6P2TNUEwxekD0OHe7@pgbouncer/bot_db")

    # engine = create_engine("postgresql+psycopg2://tgbot:OGU6P2TNUEwxekD0OHe7@pgbouncer/bot_db")
    # -> no module psycopg2
    s = Session(engine)
    return s

    # an Engine, which the Session will use for connection
    # resources
    # engine = create_engine("postgresql+psycopg2://scott:tiger@localhost/dbname")
    # engine = create_engine("postgresql+psycopg2://tgbot:OGU6P2TNUEwxekD0OHe7@pgbouncer/bot_db")
    # DB_HOST = "pgbouncer"  # use "localhost" if not using Docker
    # DB_PORT = 5432
    # DB_USER = "tgbot"
    # DB_PASS = "OGU6P2TNUEwxekD0OHe7"
    # DB_NAME = "bot_db"
    # engine = create_async_engine()
    return sessionmaker(
        engine,
        expire_on_commit=False,
        class_=AsyncSession,
    )


def save_token(value: str):
    session = get_db_session()
    new_token = TokenModel(
        token=value,
        description='lol',
        # created_at=datetime.datetime.utcnow(),
    )

    session.add(new_token)
    session.commit()
    return session, value
