"""Add a foreign key in 'posts'

Revision ID: 141edd866463
Revises: ca3a0087cb4f
Create Date: 2023-07-27 12:19:28.979719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '141edd866463'
down_revision = 'ca3a0087cb4f'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('uid', sa.Integer))

    op.create_foreign_key(
        'fk_user_post', 
        'posts',                  
        'users',                
        ['uid'],             
        ['uid'],             
    )


def downgrade():
    op.drop_constraint('fk_user_post', 'posts', type_='foreignkey')

    op.drop_column('posts', 'uid')
