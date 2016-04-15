"""empty message

Revision ID: 3954cbd1bf17
Revises: None
Create Date: 2016-04-15 21:01:13.083648

"""

# revision identifiers, used by Alembic.
revision = '3954cbd1bf17'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('devicename', sa.String(), nullable=True),
    sa.Column('deviceid', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('statuscode', sa.Integer(), nullable=True),
    sa.Column('statusmessage', sa.String(), nullable=True),
    sa.Column('statusaction', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('statuses')
    op.drop_table('devices')
    ### end Alembic commands ###