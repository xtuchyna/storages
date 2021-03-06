"""add flag to indicate missing source code

Revision ID: c8017a5b43f1
Revises: 6389973bd8b6
Create Date: 2020-09-28 15:11:48.986072+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c8017a5b43f1"
down_revision = "6389973bd8b6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "python_package_version", sa.Column("is_downloadable", sa.Boolean(), nullable=False, server_default="true")
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("python_package_version", "is_downloadable")
    # ### end Alembic commands ###
