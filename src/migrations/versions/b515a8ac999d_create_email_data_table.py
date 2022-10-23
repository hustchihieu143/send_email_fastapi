"""create email_data table

Revision ID: b515a8ac999d
Revises: e84a7d29e98f
Create Date: 2022-10-23 21:16:35.188095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b515a8ac999d'
down_revision = 'e84a7d29e98f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('email_data',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('receiver_id', sa.INTEGER(), nullable=False),
    sa.Column('sender', sa.VARCHAR(length=255), nullable=False),
    sa.Column('content', sa.VARCHAR(length=255), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('email_data')
