# -*- coding: utf-8 -*-
import os

import pysrt
import numpy as np
import cv2

from django.conf import settings


def parse_subs(filename):
	""" Opens a SRT file. """
	# TODO remove weird characters like '\n' and HTML tags
	full_path = os.path.join(settings.MEDIA_ROOT, filename)
	subs = pysrt.open(full_path)
	return subs


def find_frames(video_filename, frame_ranges):
	""" Given a video an a list of frame ranges, finds the frames and shows them. """
	full_path = os.path.join(settings.MEDIA_ROOT, video_filename)
	cap = cv2.VideoCapture(full_path)

	fps = cap.get(cv2.CAP_PROP_FPS)

	frame_number = 0
	while cap.isOpened():
		ret, frame = cap.read()

		if any(frame_number in range(fr[0], fr[1]) for fr in frame_ranges):
			cv2.imshow('frame', frame)
			if cv2.waitKey(10) & 0xFF == ord('q'):
				break
		frame_number += 1

	cap.release()
	cv2.destroyAllWindows()
