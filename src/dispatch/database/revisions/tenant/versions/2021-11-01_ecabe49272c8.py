"""Adds exclusive tag types

Revision ID: ecabe49272c8
Revises: f95247c63eda
Create Date: 2021-11-01 15:11:53.675447

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "ecabe49272c8"
down_revision = "f95247c63eda"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("tag_type", sa.Column("exclusive", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("tag_type", "exclusive")
    # ### end Alembic commands ###