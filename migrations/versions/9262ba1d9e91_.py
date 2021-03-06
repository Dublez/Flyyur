"""empty message

Revision ID: 9262ba1d9e91
Revises: a61fa617b3a3
Create Date: 2021-08-11 13:29:17.931312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9262ba1d9e91'
down_revision = 'a61fa617b3a3'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist_shows')
    op.drop_table('venue_city')
    op.drop_table('venue_shows')
    # ### end Alembic commands ###


def downgrade():
    # return 0
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('venue_shows',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('show_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['show_id'], ['Show.id'], name='venue_shows_show_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], name='venue_shows_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'show_id', name='venue_shows_pkey')
    )
    op.create_table('venue_city',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('city_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['City.id'], name='venue_city_city_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.id'], name='venue_city_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'city_id', name='venue_city_pkey')
    )
    op.create_table('artist_shows',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('show_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], name='artist_shows_artist_id_fkey'),
    sa.ForeignKeyConstraint(['show_id'], ['Show.id'], name='artist_shows_show_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'show_id', name='artist_shows_pkey')
    )
    ### end Alembic commands ###
