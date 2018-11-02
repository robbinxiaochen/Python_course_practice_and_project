from __future__ import absolute_import

from datetime import datetime

from pandas import read_sql
from sqlalchemy import Column, DateTime, Integer, Unicode, Float, ForeignKey,\
    UniqueConstraint,UnicodeText
from sqlalchemy.orm import relationship

from . import Base
from .reaction import Reaction

__all__ = ("pFBA_Solution",)


class pFBA_Solution(Base):

    __tablename__ = "pfba_solution"
    __table_args__ = (
        UniqueConstraint("experiment_id", "reaction_id"),
    )

    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"),
                           nullable=False)
    experiment = relationship("Experiment", lazy="selectin")
    reaction_id = Column(Integer, ForeignKey("reactions.id"), nullable=False)
    reaction = relationship("Reaction", lazy="selectin")
    flux = Column(Float, nullable=True)
    method = Column(UnicodeText, nullable=True)

    updated_on = Column(DateTime, nullable=True, onupdate=datetime.now())

    @classmethod
    def load_data_frame(cls, experiment, session):
        query = session.query(pFBA_Solution.flux, Reaction.identifier). \
            join(pFBA_Solution). \
            filter(Solution.experiment == experiment)
        return read_sql(query.statement, session.bind, index_col="identifier")