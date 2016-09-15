# -*- coding: utf-8 -*-
import os

import pysrt

from django.conf import settings


def parse_subs(filename):
	""" Opens a SRT file. """
	full_path = os.path.join(settings.MEDIA_ROOT, filename)
	subs = pysrt.open(full_path)
	return subs
