# -*- coding: utf-8 -*-

from __future__ import absolute_import

import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from .reaction import *
from .reaction_bound import *
from .medium import *
from .experiment import *
from .fva_solution import *
from .pfba_solution import *
from .moma_solution import *

LOGGER = logging.getLogger(__name__)


Session = sessionmaker()


def initialize_connection(url, **kwargs):
    LOGGER.debug("Connecting to database '%s'.", url)
    engine = create_engine(url, **kwargs)
    Base.metadata.create_all(engine, checkfirst=True)
    return Session(bind=engine)