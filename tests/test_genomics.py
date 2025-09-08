from genomics.annotation import sort_bed


def test_sort_bed():
    bed = """chr1	1	100	feature1	0	+
chr1	100	200	feature2	0	+
chr1	900	950	feature4	0	+
chr1	150	500	feature3	0	-
"""
    bed_sorted = """chr1	1	100	feature1	0	+
chr1	100	200	feature2	0	+
chr1	150	500	feature3	0	-
chr1	900	950	feature4	0	+
"""
    assert str(sort_bed(bed)) == bed_sorted
