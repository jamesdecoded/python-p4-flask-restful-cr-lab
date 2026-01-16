"""add columns to plants table

Revision ID: 20260116_plants
Revises: 67f5d67aea55
Create Date: 2026-01-16 10:29:45

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20260116_plants'
down_revision = '67f5d67aea55'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('plants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('plants')
