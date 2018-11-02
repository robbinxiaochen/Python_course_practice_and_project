# -*- coding: utf-8 -*-
from __future__ import absolute_import

from uuid import uuid4

from sqlalchemy import Column, Unicode

__all__ = ("UUIDMixin",)


class UUIDMixin(object):

    uuid = Column(Unicode(36), nullable=False, unique=True, index=True)

    def __init__(self, **kwargs):
        super(UUIDMixin, self).__init__(**kwargs)
        if self.uuid is None:
            self.uuid = str(uuid4())
