# -*- coding: utf-8 -*-

from __future__ import absolute_import

from sqlalchemy import Column, Integer, Unicode, Float

from . import Base

__all__ = ("ReactionBound",)


class ReactionBound(Base):

    __tablename__ = "reaction_bounds"

    id = Column(Integer, primary_key=True)
    identifier = Column(Unicode(255), nullable=False, index=True)
    lower = Column(Float, nullable=True, default=0.0)
    upper = Column(Float, nullable=True, default=0.0)