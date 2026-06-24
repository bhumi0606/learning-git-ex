"""create transaction table

Revision ID: 17379c676161
Revises: 0fad754b5451
Create Date: 2026-06-23 12:31:46.564213

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17379c676161'
down_revision: Union[str, Sequence[str], None] = '0fad754b5451'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass
    op.create_table(
        "transactions",
        sa.Column("transaction_id",sa.Integer(),primary_key=True),
        sa.Column("sender_account_number",sa.String(),nullable=False),
        sa.Column("receiver_account_number",sa.String(),nullable=True),
        sa.Column("amount",sa.Integer()),
        sa.Column("created_at",sa.DateTime),
        sa.ForeignKeyConstraint(
            ["sender_account_number"],
            ["accounts.account_number"],
            name="fk_transaction_sender_number_account"
        ),
        sa.ForeignKeyConstraint(
            ["receiver_account_number"],
            ["accounts.account_number"],
            name="fk_transaction_receiver_number_account"
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    # pass
    op.drop_table("transactions")
