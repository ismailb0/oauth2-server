""" Add Grant Token table

Revision ID: 47c4fdb08f6
Revises: 6b37b664f1
Create Date: 2017-06-30 22:51:10.752072

"""

# revision identifiers, used by Alembic.
revision = '47c4fdb08f6'
down_revision = '6b37b664f1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('grant_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('code', sa.String(length=255), nullable=False),
    sa.Column('redirect_uri', sa.String(length=255), nullable=True),
    sa.Column('expires', sa.DateTime(), nullable=True),
    sa.Column('_scopes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.client_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grant_token_code'), 'grant_token', ['code'], unique=False)


def downgrade():
    op.drop_index(op.f('ix_grant_token_code'), table_name='grant_token')
    op.drop_table('grant_token')
