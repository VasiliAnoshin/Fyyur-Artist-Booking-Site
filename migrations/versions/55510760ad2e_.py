"""empty message

Revision ID: 55510760ad2e
Revises: ce68ecdb4c03
Create Date: 2019-11-30 14:37:44.214875

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55510760ad2e'
down_revision = 'ce68ecdb4c03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=360), nullable=True))
    op.add_column('Artist', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('website', sa.String(length=120), nullable=True))
    op.execute('Update "Artist" SET seeking_talent = False WHERE seeking_talent IS NULL;')
    op.alter_column('Artist','seeking_talent', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'seeking_talent')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
