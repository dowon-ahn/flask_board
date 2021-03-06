"""empty message

Revision ID: 2c6cbd7f6c7d
Revises: fa44be00b0f7
Create Date: 2020-10-03 03:19:25.770550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c6cbd7f6c7d'
down_revision = 'fa44be00b0f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'question', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'question', type_='foreignkey')
    op.drop_column('question', 'user_id')
    # ### end Alembic commands ###
