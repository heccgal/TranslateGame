init python:
    class Weightlifting(renpy.Displayable):
        def __init__(self, **kwargs):
            super(Weightlifting, self).__init__(**kwargs)
            
            
            self._background_string = ""
            if renpy.variant("mobile"):
                self._background_string = "_mobile"
            if player.stats.str() >= 7:
                self._background_string += "_heavy"
            elif player.stats.str() >= 3:
                self._background_string += "_medium"
            self.backgrounds = [renpy.displayable("backgrounds/location_gym_minigame04a{}.jpg".format(self._background_string)),
                                renpy.displayable("backgrounds/location_gym_minigame04b{}.jpg".format(self._background_string))
                               ] 
            
            
            self._meter = renpy.displayable("buttons/meter_03.png")
            self._arrows = renpy.displayable("buttons/arrows.png")
            self._filler = renpy.displayable("buttons/meter_04.png")
            
            self._counter = 0 
            self.time_y_value = 586 
            self.y_value = 610 
            self.win = False 
            self.started = False 
            
            self._TIMER = 8 
            self._TIMER_BAR_LENGTH = 586
            self._BAR_X_POS, self._BAR_Y_POS = 42, 54 
            self._BAR_WIDTH = 160 
            self._ARROW_X_OFFSET = 74 
            self._TIMER_DECREMENT = 0.01
            
            self._start_timer = 0
            self._timer = self._TIMER 
        
        def render(self, width, height, st, at):
            if self.started:
                if int((self._TIMER-self._timer)/self._TIMER_DECREMENT) <= int((clock()-self._start_timer)/self._TIMER_DECREMENT):
                    self.timer()
            render = renpy.render(self.backgrounds[(self._counter/12)%2], width, height, st, at)
            self._width, self._height = render.get_size()
            meter_r = renpy.render(self._meter, width, height, st, at)
            arrows_r = renpy.render(self._arrows, width, height, st, at)
            filler_r = renpy.render(self._filler, width, height, st, at)
            render.blit(meter_r, (self._BAR_X_POS, self._BAR_Y_POS))
            filler_w, filler_h = filler_r.get_size()
            filler_r_crop = filler_r.subsurface((-self._BAR_X_POS, -self._BAR_Y_POS, self._BAR_WIDTH, self.y_value))
            render.blit(filler_r_crop, (0, 0))
            render.blit(arrows_r, (self._ARROW_X_OFFSET, self.time_y_value))
            renpy.redraw(self, 0)
            return render
        
        def timer(self):
            self._timer = max(self._timer - self._TIMER_DECREMENT, 0)
            if self.y_value < 600:
                self.y_value += 4 
            self.time_y_value -= self._TIMER_BAR_LENGTH / (self._TIMER / self._TIMER_DECREMENT) 
            
            if self.win:
                renpy.jump("weightlifting_done")
            elif self.time_y_value < 144:
                renpy.jump("weightlifting_fail")
            if self.y_value < 45:
                self.win = True
        
        def on_event(self):
            if not self.started:
                self.started = True
                self._start_timer = clock()
            self._counter += 1
            self.y_value -= 50
        
        def event(self, ev, x, y, st):
            if renpy.variant("mobile") and ev.type == pygame.MOUSEBUTTONUP:
                self.on_event()
                return
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                self.on_event()
                return
            return

screen weightlifting:
    add Weightlifting()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
