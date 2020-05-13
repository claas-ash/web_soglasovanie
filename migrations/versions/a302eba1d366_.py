"""empty message

Revision ID: a302eba1d366
Revises: df0e707ba136
Create Date: 2020-05-12 16:08:44.306440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a302eba1d366'
down_revision = 'df0e707ba136'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_soglasovanie_task_bp_id'), 'soglasovanie_task', ['bp_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_soglasovanie_task_bp_id'), table_name='soglasovanie_task')
    # ### end Alembic commands ###
