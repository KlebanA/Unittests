import unittest
import flietest2


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(
            flietest2.full_name('Клебан', 'Анастасия', 'Евгеньевна'),
            'Клебан Анастасия Евгеньевна'
        )

    def test_big(self):
        self.assertEqual(
            flietest2.full_name('КЛЕБАН', 'АНАСТАСИЯ', 'ЕВГЕНЬЕВНА'),
            'Клебан Анастасия Евгеньевна'
        )

    def test_small(self):
        self.assertEqual(
            flietest2.full_name('клЕБАН', 'АнАСТАСИЯ', 'ЕвГЕнЬЕВНА'),
            'Клебан Анастасия Евгеньевна'
        )


if __name__ == '__main__':
    unittest.main()
