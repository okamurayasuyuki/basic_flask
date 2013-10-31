"""a

Revision ID: 25fbe740ffa7
Revises: f3786481d2
Create Date: 2013-10-31 11:36:19.661109
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '25fbe740ffa7'
down_revision = 'f3786481d2'


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=30), nullable=True),
    sa.Column('path', sa.String(length=120), nullable=True),
    sa.Column('img_path', sa.String(length=120), nullable=True),
    sa.Column('desc', sa.String(length=400), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('has_voted', sa.Boolean(), nullable=True),
    sa.Column('is_owner', sa.Boolean(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('videotags',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['videos.id'], ),
    sa.PrimaryKeyConstraint()
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videotags')
    op.drop_table('votes')
    op.drop_table('videos')
    op.drop_table('tags')
    ### end Alembic commands ###
