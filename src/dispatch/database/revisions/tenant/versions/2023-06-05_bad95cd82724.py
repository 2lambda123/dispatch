"""Adds entity type scoping.

Revision ID: bad95cd82724
Revises: 9ad021045e45
Create Date: 2023-06-05 08:48:53.486613

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "bad95cd82724"
down_revision = "9ad021045e45"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("entity_type", sa.Column("scope", sa.String(), nullable=True))
    op.execute("UPDATE entity_type SET scope = 'multiple'")
    op.alter_column("entity_type", "scope", nullable=False)
    op.drop_column("entity_type", "global_find")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "entity_type", sa.Column("global_find", sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.drop_column("entity_type", "scope")
    # ### end Alembic commands ###
