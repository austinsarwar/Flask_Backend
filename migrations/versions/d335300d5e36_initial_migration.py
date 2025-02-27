"""Initial migration.

Revision ID: d335300d5e36
Revises: 
Create Date: 2024-10-26 15:08:15.782130

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd335300d5e36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('UserGoal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('weight_goal', sa.String(length=64), nullable=True),
    sa.Column('cardio_goal', sa.String(length=64), nullable=True),
    sa.Column('resistance_goal', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('UserInfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('sex', sa.String(length=10), nullable=False),
    sa.Column('diet', sa.String(length=64), nullable=True),
    sa.Column('activity_level', sa.String(length=64), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('UserMealPlanPreferences',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('food_preferences', sa.String(length=256), nullable=True),
    sa.Column('food_avoidances', sa.String(length=256), nullable=True),
    sa.Column('meals_per_day', sa.Integer(), nullable=True),
    sa.Column('plan_length', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['Users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('UserNutrition',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('calories', sa.Integer(), nullable=False),
    sa.Column('protein', sa.Float(), nullable=False),
    sa.Column('fat', sa.Float(), nullable=False),
    sa.Column('carbs', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['Users.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('UserNutrition')
    op.drop_table('UserMealPlanPreferences')
    op.drop_table('UserInfo')
    op.drop_table('UserGoal')
    op.drop_table('Users')
    # ### end Alembic commands ###
