# -*- coding: utf-8 -*- 

"""Pipeline scripts intended for use on computerome."""

from __future__ import absolute_import

import logging
from os.path import join, dirname, pardir

from pandas import read_excel
from tqdm import tqdm

from .. import models

LOGGER = logging.getLogger(__name__)
PROJECT_ROOT = join(dirname(__file__), pardir, pardir, pardir)


def create_media(model, session):
    media = dict()
    
    
    # M9 + glucose
    LOGGER.debug("Create M9 minimal medium + glucose.")
    medium = models.Medium(name="M9 minimal medium + glucose")
    for rxn in tqdm(model.exchanges, desc="Medium Components"):
        if not rxn.id.startswith("EX"):
            continue
        medium.components.append( models.ReactionBound(identifier=rxn.id,                                      lower=rxn.lower_bound,                                                 upper=rxn.upper_bound))
    media["m9_glc"] = medium
    session.add(medium)
    session.commit()
    
    # M9 + citrate
    LOGGER.debug("Create M9 minimal medium + citrate.")
    medium = models.Medium(name="M9 minimal medium + citrate")
    with model:
        model.reactions.EX_glc_e_.bounds = 0, 0
        model.reactions.EX_cit_e_.bounds = -10.0, 99999.0
        for rxn in tqdm(model.exchanges, desc="Medium Components"):
            if not rxn.id.startswith("EX"):
                continue
            medium.components.append(
                    models.ReactionBound(identifier=rxn.id, lower=rxn.lower_bound,
                                     upper=rxn.upper_bound))
    media["m9_cit"] = medium
    session.add(medium)
    session.commit()
    
    # M9 + Gluconate(1.0)
    LOGGER.debug("Create M9 minimal medium + gluconate (1.0).")
    medium = models.Medium(name="M9 minimal medium + gluconate (1.0)")
    with model:
        model.reactions.EX_glc_e_.bounds = 0, 0
        model.reactions.EX_glcn_e_.bounds = -1.0, 99999.0
        for rxn in tqdm(model.exchanges, desc="Medium Components"):
            if not rxn.id.startswith("EX"):
                continue
            medium.components.append(
                  models.ReactionBound(identifier=rxn.id, lower=rxn.lower_bound,
                                     upper=rxn.upper_bound))
    media["m9_glu_1.0"] = medium
    session.add(medium)
    session.commit()
    
    # M9 + Gluconate(5.51)
    LOGGER.debug("Create M9 minimal medium + gluconate (5.51).")
    medium = models.Medium(name="M9 minimal medium + gluconate (5.51)")
    with model:
        model.reactions.EX_glc_e_.bounds = 0, 0
        model.reactions.EX_glcn_e_.bounds = -5.51, 99999.0
        for rxn in tqdm(model.exchanges, desc="Medium Components"):
            if not rxn.id.startswith("EX"):
                continue
            medium.components.append(
                models.ReactionBound(identifier=rxn.id, lower=rxn.lower_bound,
                                     upper=rxn.upper_bound))
    media["m9_glu_5.51"] = medium
    session.add(medium)
    session.commit()
    
    
    # M9 + Ketogluconate(1.0)
    LOGGER.debug("Create M9 minimal medium + Ketogluconate (1.0).")
    medium = models.Medium(name="M9 minimal medium + Ketogluconate (1.0)")
    with model:
        model.reactions.EX_glc_e_.bounds = 0, 0
        model.reactions.EX_2dhglcn_e_.bounds = -1.0, 99999.0
        for rxn in tqdm(model.exchanges, desc="Medium Components"):
            if not rxn.id.startswith("EX"):
                continue
            medium.components.append(
                      models.ReactionBound(identifier=rxn.id, lower=rxn.lower_bound,
                                     upper=rxn.upper_bound))
    media["m9_ketoglu_1.0"] = medium
    session.add(medium)
    session.commit()
    
    # M9 + Ketogluconate(5.51)
    LOGGER.debug("Create M9 minimal medium + Ketogluconate (5.51).")
    medium = models.Medium(name="M9 minimal medium + Ketogluconate (5.51)")
    with model:
        model.reactions.EX_glc_e_.bounds = 0, 0
        model.reactions.EX_2dhglcn_e_.bounds = -5.51, 99999.0
        for rxn in tqdm(model.exchanges, desc="Medium Components"):
            if not rxn.id.startswith("EX"):
                continue
            medium.components.append(
                    models.ReactionBound(identifier=rxn.id, lower=rxn.lower_bound,
                                     upper=rxn.upper_bound))
    media["m9_ketoglu_5.51"] = medium
    session.add(medium)
    session.commit()
    
    
    
    
    return media

    