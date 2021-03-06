"""Create index for CVE step

Revision ID: af2b9e09e53e
Revises: 9fea7ca59f56
Create Date: 2020-01-08 13:25:27.881950+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "af2b9e09e53e"
down_revision = "9fea7ca59f56"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(
        "has_vulnerability_python_package_version_entity_idx",
        "has_vulnerability",
        ["python_package_version_entity_id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("has_vulnerability_python_package_version_entity_idx", table_name="has_vulnerability")
    # ### end Alembic commands ###
