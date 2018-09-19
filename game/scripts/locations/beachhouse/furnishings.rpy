init python:
    class Furnishing(renpy.Displayable):
        def __init__(self, image, position, callback=None, callback_args = [], **properties):
            super(Furnishing, self).__init__(**properties)
            self._image = renpy.displayable(image)
            self._hover_matrix = im.matrix.saturation(0.98)*im.matrix.contrast(1.07)*im.matrix.brightness(0.07)
            self._position = position
            self._callback = callback
            self._callback_args = callback_args
            self._width, self._height = get_size(image, True)
            self._matrix_to_use = im.matrix.identity()
        
        def render(self, width, height, st, at):
            render = renpy.render(im.MatrixColor(self._image, self._matrix_to_use), width, height, st, at)
            renpy.redraw(self, 0)
            return render
        
        def hitbox(self, x, y):
            xp, yp = self._position
            return (xp <= x <= xp+self_.width) and (yp <= y <= yp+self._height)
        
        def event(self, ev, x, y, st):
            if self.hitbox(x,y):
                self._matrix_to_use = self._hover_matrix
                if ev.type == pygame.MOUSEBUTTONUP:
                    if callable(self._callback):
                        self._callback(*self._callback_args)
                    elif self._callback in renpy.get_all_labels():
                        renpy.call(self._callback)
            else:
                self._matrix_to_use = im.matrix.identity()
            pass

label INIT_FURNISHINGS:
    python hide:
        file_ = renpy.file("scripts/data/furnishings.json")
        store.furnishings = json.load(file_)
        file_.close()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
