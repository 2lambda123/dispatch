"""Removes total_cost column in favor of hybrid property

Revision ID: 5e2bc6083503
Revises: 748744207122
Create Date: 2022-05-26 17:18:29.231995

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "5e2bc6083503"
down_revision = "748744207122"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("incident", "total_cost")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "incident", sa.Column("total_cost", sa.NUMERIC(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
