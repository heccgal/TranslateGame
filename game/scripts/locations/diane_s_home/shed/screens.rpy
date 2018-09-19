screen dianes_shed:
    add game.timer.image("backgrounds/location_diane_shed01_day{}.jpg")

    if aunt_had_sex and player.location.is_here(M_aunt):
        imagebutton:
            focus_mask True
            pos (670,280)
            idle "objects/character_diane_04.png"
            hover HoverImage("objects/character_diane_04.png")
            action Hide("dianes_shed"), Jump(game.dialog_select("aunt_dialogue_button_night"))

    if not player.has_item("milk_carton") and quest09 in quest_list and quest09 not in completed_quests and not quest09_3:
        imagebutton:
            focus_mask True
            pos (648,499)
            idle "objects/object_milk_01.png"
            hover HoverImage("objects/object_milk_01.png")
            action Function(player.get_item, "milk_carton"), Show("milk_popup", transition = dissolve), Function(game.unlock_ui)

    if not player.has_item("pump") and quest08 not in completed_quests:
        imagebutton:
            focus_mask True
            pos (79,309)
            idle "objects/item_pump1.png"
            hover HoverImage("objects/item_pump1.png")
            action SetVariable("pump_quest_active", False), Function(player.get_item, "pump"), Show("pump_popup", transition = dissolve)

    if M_dewitt.is_state(S_dewitt_shed_get_paint):
        imagebutton:
            focus_mask True
            pos (58,608)
            idle "objects/object_paint_01.png"
            hover HoverImage("objects/object_paint_01.png")
            action Hide("dianes_shed"), Jump(game.dialog_select("dianes_shed_dewitt_paint"))

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_07.png"
        hover HoverImage("boxes/auto_option_07.png")
        action Hide("dianes_shed"), SetVariable("in_garden", True), Jump("garden_dialogue")

screen pump_popup:
    imagebutton:
        idle "boxes/popup_item_pump.png"
        action Hide("pump_popup")

screen milk_popup:
    imagebutton:
        idle "boxes/popup_item_milk.png"
        action Hide("milk_popup")

screen shed_sex_options:
    if shed_sex_action == 0:
        imagebutton:
            pos (0,700)
            idle "buttons/diane_stage01_05.png"
            hover HoverImage("buttons/diane_stage01_05.png")
            action Hide("shed_sex_options"), If(shed_cow_outfit, SetVariable("shed_cow_outfit", False), SetVariable("shed_cow_outfit", True)), Jump(game.dialog_select("shed_sex_loop"))

        imagebutton:
            pos (200,700)
            idle "buttons/judith_stage02_01.png"
            hover HoverImage("buttons/judith_stage02_01.png")
            action Hide("shed_sex_options"), Jump(game.dialog_select("shed_sex_loop"))

        imagebutton:
            pos (400,700)
            idle "buttons/diane_stage01_02.png"
            hover HoverImage("buttons/diane_stage01_02.png")
            action Hide("shed_sex_options"), Jump(game.dialog_select("shed_sex_cum"))

        if store._in_replay == None:
            imagebutton:
                pos (600,700)
                idle "buttons/diane_stage01_06.png"
                hover HoverImage("buttons/diane_stage01_06.png")
                action Hide("shed_sex_options"), SetVariable("shed_sex_action", 1), Jump(game.dialog_select("shed_sex_loop"))

        imagebutton:
            pos (800,700)
            idle "buttons/diane_stage01_04.png"
            hover HoverImage("buttons/diane_stage01_04.png")
            action Hide("shed_sex_options"), If(shed_sex_angle == 0, SetVariable("shed_sex_angle", 1), SetVariable("shed_sex_angle", 0)), Jump(game.dialog_select("shed_sex_loop"))

    else:
        imagebutton:
            pos (250,700)
            idle "buttons/judith_stage02_01.png"
            hover HoverImage("buttons/judith_stage02_01.png")
            action Hide("shed_sex_options"), Jump(game.dialog_select("shed_sex_loop"))

        imagebutton:
            pos (450,700)
            if shed_sex_action == 1:
                idle "buttons/diane_stage01_07.png"
                hover HoverImage("buttons/diane_stage01_07.png")
            elif shed_sex_action == 2:
                idle "buttons/diane_stage01_08.png"
                hover HoverImage("buttons/diane_stage01_08.png")
            elif shed_sex_action == 3:
                idle "buttons/diane_stage01_09.png"
                hover HoverImage("buttons/diane_stage01_09.png")
            action Hide("shed_sex_options"), If(shed_sex_action == 3, SetVariable("shed_sex_action", 0), SetVariable("shed_sex_action", shed_sex_action + 1)), SetVariable("shed_sex_angle", 0), Jump(game.dialog_select("shed_sex_loop"))


    if anim_toggle:
        if M_aunt.get("sex speed") < .4:
            imagebutton:
                focus_mask True
                pos (250,735)
                idle "buttons/speed_02.png"
                hover HoverImage("buttons/speed_02.png")
                action Hide("shed_sex_options"), Function(M_aunt.set, "sex speed", M_aunt.get("sex speed") + 0.1), Jump("shed_sex_loop")

        if M_aunt.get("sex speed") > .21:
            imagebutton:
                focus_mask True
                pos (450,735)
                idle "buttons/speed_01.png"
                hover HoverImage("buttons/speed_01.png")
                action Hide("shed_sex_options"), Function(M_aunt.set, "sex speed", M_aunt.get("sex speed") - 0.1), Jump("shed_sex_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
