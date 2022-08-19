"""Init

Revision ID: 3991ccf968c5
Revises: 
Create Date: 2022-08-18 22:58:29.678439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3991ccf968c5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'document',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('Вид документа', sa.Unicode(300)),
        sa.Column('Объект', sa.Unicode(300)),
        sa.Column('Автор', sa.String(100)),
        sa.Column('Организация', sa.String(100)),
        sa.Column('Исполнитель', sa.String(100)),
        sa.Column('Задача', sa.Unicode(300)),
        sa.Column('Дата выдачи', sa.DateTime),
        sa.Column('Дата выполнения (план)',sa.DateTime),
        sa.Column('Дата выполнения (факт)', sa.DateTime),
        sa.Column('Просрочена, ч', sa.Float, nullable=False),
        sa.Column('Резолюция', sa.String(100)),
        sa.Column('Выполнена автоматически', sa.String(100)),
        sa.Column('Договор по шаблону', sa.String(100)),
        sa.Column('Состояние', sa.String(100)),
        sa.Column('Дата', sa.DateTime),
        sa.Column('Дата завершения', sa.DateTime),
        sa.Column('Завершен', sa.Boolean)
    )


def downgrade() -> None:
    op.drop_table('document')
