import unittest
from cards_war_solution import cards_war_solution
from format_phone_number_solution import format_phone_number_solution
from reversing_coins_solution import reversing_coins_solution
from count_seven import count_seven_solution
from multipleThreeAndFive import multipleThreeAndFive

import itertools
from solutions import pairs, is_four_of_kind, merge, dec_to_base_x
from itertools import combinations

class SolutionsTests(unittest.TestCase):
    
    def test_not_pairs(self):
        #Edge Cases
        self.assertEqual(pairs([]), [])#test for empty list
        self.assertEqual(pairs([1]), [])#test for only one number in list
        self.assertEqual(pairs([1, 8]), [(1, 8)])#test for when theres just two numbers
        self.assertEqual(pairs([1, 1, 1]), [(1, 1), (1, 1), (1, 1)])#test when all numbers are the same
        
        self.assertEqual(pairs([1, 8, 12, 5, 7]), [(1, 8), (1, 12), (1, 5), (1, 7), (8, 12), (8, 5), (8, 7), (12, 5), (12, 7), (5, 7)])
        self.assertEqual(pairs([1, 1]), [(1, 1)])
        self.assertEqual(pairs([4, 3, 22, 3, 27, 69]), [(4, 3), (4, 22), (4, 3), (4, 27), (4, 69), (3, 22), (3, 3), (3, 27), (3, 69), (22, 3), (22, 27), (22, 69), (3, 27), (3, 69), (27, 69)])
        self.assertEqual(pairs([1, 8, 12]), [(1, 8), (1, 12), (8, 12)])
        self.assertEqual(pairs([321, 251, 3, 2, 3, 2, 5, 99, 11, 12, 14, 2, 5]), [(321, 251), (321, 3), (321, 2), (321, 3), (321, 2), (321, 5), (321, 99), (321, 11), (321, 12), (321, 14), (321, 2), (321, 5), (251, 3), (251, 2), (251, 3), (251, 2), (251, 5), (251, 99), (251, 11), (251, 12), (251, 14), (251, 2), (251, 5), (3, 2), (3, 3), (3, 2), (3, 5), (3, 99), (3, 11), (3, 12), (3, 14), (3, 2), (3, 5), (2, 3), (2, 2), (2, 5), (2, 99), (2, 11), (2, 12), (2, 14), (2, 2), (2, 5), (3, 2), (3, 5), (3, 99), (3, 11), (3, 12), (3, 14), (3, 2), (3, 5), (2, 5), (2, 99), (2, 11), (2, 12), (2, 14), (2, 2), (2, 5), (5, 99), (5, 11), (5, 12), (5, 14), (5, 2), (5, 5), (99, 11), (99, 12), (99, 14), (99, 2), (99, 5), (11, 12), (11, 14), (11, 2), (11, 5), (12, 14), (12, 2), (12, 5), (14, 2), (14, 5), (2, 5)])
        #self.assertEqual(pairs([]), [])
        
        #Tests using itertools combinations, although this might not be appropriate, then simply ignore.
        #self.assertEqual(list(itertools.combinations([1, 8, 12, 5, 7], 2)), [(1, 8), (1, 12), (1, 5), (1, 7), (8, 12), (8, 5), (8, 7), (12, 5), (12, 7), (5, 7)])
        #list(itertools.combinations([69, 69, 69, 69, 69, 69, 69], 2))
        self.assertEqual(pairs([1, 8, 12, 5, 7]), list(itertools.combinations([1, 8, 12, 5, 7], 2)))
        self.assertEqual(pairs([4, 3, 22, 3, 27, 69]), list(itertools.combinations([4, 3, 22, 3, 27, 69], 2)))
        self.assertEqual(pairs([321, 321, 2, 4, 4, 3, 22, 3, 27, 69, 5, 2, 1, 1]), list(itertools.combinations([321, 321, 2, 4, 4, 3, 22, 3, 27, 69, 5, 2, 1, 1], 2)))
        self.assertEqual(pairs([1]), list(itertools.combinations([1], 2)))
        self.assertEqual(pairs([]), list(itertools.combinations([], 2)))
    
    def test_not_four_of_kind(self):
        #test for 4 of a kind, positioning the 5th card that is different as 1st, 2nd, 3rd, 4th, and 5th card in hand
        self.assertTrue(is_four_of_kind(["9","4","4","4","4"]))
        self.assertTrue(is_four_of_kind(["A","K","A","A","A"]))
        self.assertTrue(is_four_of_kind(["5","5","Q","5","5"]))
        self.assertTrue(is_four_of_kind(["1","1","1","J","1"]))
        self.assertTrue(is_four_of_kind(["2","2","2","2","K"]))
        
        #TEST CASE WHERE 5 ARE THE SAME
        self.assertTrue(is_four_of_kind(["1","1","1","1","1"]))
        
        #Test cases where there are not four of a kind
        self.assertFalse(is_four_of_kind(["5","5","Q","4","5"]))#three of a kind
        self.assertFalse(is_four_of_kind(["5","3","Q","4","5"]))#two of a kind
        self.assertFalse(is_four_of_kind(["K","J,""Q","10","9"]))#straight
        self.assertFalse(is_four_of_kind(["1","3","5","7","9"]))#none of a kind
        self.assertFalse(is_four_of_kind(["5","5","5","Q","Q"]))#house of 5s with queen pair
    
    def test_not_merge(self):
        #Edge cases
        self.assertEqual(merge([], []), [])#empty list
        self.assertEqual(merge([1, 1, 5], [2, 4, 6]), [1, 1, 2, 4, 5, 6])#duplicates
        self.assertEqual(merge([1, 1, 5, 6, 7, 11, 11, 14, 19, 20, 22], [2, 4, 6, 9, 20]), [1,1,2,4,5,6,6,7,9,11,11,14,19,20,20,22])#duplicates and different sized lists
        self.assertEqual(merge([1, 1, 5], [1, 4, 5, 6]), [1, 1, 1, 4, 5, 5, 6])#even and odd length list
        self.assertEqual(merge([1, 1, 5], [10, 11, 12]), [1,1,5,10,11,12])#one list lowest number is greater than all numbers in other list
        
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(merge([3, 7, 12, 14], [2, 6, 9, 11]), [2,3,6,7,9,11,12,14])
    
    def test_not_dec_to_base_x(self):
        #check edge case of converting 0 from base 10 to other bases
        #assume that base is always 2-9
        self.assertEqual(dec_to_base_x(9, 1), "1")
        self.assertEqual(dec_to_base_x(9, 0), "0")
        self.assertEqual(dec_to_base_x(2, 0), "0")
        self.assertEqual(dec_to_base_x(1, 1), None)#if base less than 2 returns None
        self.assertEqual(dec_to_base_x(20, 1), None)#if base greater than 9 returns None
        self.assertEqual(dec_to_base_x(10, 12345123), "12345123")#if base is 10 return num back
        
        self.assertEqual(dec_to_base_x(8, 140), "214")
        
        self.assertEqual(dec_to_base_x(8, 16), "20")
        self.assertEqual(dec_to_base_x(8, 0), "0")
        self.assertEqual(dec_to_base_x(8, 8), "10")
        self.assertEqual(dec_to_base_x(8, 80), "120")
        
        self.assertEqual(dec_to_base_x(2, 5), "101")
        self.assertEqual(dec_to_base_x(5, 101111000101111100100011), "413240421021020223101013111200021")
        self.assertEqual(dec_to_base_x(8, 413240421021020223101013111200), "515640166736766404717526036130640")
        self.assertEqual(dec_to_base_x(2, 12345123), "101111000101111100100011")
        self.assertEqual(dec_to_base_x(3, 12345123), "212020012022210")
        self.assertEqual(dec_to_base_x(4, 12345123), "233011330203")
        self.assertEqual(dec_to_base_x(5, 12345123), "11130020443")
        self.assertEqual(dec_to_base_x(6, 12345123), "1120333203")
        self.assertEqual(dec_to_base_x(7, 12345123), "206634420")
        self.assertEqual(dec_to_base_x(8, 12345123), "57057443")
        self.assertEqual(dec_to_base_x(9, 12345123), "25205283")
    
    
    
    
    

    def test_cards_war_solution(self):
        self.assertEqual(cards_war_solution("23A84Q", "K2Q25J"), 4)
        self.assertEqual(cards_war_solution("A586QK", "JJ653K"), 4)

    def test_format_phone_number_solution(self):
        self.assertEqual(format_phone_number_solution("00-44 48 5555 8361"), "004-448-555-583-61")
        self.assertEqual(format_phone_number_solution("0 - 22 1985--324"), "022-198-53-24")
        self.assertEqual(format_phone_number_solution("555372654"), "555-372-654")
        self.assertEqual(format_phone_number_solution("22"), "22")
        self.assertEqual(format_phone_number_solution("2222"), "22-22")
        #self.assertEqual(format_phone_number_solution(), )

    def test_reversing_coins_solution(self):
        self.assertEqual(reversing_coins_solution([1, 0, 0, 1, 0, 0]), 2)
        self.assertEqual(reversing_coins_solution([1, 0, 0, 1, 0, 0, 1, 1, 1]), 4)
        self.assertEqual(reversing_coins_solution([1, 0, 0, 1, 0, 0, 0, 1, 0]), 3)
        self.assertEqual(reversing_coins_solution([1, 0, 1, 1, 1, 1]), 1)
        self.assertEqual(reversing_coins_solution([1, 1, 1, 1, 1, 1]), 0)

    def test_count_seven_solution(self):
        self.assertEqual(count_seven_solution(746728), 2)
        self.assertEqual(count_seven_solution(7732174434127), 4)

    def test_multipleThreeAndFive(self):
        self.assertEqual(multipleThreeAndFive(), 233168)


if __name__ == '__main__':
    unittest.main()
