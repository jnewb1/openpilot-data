#!/usr/bin/env python

# Syncs the status of the repository (adds new routes and add segments to segments.json)
from openpilot.data import SEGMENTS_DIR, save_segments_data
from openpilot.data.segments import get_all_segments, get_valid_segments
from openpilot.data.utils import add_segment_from_logreader
from openpilot.tools.lib.logreader import logreader_from_route_or_segment


if __name__ == "__main__":
  all_segments = {s for segments in get_all_segments().values() for s in segments}
  valid_segments = {s for segments in get_valid_segments().values() for s in segments}

  invalid_segments = all_segments - valid_segments # segments which aren't yet in the repository

  for segment in invalid_segments:
    try:
      add_segment_from_logreader((SEGMENTS_DIR / segment).with_suffix(".bz2"), logreader_from_route_or_segment(segment))
    except Exception as e:
      print(f"Failed to add segment {segment}: {e}")

  save_segments_data({"segments_per_platform": get_valid_segments()})
