"""add context to the post table

Revision ID: 6345af6bf68a
Revises: 6df13b747f79
Create Date: 2024-11-07 20:27:21.846287

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6345af6bf68a'
down_revision: Union[str, None] = '6df13b747f79'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
