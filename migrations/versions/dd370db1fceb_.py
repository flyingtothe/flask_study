"""empty message

Revision ID: dd370db1fceb
Revises: aa3d94c455cf
Create Date: 2018-10-26 15:29:39.087415

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dd370db1fceb'
down_revision = 'aa3d94c455cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('answer', 'create_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('answer', sa.Column('create_time', mysql.DATETIME(), nullable=True))
    # ### end Alembic commands ###