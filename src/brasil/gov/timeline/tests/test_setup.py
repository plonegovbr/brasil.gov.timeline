# -*- coding: utf-8 -*-
from brasil.gov.timeline.config import PROJECTNAME
from brasil.gov.timeline.interfaces import IBrowserLayer
from brasil.gov.timeline.testing import INTEGRATION_TESTING
from plone.browserlayer.utils import registered_layers

import unittest


class InstallTestCase(unittest.TestCase):
    """Ensure product is properly installed."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    def test_browser_layer_installed(self):
        self.assertIn(IBrowserLayer, registered_layers())

    def test_setup_permission(self):
        permission = 'brasil.gov.timeline: Add Timeline'
        roles = self.portal.rolesOfPermission(permission)
        roles = [r['name'] for r in roles if r['selected']]
        expected = [
            'Contributor',
            'Manager',
            'Owner',
            'Site Administrator',
        ]
        self.assertItemsEqual(roles, expected)
