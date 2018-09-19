init python:
    class PinkItem:
        def __init__(self, item, name = "", image = "", popup = "", idle = "", hover = "", price = 0, category = "", purchased = False):
            self.name = name
            self.image = image
            self.popup = popup
            self.idle = idle
            self.hover = hover
            self.price = price
            self.category = category
            self.item = item
            self.purchased = purchased


    class PinkStore (object) :
        def __init__(self):
            self.items = []

    class ComicItem:
        def __init__(self, item, name = "", image = "", popup = "", idle = "", hover = "", price = 0, category = "", purchased = False):
            self.name = name
            self.image = image
            self.popup = popup
            self.idle = idle
            self.hover = hover
            self.price = price
            self.category = category
            self.item = item
            self.purchased = purchased


    class ComicStore (object) :
        def __init__(self):
            self.items = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
