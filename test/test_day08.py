from hypothesis import strategies as st, given
from src.aoc22.day08.part_a_helpers import get_viewing_distance

@given(st.lists(st.integers(min_value=0, max_value=9), min_size=1))
def test_get_viewing_distance(data):
    expected_distance = next((i + 1 for i, h in enumerate(data) if h >= data[0]), len(data))
    assert get_viewing_distance(data[0], data) == expected_distance