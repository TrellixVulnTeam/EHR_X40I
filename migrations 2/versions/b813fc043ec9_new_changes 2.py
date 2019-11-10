"""new_changes

Revision ID: b813fc043ec9
Revises: b2ff149792c8
Create Date: 2019-10-31 09:06:10.812156

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b813fc043ec9'
down_revision = 'b2ff149792c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prescription',
    sa.Column('prescription_id', sa.Integer(), nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('physician_id', sa.Integer(), nullable=False),
    sa.Column('date_prescribed', sa.Date(), nullable=False),
    sa.Column('expir_date', sa.Date(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patient.user_id'], ),
    sa.ForeignKeyConstraint(['physician_id'], ['physician.user_id'], ),
    sa.PrimaryKeyConstraint('prescription_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('prescription')
    # ### end Alembic commands ###
