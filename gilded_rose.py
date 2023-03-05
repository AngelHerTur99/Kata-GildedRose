# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # This method calls the update quality method for each item.
        for item in self.items: item.update_quality()
        