from collections import defaultdict
from openpilot.data import BASEDIR, SEGMENTS_DIR
from openpilot.selfdrive.car.tests.routes import routes
from openpilot.selfdrive.test.helpers import read_segment_list

ADDITIONAL_SEGMENTS = read_segment_list(BASEDIR / "additional_segments.txt")

def get_all_segments():
  segments = defaultdict(list)

  for route in routes:
    for segment in [route.segment] if route.segment is not None else [0,1,2]:
      segment_name = f"{route.route}--{segment}"
      segments[route.car_model].append(segment_name)

  for platform, segment in ADDITIONAL_SEGMENTS:
    segments[platform].append(segment)

  return segments

def segment_exists(segment_name):
  segment_file = (SEGMENTS_DIR / segment_name).with_suffix(".bz2")
  return segment_file.exists()

def get_valid_segments(): # segments that exist
  return {platform: [s for s in segments if segment_exists(s)] for platform, segments in get_all_segments().items()}
