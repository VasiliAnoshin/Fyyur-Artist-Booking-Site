"""empty message

Revision ID: ca866253ef3b
Revises: 4835a04f88dc
Create Date: 2019-11-24 12:56:37.399077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca866253ef3b'
down_revision = '4835a04f88dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'num_upcoming_shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('num_upcoming_shows', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
