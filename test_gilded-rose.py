# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(unittest.TestCase):
    item = Item()
    def test_foo(self):
        items = [self.item.create("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_normal_item(self):
        items = [self.item.create("Iron sword", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(9, items[0].quality)
        # Testing 1 more day
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(7, items[0].quality)
        # Testing one more day, changing the quality to prove that it cannot be negative.
        items[0].quality = 0
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)



    def test_conjured(self):
        items = [self.item.create("Conjured bread", 1, 8)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(6, items[0].quality)
        # Testing 1 more day
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(4, items[0].quality)
        # Testing 1 more day again
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
        # Testing last day 
        gilded_rose.update_quality()
        self.assertEqual(-3, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie(self):
        items = [self.item.create("Aged Brie", 1, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
        # Testing 1 day more
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras(self):
        items = [self.item.create("Sulfuras, Hand of Ragnaros", 1, 23)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(23, items[0].quality)

    def test_concert(self):
        items = [self.item.create("Backstage passes to a TAFKAL80ETC concert", 11, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(1, items[0].quality)
        # Testing 1 day more
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(3, items[0].quality)
        # Testing 1 day more changing sell_in
        items[0].sell_in = 5
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)
        # Testing 1 day more changing sell_in
        items[0].sell_in = 0
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
        # Testing 1 day more changing quality and sell in to prove 50 max in quality
        items[0].sell_in = 5
        items[0].quality = 49
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

        
if __name__ == '__main__':
    unittest.main()