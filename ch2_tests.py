import unittest
import ch2


class MyFirstTests(unittest.TestCase):
    def test_name(self):
        result = ch2.name('Jocelyn')
        self.assertEqual(result, 'So nice to meet you, Jocelyn')


if __name__ == '__main__':
    unittest.main()
