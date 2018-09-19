screen trailer_bedroom:
    add game.timer.image("trailer_bedroom{}")

    imagebutton:
        focus_mask True
        pos (819,136)
        idle game.timer.image("objects/object_door_88{}.png")
        hover HoverImage(game.timer.image("objects/object_door_88{}.png"))
        action Hide("trailer_bedroom"), Function(renpy.call, "trailer_lock_check", "trailer_interior")

    if player.location.is_here(M_roxxy):
        imagebutton:
            focus_mask True
            pos (41,404)
            idle "objects/character_roxxy_03.png"
            hover HoverImage("objects/character_roxxy_03.png")
            action Hide("trailer_bedroom"), Jump("roxxy_trailer_button_dialogue")



screen roxxy_bed_sex_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("roxxy_bed_sex_options"), Jump("button_roxxy_trailer_bed_sex_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("roxxy_bed_sex_options"), Jump("button_roxxy_trailer_bed_sex_cum")

    if anim_toggle:
        if M_roxxy.get("sex speed") < .09:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("roxxy_bed_sex_options"), Function(M_roxxy.set, "sex speed", M_roxxy.get("sex speed") + 0.05), Jump("button_roxxy_trailer_bed_sex_loop")

        if M_roxxy.get("sex speed") > .031:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("roxxy_bed_sex_options"), Function(M_roxxy.set, "sex speed", M_roxxy.get("sex speed") - 0.05), Jump("button_roxxy_trailer_bed_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
