"""create kb_tokens table

Revision ID: b99049a87d15
Revises: e4b7e8c165c1
Create Date: 2024-05-12 11:51:23.864127

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b99049a87d15'
down_revision: Union[str, None] = 'e4b7e8c165c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "kb_tokens",
        sa.Column("id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("token", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("TIMEZONE('utc', now())"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
        sa.UniqueConstraint("token"),
    )


def downgrade() -> None:
    pass
