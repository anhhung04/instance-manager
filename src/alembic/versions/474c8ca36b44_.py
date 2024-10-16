"""empty message

Revision ID: 474c8ca36b44
Revises: 
Create Date: 2024-09-23 15:08:47.517257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '474c8ca36b44'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('challenges',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('running', 'stop', name='status'), nullable=True),
    sa.Column('connection_info', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_challenges_id'), 'challenges', ['id'], unique=False)
    op.create_index(op.f('ix_challenges_title'), 'challenges', ['title'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('display_name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_display_name'), 'users', ['display_name'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_table('joins',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('joined_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_joins_id'), 'joins', ['id'], unique=False)
    op.create_table('services',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('image', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('challenge_id', sa.Integer(), nullable=True),
    sa.Column('privileged', sa.Boolean(), nullable=True),
    sa.Column('cpu', sa.String(), nullable=True),
    sa.Column('memory', sa.String(), nullable=True),
    sa.Column('ports', sa.String(), nullable=False),
    sa.Column('environment', sa.String(), nullable=False),
    sa.Column('cap_add', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['challenge_id'], ['challenges.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_services_id'), 'services', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_services_id'), table_name='services')
    op.drop_table('services')
    op.drop_index(op.f('ix_joins_id'), table_name='joins')
    op.drop_table('joins')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_display_name'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_challenges_title'), table_name='challenges')
    op.drop_index(op.f('ix_challenges_id'), table_name='challenges')
    op.drop_table('challenges')
    # ### end Alembic commands ###
