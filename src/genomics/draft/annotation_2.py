import os.path

from pybedtools import BedTool  # type: ignore[import-untyped]


def sort_bed(bed: str):
    """
    Takes a bed file either as a string or filepath,
    sorts entries by chr and start bp.
    """
    return BedTool(bed, from_string=not os.path.exists(bed)).sort()
