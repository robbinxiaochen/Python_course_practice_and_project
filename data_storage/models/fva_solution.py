from __future__ import absolute_import

from datetime import datetime

from pandas import read_sql
from sqlalchemy import Column, DateTime, Integer, Unicode, Float, ForeignKey,\
    UniqueConstraint
from sqlalchemy.orm import relationship

from . import Base
from .reaction import Reaction

__all__ = ("FvaSolution",)


class FvaSolution(Base):

    __tablename__ = "fva_solution"
    __table_args__ = (
        UniqueConstraint("experiment_id", "reaction_id"),
    )

    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey("experiments.id"), nullable=False)
    experiment = relationship("Experiment", lazy="selectin")
    reaction_id = Column(Integer, ForeignKey("reactions.id"), nullable=False)
    reaction = relationship("Reaction", lazy="selectin")
    maximum = Column(Float, nullable=True)
    minimum = Column(Float, nullable=True)
    updated_on = Column(DateTime, nullable=True, onupdate=datetime.now())

    @classmethod
    def load_data_frame(cls, experiment, session):
        query = session.query(FvaSolution.maximum, FvaSolution.minimum,
                              Reaction.identifier). \
            join(Reaction). \
            filter(FvaSolution.experiment == experiment)
        return read_sql(query.statement, session.bind, index_col="identifier")