# -*- coding: utf-8 -*-

class Item(object):
    def create(self, name, sell_in, quality):
        # Creates the item depending on its name.
        if name == "Sulfuras, Hand of Ragnaros": return SulfurasUpdater(name, sell_in, quality)
        if name == "Aged Brie": return AgedBrieUpdater(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert": return ConcertUpdater(name, sell_in, quality)
        if "conjured" in name.lower(): 
            return ConjuredUdater(name, sell_in, quality)
        else: 
            return NormalItem(name, sell_in, quality)

    
class NormalItem(object):
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.quality = quality
        self.sell_in = sell_in

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        # When the quality is greater than 0, it decreases by 2 or 1, depending on whether the sell-in value is less than or equal to 0
        self.quality -= 2 if self.sell_in <= 0 else 1
        self.quality = 0 if self.quality < 0 else self.quality
        self.sell_in -= 1

class AgedBrieUpdater(NormalItem):
    def update_quality(self):
        # While the quality is less than 50, it will add 1, otherwise, it won't add anything.
        self.quality += 1 if self.quality < 50 else 0
        self.sell_in -= 1


class ConcertUpdater(NormalItem):
    def update_quality(self):
        # The quality will increase or decrease depending on the value of the sell-in.
        if 10 >= self.sell_in > 5:
            self.quality += 2 
        elif 5 >= self.sell_in > 0:
            self.quality += 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality += 1
        # If the quality is greater than 50, it will return to 50, because the quality cannot be more than 50.
        self.quality = 50 if self.quality > 50 else self.quality
        self.sell_in -= 1

class SulfurasUpdater(NormalItem):
    def update_quality(self):
        # This item always passes because it is immutable.
        pass

class ConjuredUdater(NormalItem):
    def update_quality(self):
        # The quality will decrease by 2 whenever the quality is greater than 0, since the items can never go below that.
        self.quality -= 2 if self.quality > 0 else 0
        # if sell in days have passed and quality is greater than 0, decrease quality twice 
        self.quality -= 2 if self.sell_in < 0 and self.quality > 0 else 0
        self.sell_in -= 1