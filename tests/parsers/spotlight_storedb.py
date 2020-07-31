#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for the Apple Spotlight store database parser."""

from __future__ import unicode_literals

import unittest

from plaso.lib import definitions
from plaso.parsers import spotlight_storedb

from tests.parsers import test_lib


class SpotlightStoreDatabaseParserTest(test_lib.ParserTestCase):
  """Tests for the Apple Spotlight store database parser."""

  def testParse(self):
    """Tests the Parse function."""
    parser = spotlight_storedb.SpotlightStoreDatabaseParser()
    storage_writer = self._ParseFile(['store.db'], parser)

    self.assertEqual(storage_writer.number_of_warnings, 0)
    self.assertEqual(storage_writer.number_of_events, 1159238)

    events = list(storage_writer.GetEvents())

    expected_event_values = {
        'file_name': 'CIJCanoScan9000F.icns',
        'file_system_identifier': 41322,
        'kind': 'Apple icon image',
        'parent_file_system_identifier': 41320,
        'timestamp': '2013-06-04 20:53:10.000000',
        'timestamp_desc': definitions.TIME_DESCRIPTION_MODIFICATION}

    self.CheckEventValues(storage_writer, events[12], expected_event_values)

    expected_message = 'CIJCanoScan9000F.icns com.apple.icns'
    expected_short_message = 'CIJCanoScan9000F.icns'

    event_data = self._GetEventDataOfEvent(storage_writer, events[12])
    self._TestGetMessageStrings(
        event_data, expected_message, expected_short_message)


if __name__ == '__main__':
  unittest.main()
