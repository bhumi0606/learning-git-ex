"""create account table

Revision ID: f47e6f447f8f
Revises: 811174f9af5c
Create Date: 2026-06-17 11:19:46.671812

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f47e6f447f8f'
down_revision: Union[str, Sequence[str], None] = '811174f9af5c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # pass
    op.create_table(
        'accounts',
        sa.Column('id',sa.Integer(),primary_key=True),
        sa.Column('user_id',sa.Integer()),
        sa.Column('account_number',sa.String(length=15),unique=True),
        sa.Column('account_type',sa.String(length=30)),
        sa.Column('balance',sa.Integer()),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name="fk_accounts_userid_users"
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    # pass
    op.drop_table('accounts')
