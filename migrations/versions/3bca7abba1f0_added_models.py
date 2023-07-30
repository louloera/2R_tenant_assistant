"""added models

Revision ID: 3bca7abba1f0
Revises: 
Create Date: 2023-07-30 12:24:06.839721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bca7abba1f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('hosts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('initiation_date', sa.DateTime(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('homes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('host_id', sa.Integer(), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('checkout_time', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['host_id'], ['hosts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Items',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('home_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['home_id'], ['homes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Towels',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('home_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['home_id'], ['homes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Trash',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('days', sa.String(), nullable=True),
    sa.Column('time', sa.Integer(), nullable=True),
    sa.Column('home_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['home_id'], ['homes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Trash')
    op.drop_table('Towels')
    op.drop_table('Items')
    op.drop_table('homes')
    op.drop_table('hosts')
    # ### end Alembic commands ###
