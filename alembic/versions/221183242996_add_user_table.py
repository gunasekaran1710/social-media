"""add user table

Revision ID: 221183242996
Revises: 6345af6bf68a
Create Date: 2024-11-07 22:26:35.744639

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '221183242996'
down_revision: Union[str, None] = '6345af6bf68a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',sa.Column('id',sa.Integer(),nullable=False),sa.Column('email',sa.String(),nullable=False),sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
