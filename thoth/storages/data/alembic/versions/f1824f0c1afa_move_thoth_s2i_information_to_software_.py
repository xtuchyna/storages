"""Move Thoth s2i information to software environment

Revision ID: f1824f0c1afa
Revises: b957aa9cce3e
Create Date: 2021-01-29 08:10:11.514624+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f1824f0c1afa"
down_revision = "b957aa9cce3e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("external_software_environment", sa.Column("thoth_s2i_image_name", sa.Text(), nullable=True))
    op.add_column("external_software_environment", sa.Column("thoth_s2i_image_version", sa.Text(), nullable=True))
    op.drop_column("package_extract_run", "thoth_s2i_image_name")
    op.drop_column("package_extract_run", "thoth_s2i_image_version")
    op.add_column("software_environment", sa.Column("thoth_s2i_image_name", sa.Text(), nullable=True))
    op.add_column("software_environment", sa.Column("thoth_s2i_image_version", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("software_environment", "thoth_s2i_image_version")
    op.drop_column("software_environment", "thoth_s2i_image_name")
    op.add_column(
        "package_extract_run", sa.Column("thoth_s2i_image_version", sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.add_column(
        "package_extract_run", sa.Column("thoth_s2i_image_name", sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.drop_column("external_software_environment", "thoth_s2i_image_version")
    op.drop_column("external_software_environment", "thoth_s2i_image_name")
    # ### end Alembic commands ###
