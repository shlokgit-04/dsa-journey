from longest_common_prefix import longest_common_prefix


def test_examples():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""


def test_single_and_prefix():
    assert longest_common_prefix(["interspecies"]) == "interspecies"
    assert longest_common_prefix(["ab", "a"]) == "a"
