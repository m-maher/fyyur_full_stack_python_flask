"""empty message

Revision ID: f7de5e3c1632
Revises: ab14dedf1786
Create Date: 2020-03-31 22:50:38.079468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7de5e3c1632'
down_revision = 'ab14dedf1786'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'artist_venue_fkey', 'artist', type_='foreignkey')
    op.drop_column('artist', 'venue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('artist', sa.Column('venue', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key(u'artist_venue_fkey', 'artist', 'venue', ['venue'], ['id'])
    # ### end Alembic commands ###