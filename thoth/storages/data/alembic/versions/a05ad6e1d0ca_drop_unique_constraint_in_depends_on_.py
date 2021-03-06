"""Drop unique constraint in depends_on table

Revision ID: a05ad6e1d0ca
Revises: bcf07d69fc15
Create Date: 2019-10-26 13:21:16.421540+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a05ad6e1d0ca"
down_revision = "bcf07d69fc15"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("depends_on_entity_id_version_id_version_range_key", "depends_on", type_="unique")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(
        "depends_on_entity_id_version_id_version_range_key", "depends_on", ["entity_id", "version_id", "version_range"]
    )
    # ### end Alembic commands ###
