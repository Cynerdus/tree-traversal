import unittest
from tree import Tree

class TestTreeFind(unittest.TestCase):
    def setUp(self):
        self.tree = Tree()
        self.tree.add(10)
        self.tree.add(5)
        self.tree.add(15)
        self.tree.add(3)
        self.tree.add(7)
        self.tree.add(12)
        self.tree.add(17)

    def test_find_existing_node(self):
        found_node = self.tree._find(7, self.tree.root)
        self.assertIsNotNone(found_node)
        self.assertEqual(found_node.data, 7)

    def test_find_nonexistent_node(self):
        found_node = self.tree._find(20, self.tree.root)
        self.assertIsNone(found_node)