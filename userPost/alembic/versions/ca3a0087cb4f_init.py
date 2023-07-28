"""init

Revision ID: ca3a0087cb4f
Revises: 
Create Date: 2023-07-27 07:08:19.970229

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca3a0087cb4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('uid',sa.Integer, primary_key=True, index=True),
        sa.Column('email',sa.String, nullable=False),
        sa.Column('password',sa.String, nullable=False),
        sa.Column('created_time',sa.Datetime(), server_default=sa.func.now())
    )

    op.create_table(
        'posts',
        sa.Column('pid',sa.Integer, primary_key=True, index=True),
        sa.Column('title',sa.String, nullable=False),
        sa.Column('content',sa.String, nullable=False),
        sa.Column('published',sa.Boolean, nullable=False),
        sa.Column('created_time',sa.Datetime(), server_default=sa.func.now()),
    )

def downgrade():
    op.drop_table('users')
    op.drop_table('posts')
