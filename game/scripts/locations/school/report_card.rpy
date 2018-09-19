init python:
    def reportcard_name(st, at):
        if store.firstname == "":
            return Text("Anon"), None
        else: 
            return Text(store.firstname, size = 48, xanchor = 0.5, yanchor = 1.0)

    class ReportCard(renpy.Displayable):
        def __init__(self, **properties):
            super(ReportCard, self).__init__(**properties)
            self._bg = renpy.displayable("objects/closeup_reportcard.png")
            self._grades_pos = {"french":(491, 217),
                                "music":(497, 308),
                                "art":(501,402),
                                "science":(504,498),
                                "gym":(505,589)}
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            if store.firstname == "":
                name = Text("Anon"), None
            else: 
                name = Text(store.firstname, size = 48, xanchor = 0.5, yanchor = 1.0)
            name_r = renpy.render(name, width, height, st, at)
            render.blit(name_r, (256, 68))
            for key, value in player.grades.items():
                grade_pos = self._grades_pos[key]
                grade_d = renpy.displayable("buttons/report_card_0{}.png".format(value))
                grade_r = renpy.render(grade_d, width, height, st, at)
                render.blit(grade_r, grade_pos)
            return render
        def event(self, ev, x, y, st):
            pass

    class LockerList(renpy.Displayable):
        def __init__(self, **properties):
            super(LockerList, self).__init__(**properties)
            self._bg = renpy.displayable("backgrounds/location_school_locker_list.jpg")
            self.mark = renpy.displayable("buttons/locker_list_02.png")
            self.mark_max = renpy.displayable("buttons/locker_list_01.png")
            self.coords_init = {"mia":(453, 247, 750, 210),
                                "judith":(453, 308, 752, 278),
                                "roxxy":(455, 369, 760, 338),
                                "eve": (456, 428, 762, 398),
                                "annie": (455, 491, 767, 459),
                                "ronda": (462, 557, 768, 524),
                                "june":(459, 620, 766, 587),
                                "kevin":(459, 684, 773, 653),
                                }
        
        def render(self, width, height, st, at):
            render = renpy.render(self._bg, width, height, st, at)
            dot_r = renpy.render(self.mark, width, height, st, at)
            check_r = renpy.render(self.mark_max, width, height, st, at)
            for machine in [m for name, m in store.machines.items() if name in self.coords_init.keys()]:
                x, y, fx, fy = self.coords_init[machine._name]
                for i in range(int(machine.progress*9./100.)):
                    if i == 8:
                        render.blit(check_r, (fx, fy))
                    else:
                        render.blit(dot_r, (x+35*i, y))
            return render
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
