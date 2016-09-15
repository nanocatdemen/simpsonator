# -*- coding: utf-8 -*-
from django.test import TestCase
from subtitles.utils import parse_subs, find_frames


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


class PlayVideoTest(TestCase):

	def setUp(self):
		""" Opens the substitles file and the video. """
		self.video_filename = "tests/test_0.mkv"
		self.subs_filename = "tests/test_0.srt"
		self.subs_obj = parse_subs(self.subs_filename)

	def test_find_obama_frames(self):
		obama_mentioned_in_frames = []
		for sub in self.subs_obj:
			if "Obama" in sub.text:
				start_in_second = sub.start.hours * 3600 + sub.start.minutes * 60 + sub.start.seconds
				end_in_seconds = sub.end.hours * 3600 + sub.end.minutes * 60 + sub.end.seconds
				start_frame = 24 * start_in_second
				end_frame = 24 * end_in_seconds
				obama_mentioned_in_frames.append((start_frame, end_frame))
		# [(3456, 3504), (4200, 4248), (4464, 4536)]
		find_frames(self.video_filename, obama_mentioned_in_frames)