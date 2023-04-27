"""Adds incident type specific documents.

Revision ID: 875e6b212dc7
Revises: 32811f581cb8
Create Date: 2021-07-01 10:19:24.016062

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "875e6b212dc7"
down_revision = "32811f581cb8"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "incident_type",
        "template_document_id",
        nullable=True,
        new_column_name="incident_template_document_id",
    )
    op.add_column(
        "incident_type", sa.Column("executive_template_document_id", sa.Integer(), nullable=True)
    )
    op.add_column(
        "incident_type", sa.Column("review_template_document_id", sa.Integer(), nullable=True)
    )
    op.add_column(
        "incident_type", sa.Column("tracking_template_document_id", sa.Integer(), nullable=True)
    )
    op.drop_constraint(
        "incident_type_template_document_id_fkey", "incident_type", type_="foreignkey"
    )
    op.create_foreign_key(
        None, "incident_type", "document", ["review_template_document_id"], ["id"]
    )
    op.create_foreign_key(
        None, "incident_type", "document", ["tracking_template_document_id"], ["id"]
    )
    op.create_foreign_key(
        None, "incident_type", "document", ["incident_template_document_id"], ["id"]
    )
    op.create_foreign_key(
        None, "incident_type", "document", ["executive_template_document_id"], ["id"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "incident_type",
        "incident_template_document_id",
        new_column_name="template_document_id",
        nullable=True,
    )
    op.create_foreign_key(
        "incident_type_template_document_id_fkey",
        "incident_type",
        "document",
        ["template_document_id"],
        ["id"],
    )
    op.drop_column("incident_type", "tracking_template_document_id")
    op.drop_column("incident_type", "review_template_document_id")
    op.drop_column("incident_type", "executive_template_document_id")
    op.drop_column("incident_type", "incident_template_document_id")
    # ### end Alembic commands ###