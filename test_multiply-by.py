import unittest
import pandas as pd
from pandas.testing import assert_frame_equal

render = __import__("multiply-by").render

DefaultParams = {
    'columns': [],
    'constant': 1,
}


def P(**kwargs):
    """Build a params dict."""
    return {
        **DefaultParams,
        **kwargs
    }

class TestMultiplyBy(unittest.TestCase):
    def test_initial_nop(self):
        # should NOP when first applied; no column selected
        result = render(pd.DataFrame({'A': [1, 2]}), P())
        assert_frame_equal(result, pd.DataFrame({'A': [1, 2]}))
        
    def test_single_column(self):
        result = render(pd.DataFrame({'A': [1, 2], 'B': [3, 6]}), P(columns=['A'], constant=3))
        assert_frame_equal(result, pd.DataFrame({'A': [3, 6], 'B': [3, 6]}))
        
    def test_multiple_columns(self):
        result = render(pd.DataFrame({'A': [1, 2], 'B': [3, 6], 'C': [2, 5]}), P(columns=['A', 'C'], constant=3))
        assert_frame_equal(result, pd.DataFrame({'A': [3, 6], 'B': [3, 6], 'C': [6, 15]}))
        
    def test_negative(self):
        result, warning = render(pd.DataFrame({'A': [1, 2], 'B': [3, 6]}), P(columns=['A'], constant=-3))
        assert_frame_equal(result, pd.DataFrame({'A': [-3, -6], 'B': [3, 6]}))
        self.assertTrue(warning)


if __name__ == '__main__':
    unittest.main()
