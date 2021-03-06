"""create tables

Revision ID: d8d7ebf499c8
Revises: 1ebbbd90b77e
Create Date: 2018-06-30 17:26:31.255437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8d7ebf499c8'
down_revision = '1ebbbd90b77e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('img',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('imgname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('img')
    # ### end Alembic commands ###
