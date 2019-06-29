import unittest

def parse_int(s):
    return int(s)

class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'not_number')

    def test_bad_int_with_value(self):
        self.assertRaisesRegex(ValueError, ".* 'not_number'", parse_int, 'not_number')

    # assertEqual을 써서 예외를 테스트하려면 coner case 처리가 필요해서 이렇게 구질구질해진다
    def test_bad_by_assertEqual(self):   
            try:        
                r = parse_int('a')        
            except ValueError as e:            
                self.assertEqual(type(e), ValueError)
            else:
                self.fail('ValueError not raised')
    
    # context manager로도 사용할 수 있다!
    def test_bad_by_multiple_step(self):
        with self.assertRaisesRegex(ValueError, 'invalid literal .*'):   
            r = parse_int('N/A')

        with self.assertRaises(ValueError):
            r = parse_int('N/A')



if __name__ == '__main__':
    unittest.main()
