"""Add User model

Revision ID: 1625cff230b
Revises: 4f2e2c180af
Create Date: 2017-06-30 18:53:30.061501

"""

# revision identifiers, used by Alembic.
revision = '1625cff230b'
down_revision = '4f2e2c180af'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )


def downgrade():
    op.drop_table('user')
