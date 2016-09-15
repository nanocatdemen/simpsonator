# -*- coding: utf-8 -*-
from django.test import TestCase
from subtitles.utils import parse_subs


class ParseSubsTest(TestCase):

	def setUp(self):
		""" Open a .SRT file from the media folder and reads it. """
		filename = "tests/test_0.srt"
		self.subs_obj = parse_subs(filename)

	def test_parse_simple_subs(self):
		self.assertIsNotNone(self.subs_obj)

	def test_correct_length(self):
		self.assertEqual(len(self.subs_obj), 635)

	def test_check_random_sub_text(self):
		sub = self.subs_obj[579]
		self.assertEqual(sub.text, "I can't keep pretending\nlike this is gonna go away.")

	def test_check_random_sub_start(self):
		sub = self.subs_obj[579]

		self.assertEqual(sub.start.hours, 0)
		self.assertEqual(sub.start.seconds, 59)
		self.assertEqual(sub.start.minutes, 35)

	def test_check_random_sub_end(self):
		sub = self.subs_obj[579]

		self.assertEqual(sub.end.hours, 0)
		self.assertEqual(sub.end.minutes, 36)
		self.assertEqual(sub.end.seconds, 3)
