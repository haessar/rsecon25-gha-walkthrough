import os.path

from pybedtools import BedTool  # type: ignore[import-untyped]


def sort_bed(bed: str):
    return BedTool(bed, from_string=not os.path.exists(bed)).sort()
