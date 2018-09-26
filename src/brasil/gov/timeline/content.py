# -*- coding: utf-8 -*-
from brasil.gov.timeline.interfaces import ITimeline
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(ITimeline)
class Timeline(Container):
    """A Timeline."""
