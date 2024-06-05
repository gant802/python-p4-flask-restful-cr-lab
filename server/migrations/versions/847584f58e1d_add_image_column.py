"""add image column

Revision ID: 847584f58e1d
Revises: 03b1a0a6d4fb
Create Date: 2024-06-05 11:13:20.874215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '847584f58e1d'
down_revision = '03b1a0a6d4fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('plants', schema=None) as batch_op:
        batch_op.drop_column('image')

    # ### end Alembic commands ###
