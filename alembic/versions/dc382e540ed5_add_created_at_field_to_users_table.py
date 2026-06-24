"""add created_at field to users table

Revision ID: dc382e540ed5
Revises: f47e6f447f8f
Create Date: 2026-06-22 15:17:37.983924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc382e540ed5'
down_revision: Union[str, Sequence[str], None] = 'f47e6f447f8f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # pass
    op.add_column(
        "users",
        sa.Column('created_at', sa.DateTime)
    )


def downgrade() -> None:
    """Downgrade schema."""
    pass
    