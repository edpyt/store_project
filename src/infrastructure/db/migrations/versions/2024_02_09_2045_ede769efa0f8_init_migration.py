"""init migration

Revision ID: ede769efa0f8
Revises:
Create Date: 2024-02-09 20:45:46.787680

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils



# revision identifiers, used by Alembic.
revision: str = 'ede769efa0f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('status', sqlalchemy_utils.types.choice.ChoiceType(length=255), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_order'))
    )
    op.create_table('product',
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('price', sa.Numeric(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.CheckConstraint('price >= 0', name=op.f('ck_product_check_cost_positive')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_product'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('order')
    # ### end Alembic commands ###
