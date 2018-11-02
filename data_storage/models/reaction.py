from __future__ import absolute_import

import logging

from sqlalchemy import Column, Integer, Unicode

from . import Base

__all__ = ("Reaction",)

LOGGER = logging.getLogger(__name__)


class Reaction(Base):

    __tablename__ = "reactions"

    id = Column(Integer, primary_key=True)
    identifier = Column(Unicode(255), nullable=False, unique=True, index=True)

    @classmethod
    def populate(cls, model, session):
        if session.query(cls).count() == 0:
            LOGGER.debug("Creating reactions from metabolic model.")
            reactions = [{"identifier": r.id} for r in model.reactions]
            session.execute(cls.__table__.insert(), reactions)
        return session.query(cls).all()