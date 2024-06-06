"""Add kb_token.id autoincrement

Revision ID: 55b4ce4d7c50
Revises: b99049a87d15
Create Date: 2024-05-13 05:40:13.911455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '55b4ce4d7c50'
down_revision: Union[str, None] = 'b99049a87d15'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('kb_tokens', sa.Column('id', sa.BigInteger(), nullable=False, autoincrement=True))


def downgrade() -> None:
    pass
