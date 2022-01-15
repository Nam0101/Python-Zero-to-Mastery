import unittest
import script


class Testscript(unittest.TestCase):
    def setUp(self):
        print("Testing script:")
    def test_do_stuff(self):
        '''Hiiii!'''
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'assaad'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEqual(result, 0)

    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEqual(result, 0)
    def tearDown(self) -> None:
        print('Clear')
        return super().tearDown()

if __name__ == '__main__':
    unittest.main()
