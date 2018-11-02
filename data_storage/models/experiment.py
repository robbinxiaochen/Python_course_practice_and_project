from __future__ import absolute_import

import logging

from sqlalchemy import Column, Integer, Unicode, ForeignKey, Table, UnicodeText
from sqlalchemy.orm import relationship

from . import Base
from .mixins import UUIDMixin

__all__ = ("Experiment",)

LOGGER = logging.getLogger(__name__)


experiment_reaction_bounds_association = Table(
    "experiment_reaction_bounds_association",
    Base.metadata,
    Column("experiment_id", Integer, ForeignKey("experiments.id")),
    Column("reaction_bound_id", Integer, ForeignKey("reaction_bounds.id"))
)

class Experiment(UUIDMixin, Base):

    __tablename__ = "experiments"

    id = Column(Integer, primary_key=True)
    objective = Column(Unicode(255), nullable=False)
    #method = Column(Unicode(255), nullable=False)
    solver = Column(Unicode(20), nullable=True)
    description = Column(UnicodeText, nullable=True)
    medium_id = Column(Integer, ForeignKey("media.id"), nullable=False)
    medium = relationship("Medium", lazy="selectin")
    constraints = relationship(
        "ReactionBound",
        secondary=experiment_reaction_bounds_association,
        lazy="selectin"
    )

    def adjust_model(self, model):
        if self.solver is not None:
            LOGGER.debug("Set solver to '%s'.", self.solver)
            model.solver = self.solver
        LOGGER.debug("Set objective to '%s'.", self.objective)
        model.objective = model.reactions.get_by_id(self.objective)
        LOGGER.debug("Set medium.")
        for rxn_bound in self.medium.components:
            rxn = model.reactions.get_by_id(rxn_bound.identifier)
            rxn.bounds = rxn_bound.lower, rxn_bound.upper

    def constrain_model(self, model):
        LOGGER.debug("Set additional constraints.")
        for rxn_bound in self.constraints:
            rxn = model.reactions.get_by_id(rxn_bound.identifier)
            rxn.bounds = rxn_bound.lower, rxn_bound.upper