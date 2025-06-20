"""create a posts table

Revision ID: 19060078964d
Revises: 
Create Date: 2025-06-12 13:52:35.774116

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19060078964d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table('posts',sa.Column('id',sa.Integer(),nullable=False,primary_key=True)
                    ,sa.Column('title',sa.String,nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('posts')
    pass
