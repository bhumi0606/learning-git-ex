"""create user table

Revision ID: 811174f9af5c
Revises: 
Create Date: 2026-06-17 11:05:19.868219

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '811174f9af5c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # pass
    op.create_table(
        'users',
        sa.Column('id',sa.Integer(),primary_key=True),
        sa.Column('name',sa.String(length=30)),
        sa.Column('email',sa.String(length=20),unique=True),
        sa.Column('password',sa.String(length=255)),
        sa.Column('role',sa.String(length=20))
    )


def downgrade() -> None:
    """Downgrade schema."""
    # pass
    op.drop_table('users')
