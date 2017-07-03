""" Add Token

Revision ID: 1e66b89ce4f
Revises: 47c4fdb08f6
Create Date: 2017-07-03 20:24:15.531694

"""

# revision identifiers, used by Alembic.
revision = '1e66b89ce4f'
down_revision = '47c4fdb08f6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('token_type', sa.String(length=40), nullable=True),
    sa.Column('access_token', sa.String(length=255), nullable=True),
    sa.Column('refresh_token', sa.String(length=255), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('_scopes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.client_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('access_token'),
    sa.UniqueConstraint('refresh_token')
    )


def downgrade():
    op.drop_table('token')
