"""Added trash and towel to home

Revision ID: 15c4aaebf2d3
Revises: 3bca7abba1f0
Create Date: 2023-07-30 14:45:12.463888

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '15c4aaebf2d3'
down_revision = '3bca7abba1f0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('hosts', 'initiation_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hosts', sa.Column('initiation_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###