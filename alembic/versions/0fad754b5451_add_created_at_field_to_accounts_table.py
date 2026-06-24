"""add created_at field to accounts table

Revision ID: 0fad754b5451
Revises: dc382e540ed5
Create Date: 2026-06-22 15:24:59.688818

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fad754b5451'
down_revision: Union[str, Sequence[str], None] = 'dc382e540ed5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # pass
    op.add_column(
        "accounts",
        sa.Column('created_at', sa.DateTime)
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
