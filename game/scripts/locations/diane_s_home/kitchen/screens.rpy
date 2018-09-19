screen dianes_kitchen:
    add "backgrounds/location_diane_kitchen_empty_day.jpg"

    if aunt_drink_offered:
        imagebutton:
            focus_mask True
            pos (370,408)
            idle "objects/object_drinks_01.png"
            hover HoverImage("objects/object_drinks_01.png")
            action Hide("dianes_kitchen"), Jump(game.dialog_select("kitchen_drink"))

    if (not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)) and (not aunt.known(aunt_drunken_splur) or aunt.over(aunt_drunken_splur)):
        if aunt_count >= 8:
            imagebutton:
                focus_mask True
                pos (345,219)
                idle "objects/character_diane_02.png"
                hover HoverImage("objects/character_diane_02.png")
                action Hide("dianes_kitchen"), Jump(game.dialog_select("aunt_button_dialogue"))

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (0,260)
            idle "objects/object_door_66.png"
            hover HoverImage("objects/object_door_66.png")
            action If(
                not aunt.known(aunt_mouse_attack),
                [Hide("dianes_kitchen"), Jump("dianelobby_locked")],
                [Hide("dianes_kitchen"), Function(playSound), Jump("dianelobby_dialogue")]
            )

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_07.png"
        hover HoverImage("boxes/auto_option_07.png")
        action If(
            aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack),
            [Hide("dianes_kitchen"), Jump(game.dialog_select("mouse_attack"))],
            [Hide("dianes_kitchen"), SetVariable("in_garden", True), Jump(game.dialog_select("garden_dialogue"))]
        )

screen aunt_sex_options:
    imagebutton:
        pos (150,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("aunt_sex_options"), Jump(game.dialog_select("aunt_sex_loop"))

    imagebutton:
        pos (350,700)
        idle "buttons/diane_stage01_02.png"
        hover HoverImage("buttons/diane_stage01_02.png")
        action Hide("aunt_sex_options"), Jump(game.dialog_select("aunt_sex_cum_in"))

    imagebutton:
        pos (550,700)
        idle "buttons/diane_stage01_03.png"
        hover HoverImage("buttons/diane_stage01_03.png")
        action Hide("aunt_sex_options"), Jump(game.dialog_select("aunt_sex_cum_out"))

    if M_aunt.get("sex speed") < .4:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("aunt_sex_options"), Function(M_aunt.set, "sex speed", M_aunt.get("sex speed") + 0.1), Jump(game.dialog_select("aunt_sex_loop"))

    if M_aunt.get("sex speed") > .21:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("aunt_sex_options"), Function(M_aunt.set, "sex speed", M_aunt.get("sex speed") - 0.1), Jump(game.dialog_select("aunt_sex_loop"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
