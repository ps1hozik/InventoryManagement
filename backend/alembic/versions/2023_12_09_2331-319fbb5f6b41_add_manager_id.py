"""add manager_id

Revision ID: 319fbb5f6b41
Revises: ed6815a04f7f
Create Date: 2023-12-09 23:31:58.437947

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '319fbb5f6b41'
down_revision: Union[str, None] = 'ed6815a04f7f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
