import unittest
from warbyparker import problem_one_main, recursive_search, TreeNode, problem_five_main, SavingsAccount
from christine import unique_words

class SolutionsTests(unittest.TestCase):

    def test_unique_words(self):
        unique_words(1,10,"/Users/victorzhu/Downloads/article.txt")

    def test_problem_one_main(self):
        self.assertEqual(problem_one_main([1,4,6,8,9,10], 10), 5)#end of array
        self.assertEqual(problem_one_main([1,4,6,8,9,10], 1), 0)#beginning of array
        self.assertEqual(problem_one_main([1,4,6,8,9,10], 100), False)#even array
        self.assertEqual(problem_one_main([1,4,6,8,9], 100), False)#odd array
        self.assertEqual(problem_one_main([1,4,6,8,9], 6), 2)#odd array

        self.assertEqual(problem_one_main([], 10), False)#empty array
        print("Problem One Passed")

    def test_problem_three_main(self):
        with self.assertRaises(ValueError):
            account = SavingsAccount(299)

        check = SavingsAccount(300)
        print("Problem Three Passed")

    def test_problem_four_main(self):
        root1 = TreeNode(1)
        root1.left = TreeNode(4)
        root1.left.left = TreeNode(8)
        root1.left.right = TreeNode(9)

        root1.right = TreeNode(5)
        root1.right.right = TreeNode(3)

        root2 = TreeNode(1)
        root2.left = TreeNode(4)
        root2.left.left = TreeNode(8)
        root2.left.right = TreeNode(9)

        root2.right = TreeNode(5)
        root2.right.right = TreeNode(2)

        root3 = None
        root4 = TreeNode(1)
        root5 = TreeNode(3)

        self.assertEqual(recursive_search(root1, 3), True)#Where value (aka 3) exists
        self.assertEqual(recursive_search(root2, 3), False)#Where value (aka 3) does not exist
        self.assertEqual(recursive_search(root3, 3), False)#Empty Tree
        self.assertEqual(recursive_search(root4, 3), False)#Single node
        self.assertEqual(recursive_search(root5, 3), True)#Single node

        print("Problem Four Passed")

    def test_problem_five_main(self):
        self.assertEqual(round(problem_five_main(700, 100, .1, 1), 2), 870.00)
        self.assertEqual(round(problem_five_main(870, 100, .1, 1), 2), 1057.00)

        self.assertEqual(round(problem_five_main(700, 100, .1, 8), 2), 2644.10)


        print("Problem Five Passed")


if __name__ == '__main__':
    unittest.main()
