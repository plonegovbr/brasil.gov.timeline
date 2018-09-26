# -*- coding: utf-8 -*-
from brasil.gov.timeline import _
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema
from zope.interface import Interface


class IBrowserLayer(Interface):
    """Add-on specific layer."""


class ITimeline(model.Schema):
    """A timeline."""

    title = schema.TextLine(
        title=_(u'label_title', default=u'Title'),
        description=_(
            u'help_title', default=u'The title of timeline.'),
        default=u'',
        required=True,
    )

    description = schema.Text(
        title=_(u'label_description', default=u'Description'),
        description=_(
            u'help_description',
            default=u'A brief text describing of timeline.'),
        default=u'',
        required=False,
    )

    more_information = schema.TextLine(
        title=_(u'label_more_information', default=u'More Informartion'),
        description=_(
            u'help_more_information', default=u'The field for more information.'),
        default=u'',
        required=False,
    )

    image_timeline = NamedBlobImage(
        title=_(u'label_image_timeline', default=u'Image Timeline'),
        description=_(
            u'help_image_timeline',
            default=u'A photo of Timeline.'),
        required=True,
    )

    year = schema.TextLine(
        title=_(u'label_year', default=u'Year'),
        description=_(
            u'help_year', default=u'The year of timeline.'),
        default=u'',
        required=False,
    )

    month = schema.TextLine(
        title=_(u'label_month', default=u'Month'),
        description=_(
            u'help_month', default=u'The month of timeline.'),
        default=u'',
        required=False,
    )
