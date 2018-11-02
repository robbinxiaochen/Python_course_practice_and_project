from __future__ import absolute_import

from sqlalchemy import Column, Integer, Unicode, UnicodeText, Table, ForeignKey
from sqlalchemy.orm import relationship

from . import Base
from .mixins import UUIDMixin

__all__ = ("Medium",)


medium_reaction_bounds_association = Table(
    "medium_reaction_bounds_association",
    Base.metadata,
    Column("medium_id", Integer, ForeignKey("media.id")),
    Column("reaction_bound_id", Integer, ForeignKey("reaction_bounds.id"))
)


class Medium(UUIDMixin, Base):

    __tablename__ = "media"

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=True)
    description = Column(UnicodeText, nullable=True)
    components = relationship(
        "ReactionBound",
        secondary=medium_reaction_bounds_association,
        lazy="selectin"
    )