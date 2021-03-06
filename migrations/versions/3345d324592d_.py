"""empty message

Revision ID: 3345d324592d
Revises: 
Create Date: 2019-06-03 13:32:13.345633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3345d324592d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('airline',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('name_abb', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('firstname', sa.String(length=120), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('tel', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('profile', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('flight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('airline', sa.Integer(), nullable=False),
    sa.Column('departure_time', sa.Time(), nullable=False),
    sa.Column('departure_date', sa.Date(), nullable=False),
    sa.Column('arrival_time', sa.Time(), nullable=False),
    sa.Column('departure_location', sa.String(length=50), nullable=False),
    sa.Column('arrival_location', sa.String(length=50), nullable=False),
    sa.Column('flight_code', sa.String(length=10), nullable=False),
    sa.Column('no_of_seats', sa.Integer(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('status', sa.Enum('cancelled', 'active', 'unknown', name='myenum'), nullable=False),
    sa.ForeignKeyConstraint(['airline'], ['airline.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('flight_code')
    )
    op.create_table('flight_seats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=False),
    sa.Column('flight_code', sa.String(), nullable=False),
    sa.Column('seat', sa.String(length=3), nullable=False),
    sa.Column('is_available', sa.Boolean(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['flight_code'], ['flight.flight_code'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flight_seats')
    op.drop_table('flight')
    op.drop_table('user')
    op.drop_table('airline')
    # ### end Alembic commands ###
