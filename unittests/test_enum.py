from unittest import TestCase

from eenum import ExtendedEnum

# =============================================================================

class ColourEnum(ExtendedEnum):
    red = 'r'
    blue = 'b'
    green = 'g'


class TestEnum(TestCase):
    def test_enum(self):
        # test choices()
        choices = ColourEnum.choices()
        self.assertEqual(len(choices), 3)
        self.assertIn(('r', 'red'), choices)
        self.assertIn(('b', 'blue'), choices)
        self.assertIn(('g', 'green'), choices)

        # test count()
        self.assertEqual(3, ColourEnum.count())

        # test values()
        values = ColourEnum.values()
        self.assertEqual(len(values), 3)
        self.assertIn('r', values)
        self.assertIn('b', values)
        self.assertIn('g', values)

        # test names()
        names = ColourEnum.names()
        self.assertEqual(len(names), 3)
        self.assertIn('red', names)
        self.assertIn('blue', names)
        self.assertIn('green', names)

        # test items()
        items = list(ColourEnum.items())
        self.assertEqual(len(items), 3)
        self.assertIn(('red', 'r'), items)
        self.assertIn(('blue', 'b'), items)
        self.assertIn(('green', 'g'), items)
