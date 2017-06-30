"""Add Client model

Revision ID: 6b37b664f1
Revises: 1625cff230b
Create Date: 2017-06-30 22:21:36.645086

"""

# revision identifiers, used by Alembic.
revision = '6b37b664f1'
down_revision = '1625cff230b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('client',
    sa.Column('name', sa.String(length=40), nullable=True),
    sa.Column('description', sa.String(length=400), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.String(length=40), nullable=False),
    sa.Column('client_secret', sa.String(length=55), nullable=False),
    sa.Column('is_confidential', sa.Boolean(), nullable=True),
    sa.Column('_redirect_uris', sa.Text(), nullable=True),
    sa.Column('_default_scopes', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('client_id')
    )
    op.create_index(op.f('ix_client_client_secret'), 'client', ['client_secret'], unique=True)


def downgrade():
    op.drop_index(op.f('ix_client_client_secret'), table_name='client')
    op.drop_table('client')
