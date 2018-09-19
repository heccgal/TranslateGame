screen basement:
    add game.timer.image("backgrounds/location_home_basement_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (0,308)
        idle game.timer.image("objects/object_stairs_03{}.png")
        hover HoverImage(game.timer.image("objects/object_stairs_03{}.png"))
        action Hide("basement"), Function(renpy.call, "home_lock_check", "Living Room", "home_livingroom_dialogue")

    if M_mom.get_state() == S_mom_close_valve:
        imagebutton:
            focus_mask True
            pos (394,512)
            idle game.timer.image("objects/object_pipe_01{}.png")
            hover HoverImage(game.timer.image("objects/object_pipe_01{}.png"))
            action Hide("basement"), Jump("broken_pipe")

    if player.location.is_here(M_mom):
        imagebutton:
            focus_mask True
            pos (486,320)
            idle "images/objects/character_debbie_06.png"
            hover HoverImage("images/objects/character_debbie_06.png")
            action Hide("basement"), If(
                                        M_mom.get_state() == S_mom_laundry_help and M_mom.is_set('chores'),
                                        Jump("laundry_dialogue"),
                                        Function(renpy.call, "home_lock_check", "Mom", "mom_button_dialogue"),
                                     )

screen basement_mom_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("basement_mom_sex_options"), Jump("basement_mom_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("basement_mom_sex_options"), Jump("basement_mom_sex_cum")

    if M_mom.get("sex speed") < .176:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("basement_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("basement_mom_sex_loop")

    if M_mom.get("sex speed") > .075:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("basement_mom_sex_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.05), Jump("basement_mom_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
