"""add columns to table

Revision ID: 8e16afb1d3b0
Revises: 77747ec6da5a
Create Date: 2023-10-01 02:09:28.033252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e16afb1d3b0'
down_revision = '77747ec6da5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('plants', sa.Column('name', sa.String(), nullable=True))
    op.add_column('plants', sa.Column('image', sa.String(), nullable=True))
    op.add_column('plants', sa.Column('price', sa.Float(), nullable=True))
    op.add_column('plants', sa.Column('is_in_stock', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('plants', 'is_in_stock')
    op.drop_column('plants', 'price')
    op.drop_column('plants', 'image')
    op.drop_column('plants', 'name')
    # ### end Alembic commands ###
