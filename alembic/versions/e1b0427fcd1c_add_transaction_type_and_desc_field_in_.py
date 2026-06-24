"""add transaction type and desc field in transaction table

Revision ID: e1b0427fcd1c
Revises: 17379c676161
Create Date: 2026-06-23 16:09:33.052552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e1b0427fcd1c'
down_revision: Union[str, Sequence[str], None] = '17379c676161'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

transaction_type = sa.Enum(
    "deposit",
    "withdraw",
    "transfer",
    name="transaction_type"
)

def upgrade() -> None:
    """Upgrade schema."""
    transaction_type.create(op.get_bind(), checkfirst=True)

    # pass
    op.add_column(
        "transactions",
        sa.Column("transaction_type",
        transaction_type    
        )
    )
    op.add_column(
        "transactions",
        sa.Column("description",sa.String(length=50))
    )

def downgrade() -> None:
    """Downgrade schema."""
    # pass
