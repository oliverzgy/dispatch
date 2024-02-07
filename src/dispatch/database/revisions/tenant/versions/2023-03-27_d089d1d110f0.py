"""Adds signal case override

Revision ID: d089d1d110f0
Revises: d1b5ed66d83d
Create Date: 2023-03-27 16:16:04.098781

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "d089d1d110f0"
down_revision = "d1b5ed66d83d"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("signal", sa.Column("create_case", sa.Boolean(), nullable=True))
    op.add_column("signal", sa.Column("conversation_target", sa.String(), nullable=True))
    op.add_column("signal", sa.Column("oncall_service_id", sa.Integer(), nullable=True))
    op.create_foreign_key(None, "signal", "service", ["oncall_service_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "signal", type_="foreignkey")
    op.drop_column("signal", "oncall_service_id")
    op.drop_column("signal", "conversation_target")
    op.drop_column("signal", "create_case")
    # ### end Alembic commands ###
