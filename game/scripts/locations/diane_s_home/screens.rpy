screen dianes_front_yard:
    add game.timer.image("backgrounds/location_diane_front_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (289,382)
        idle game.timer.image("objects/object_door_106{}.png")
        hover HoverImage(game.timer.image("objects/object_door_106{}.png"))
        action Hide("dianes_front_yard"), If(
                                             game.timer.is_dark(),
                                             Jump(game.dialog_select("diane_front_yard_night_locked")),
                                             If(
                                                not aunt.known(aunt_mouse_attack),
                                                Jump("dianelobby_locked"),
                                                [Function(playSound), Jump(game.dialog_select("dianelobby_dialogue"))]
                                             )
        )

    imagebutton:
        focus_mask True
        pos (563,482)
        idle game.timer.image("objects/object_door_107{}.png")
        hover HoverImage(game.timer.image("objects/object_door_107{}.png"))
        action Hide("dianes_front_yard"), Jump("garden_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
