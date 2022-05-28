import unittest
from src.structures.hashmap import HashMap
import random


class TestLinkedList(unittest.TestCase):

    def setUp(self) -> None:
        self.ll: HashMap.LinkedList = HashMap.LinkedList()

    def test___init__(self):
        self.assertTrue(self.ll.head is None)
        self.assertTrue(self.ll.tail is None)

    def test__len__(self):
        self.assertEqual(len(self.ll), 0)
        n = random.randint(1, 1000)
        for i in range(n):
            self.ll.insert_to_end(key=random.randint(1, 1000000), value=random.randint(1, 1000000))
        self.assertEqual(len(self.ll), n)

    def test_insert_to_end(self):
        self.ll.insert_to_end(1, 2)
        self.assertTrue(self.ll.tail.key == 1)
        self.assertTrue(self.ll.tail.value == 2)
        self.assertTrue(self.ll.head.key == 1)
        self.assertTrue(self.ll.head.value == 2)
        self.ll.insert_to_end(2, 2)

    def test_contains(self):
        self.ll.insert_to_end('12', 12)
        self.ll.insert_to_end('13', 13)
        self.ll.insert_to_end('14', 14)
        self.assertTrue('12' in self.ll)
        self.assertTrue('13' in self.ll)
        self.assertFalse('13' in self.ll)
        self.assertTrue('14' in self.ll)


class TestHashMap(unittest.TestCase):
    def setUp(self) -> None:
        self.hm = HashMap()
        for i in range(100):
            self.hm[str(i)] = random.randint(1, 1000)
        self.empty_hm = HashMap()

    def test___contains__(self):
        self.assertTrue('10' in self.hm)
        self.assertFalse('123' in self.hm)

    def test_