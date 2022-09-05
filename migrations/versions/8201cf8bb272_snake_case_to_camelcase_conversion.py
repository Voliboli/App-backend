"""snake_case to camelCase conversion

Revision ID: 8201cf8bb272
Revises: e7b326d65d8f
Create Date: 2022-09-05 17:35:16.074135

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8201cf8bb272'
down_revision = 'e7b326d65d8f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player_model', sa.Column('idPlayer', sa.Integer(), nullable=False))
    op.add_column('player_model', sa.Column('totalPoints', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('breakPoints', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('totalServe', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('errorServe', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('pointsServe', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('totalReception', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('errorReception', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('posReception', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('excReception', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('totalAttacks', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('errorAttacks', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('blockedAttacks', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('pointsAttack', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('posAttack', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('pointsBlock', sa.String(length=1000), nullable=True))
    op.add_column('player_model', sa.Column('pointsAvg', sa.Float(), nullable=True))
    op.add_column('player_model', sa.Column('attackAvg', sa.Float(), nullable=True))
    op.add_column('player_model', sa.Column('dateTeam', sa.String(length=1000), nullable=True))
    op.drop_constraint('player_model_id_player_key', 'player_model', type_='unique')
    op.create_unique_constraint(None, 'player_model', ['idPlayer'])
    op.drop_column('player_model', 'total_reception')
    op.drop_column('player_model', 'total_serve')
    op.drop_column('player_model', 'break_points')
    op.drop_column('player_model', 'exc_reception')
    op.drop_column('player_model', 'total_points')
    op.drop_column('player_model', 'points_serve')
    op.drop_column('player_model', 'id_player')
    op.drop_column('player_model', 'error_reception')
    op.drop_column('player_model', 'points_attack')
    op.drop_column('player_model', 'pos_attack')
    op.drop_column('player_model', 'error_attacks')
    op.drop_column('player_model', 'total_attacks')
    op.drop_column('player_model', 'points_block')
    op.drop_column('player_model', 'error_serve')
    op.drop_column('player_model', 'attack_avg')
    op.drop_column('player_model', 'date_team')
    op.drop_column('player_model', 'blocked_attacks')
    op.drop_column('player_model', 'points_avg')
    op.drop_column('player_model', 'pos_reception')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('player_model', sa.Column('pos_reception', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('points_avg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('blocked_attacks', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('date_team', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('attack_avg', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('error_serve', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('points_block', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('total_attacks', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('error_attacks', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('pos_attack', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('points_attack', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('error_reception', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('id_player', sa.INTEGER(), autoincrement=True, nullable=False))
    op.add_column('player_model', sa.Column('points_serve', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('total_points', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('exc_reception', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('break_points', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('total_serve', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.add_column('player_model', sa.Column('total_reception', sa.VARCHAR(length=1000), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'player_model', type_='unique')
    op.create_unique_constraint('player_model_id_player_key', 'player_model', ['id_player'])
    op.drop_column('player_model', 'dateTeam')
    op.drop_column('player_model', 'attackAvg')
    op.drop_column('player_model', 'pointsAvg')
    op.drop_column('player_model', 'pointsBlock')
    op.drop_column('player_model', 'posAttack')
    op.drop_column('player_model', 'pointsAttack')
    op.drop_column('player_model', 'blockedAttacks')
    op.drop_column('player_model', 'errorAttacks')
    op.drop_column('player_model', 'totalAttacks')
    op.drop_column('player_model', 'excReception')
    op.drop_column('player_model', 'posReception')
    op.drop_column('player_model', 'errorReception')
    op.drop_column('player_model', 'totalReception')
    op.drop_column('player_model', 'pointsServe')
    op.drop_column('player_model', 'errorServe')
    op.drop_column('player_model', 'totalServe')
    op.drop_column('player_model', 'breakPoints')
    op.drop_column('player_model', 'totalPoints')
    op.drop_column('player_model', 'idPlayer')
    # ### end Alembic commands ###