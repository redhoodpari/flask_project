"""empty message

Revision ID: 077deaa6da19
Revises: 
Create Date: 2018-07-15 22:57:20.389899

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '077deaa6da19'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('assetlocation',
    sa.Column('pri_id', sa.INTEGER(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('description', sa.VARCHAR(length=30), nullable=True),
    sa.Column('data_time', sa.TIMESTAMP(), nullable=True),
    sa.Column('longitude', sa.DECIMAL(), nullable=True),
    sa.Column('latitude', sa.DECIMAL(), nullable=True),
    sa.Column('elevation', sa.INTEGER(), nullable=True),
    sa.PrimaryKeyConstraint('pri_id')
    )
    op.drop_table('location')
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('username', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('email', mysql.VARCHAR(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.create_table('location',
    sa.Column('pri_id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('description', mysql.VARCHAR(length=80), nullable=True),
    sa.Column('data_time', mysql.DATETIME(), nullable=True),
    sa.Column('longtitude', mysql.DOUBLE(precision=9, scale=7, asdecimal=True), nullable=True),
    sa.Column('latitude', mysql.DOUBLE(precision=9, scale=7, asdecimal=True), nullable=True),
    sa.Column('elevation', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('pri_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    op.drop_table('assetlocation')
    # ### end Alembic commands ###