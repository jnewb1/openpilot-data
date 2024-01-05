import bz2

from sanetizer import sanetize
from openpilot.data import SEGMENTS_DIR
from openpilot.tools.lib.logreader import LogReader
from openpilot.tools.lib.route import Route


def add_segment_from_logreader(output_filepath, lr):
  stripped = list(sanetize(lr))

  assert len(stripped) > 0

  stripped_bytes = b"".join([m.as_builder().to_bytes() for m in stripped])
  compressed_bytes = bz2.compress(stripped_bytes)

  with open(output_filepath, "wb") as f:
    f.write(compressed_bytes)


def add_segment(route: Route, seg: int):
  # add an individual segment
  lr = LogReader(route.log_paths()[seg], sort_by_time=True)
  add_segment_from_logreader((SEGMENTS_DIR / f"{route.name}--{seg}").with_suffix(".bz2"), lr)
