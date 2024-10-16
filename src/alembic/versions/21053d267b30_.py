"""empty message

Revision ID: 21053d267b30
Revises: 474c8ca36b44
Create Date: 2024-09-23 15:09:10.374047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21053d267b30'
down_revision: Union[str, None] = '474c8ca36b44'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('challenges', sa.Column('visible', sa.Boolean(), nullable=True))
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'is_admin')
    op.drop_column('challenges', 'visible')
    # ### end Alembic commands ###
