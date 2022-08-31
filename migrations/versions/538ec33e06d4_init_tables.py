"""init tables

Revision ID: 538ec33e06d4
Revises:
Create Date: 2021-08-18 06:48:26.249946

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '538ec33e06d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(length=64), nullable=True),
    sa.Column('student_email', sa.String(length=64), nullable=True),
    sa.Column('parent_name', sa.String(length=64), nullable=True),
    sa.Column('parent_email', sa.String(length=64), nullable=True),
    sa.Column('timezone', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=32), nullable=True),
    sa.Column('last_name', sa.String(length=32), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=32), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('about_me', sa.String(length=500), nullable=True),
    sa.Column('last_viewed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_email'), ['email'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_first_name'), ['first_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_last_name'), ['last_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_phone'), ['phone'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_phone'))
        batch_op.drop_index(batch_op.f('ix_user_last_name'))
        batch_op.drop_index(batch_op.f('ix_user_first_name'))
        batch_op.drop_index(batch_op.f('ix_user_email'))

    op.drop_table('user')
    op.drop_table('student')
    # ### end Alembic commands ###