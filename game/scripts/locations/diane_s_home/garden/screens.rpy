screen dianes_garden:
    if not game.timer.is_dark():
        add "backgrounds/location_diane_garden_day.jpg"

        imagebutton:
            focus_mask True
            pos (26,369)
            idle "objects/object_door_08.png"
            hover HoverImage("objects/object_door_08.png")
            action If(
                aunt_count == 5 and not aunt_dialogue_advance,
                If(
                    game.timer.is_dark(),
                    [Hide("dianes_garden"), Jump(game.dialog_select("night_closed_garden"))],
                    If(
                        aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur),
                        [Hide("dianes_garden"), Play("audio", sfxDoor()), Jump(game.dialog_select("kitchen_dialogue"))],
                        [Hide("dianes_garden"), Jump(game.dialog_select("aunt_masturbate"))]
                    )
                ),
                If(aunt_count == 5 and aunt_dialogue_advance ,
                   If(
                        game.timer.is_dark(),
                        [Hide("dianes_garden"), Jump(game.dialog_select("night_closed_garden"))],
                        [Hide("dianes_garden"), Jump("after_masturbation")]
                   ),
                   If(
                        game.timer.is_dark(),
                        [Hide("dianes_garden"), Jump(game.dialog_select("night_closed_garden"))],
                        [Hide("dianes_garden"), Play("audio", sfxDoor()), Jump(game.dialog_select("kitchen_dialogue"))]
                   )
                )
            )

        imagebutton:
            focus_mask True
            pos (686,345)
            idle "objects/object_door_09.png"
            hover HoverImage("objects/object_door_09.png")
            action If(
                game.timer.is_dark(),
                [Hide("dianes_garden"),
                 If(
                    not game.timer.is_night(),
                    If(
                        shed_unlocked,
                        [Function(playSound), Jump(game.dialog_select("shed"))],
                        Jump(game.dialog_select("night_closed_garden"))
                    ),
                    Jump(game.dialog_select("night_closed_garden"))
                 )
                ],
                [Hide("dianes_garden"),
                 If(
                    shed_unlocked or (M_dewitt.is_state(S_dewitt_shed_get_paint) and not player.has_item("paint")),
                    [Function(playSound), Play("audio", "audio/sfx_door_heavy.ogg"), Jump(game.dialog_select("shed"))],
                    Jump(game.dialog_select("locked_shed_dialogue"))
                 )
                ]
            )

        if (not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)) and (not aunt.known(aunt_drunken_splur) or aunt.over(aunt_drunken_splur)):
            if quest10 in quest_list and not infestation_done:
                $ garden_img_i = "objects/object_garden_01_dead.png"
                $ garden_img_h = HoverImage("objects/object_garden_01_dead.png")
            else:
                $ garden_img_i = "objects/object_garden_01.png"
                $ garden_img_h = HoverImage("objects/object_garden_01.png")
            imagebutton:
                focus_mask True
                pos (36,535)
                idle garden_img_i
                hover garden_img_h
                action Show("garden01_options")

        if (not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)) and (not aunt.known(aunt_drunken_splur) or aunt.over(aunt_drunken_splur)):
            if aunt_count < 8:
                if aunt_count != 5:
                    imagebutton:
                        focus_mask True
                        pos (491,397)
                        if aunt_drink_made:
                            idle "objects/character_diane_03.png"
                            hover HoverImage("objects/character_diane_03.png")
                        else:
                            idle "objects/character_diane_01.png"
                            hover HoverImage("objects/character_diane_01.png")
                        action Hide("dianes_garden"), Jump(game.dialog_select("aunt_button_dialogue"))

    else:
        add "backgrounds/location_diane_garden_night.jpg"
        imagebutton:
            focus_mask True
            pos (26,369)
            idle "objects/object_door_08_night.png"
            hover HoverImage("objects/object_door_08_night.png")
            action If(
                aunt_count == 5 and not aunt_dialogue_advance,
                If(
                    game.timer.is_dark(),
                    [Hide("dianes_garden"), Jump(game.dialog_select("night_closed_garden"))],
                    [Hide("dianes_garden"), Jump(game.dialog_select("aunt_masturbate"))]
                ),
                If(
                    aunt_count == 5 and aunt_dialogue_advance,
                    If(
                        game.timer.is_dark(),
                        [Hide("dianes_garden"), Jump(game.dialog_select("night_closed_garden"))],
                        [Hide("dianes_garden"), Jump("after_masturbation")]
                    ),
                    If(
                        game.timer.is_dark(),
                        [Hide("dianes_garden"), Jump(game.dialog_select("night_closed_garden"))],
                        [Hide("dianes_garden"), Function(playSound), Jump(game.dialog_select("kitchen_dialogue"))]
                    )
                )
            )

        if quest09 in completed_quests and not aunt_shed_scene:
            imagebutton:
                focus_mask True
                pos (686,315)
                idle "objects/object_door_09_night02.png"
                hover HoverImage("objects/object_door_09_night02.png")
                action If(
                    game.timer.is_dark(),
                    [Hide("dianes_garden"),
                     If(
                        not game.timer.is_night(),
                        If(
                            shed_unlocked,
                            [Function(playSound), Jump(game.dialog_select("shed"))],
                            Jump(game.dialog_select("night_closed_garden"))
                        ),
                        Jump(game.dialog_select("night_closed_garden"))
                     )
                    ],
                    [Hide("dianes_garden"),
                     If(
                        shed_unlocked,
                        [Function(playSound), Jump(game.dialog_select("shed"))],
                        Jump(game.dialog_select("locked_shed_dialogue"))
                     )
                    ]
                )

        else:
            imagebutton:
                focus_mask True
                pos (686,345)
                idle "objects/object_door_09_night.png"
                hover HoverImage("objects/object_door_09_night.png")
                action If(
                    game.timer.is_dark(),
                    [Hide("dianes_garden"),
                     If(
                        not game.timer.is_night(),
                        If(
                            shed_unlocked,
                            [Function(playSound), Jump(game.dialog_select("shed"))],
                            Jump(game.dialog_select("night_closed_garden"))
                        ),
                        Jump(game.dialog_select("night_closed_garden"))
                     )
                    ],
                    [Hide("dianes_garden"),
                     If(
                        shed_unlocked,
                        [Function(playSound), Jump(game.dialog_select("shed"))],
                        Jump(game.dialog_select("locked_shed_dialogue"))
                     )
                    ]
                )

        if quest10 in quest_list and not infestation_done:
            $ garden_img_i = "objects/object_garden_01_dead_night.png"
            $ garden_img_h = HoverImage("objects/object_garden_01_dead_night.png")

        else:
            $ garden_img_i = "objects/object_garden_01_night.png"
            $ garden_img_h = HoverImage("objects/object_garden_01_night.png")

        imagebutton:
            focus_mask True
            pos (36,535)
            idle garden_img_i
            hover garden_img_h
            action Show("garden01_options")

    if False:
        imagebutton:
            focus_mask True
            if not game.timer.is_dark():
                pos (928,420)
            else:
                pos (928,418)
            idle game.timer.image("objects/object_crack_02{}.png")
            hover HoverImage(game.timer.image("objects/object_crack_02{}.png"))
            action Show("popup_unfinished")

    else:
        imagebutton:
            focus_mask True
            if not game.timer.is_dark():
                pos (928,420)
            else:
                pos (928,416)
            idle game.timer.image("objects/object_crack_01{}.png")
            hover HoverImage(game.timer.image("objects/object_crack_01{}.png"))
            action Hide("dianes_garden"), Jump("church_graveyard_dialogue")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("dianes_garden"), Jump("diane_front_yard")

screen garden01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("garden01_options")

    imagebutton:
        focus_mask True
        align (0.5,0.82)
        idle "boxes/garden_option_01.png"
        hover HoverImage("boxes/garden_option_01.png")
        if quest20 not in completed_quests:
            action Hide("garden01_options"), Hide("dianes_garden"), Jump(game.dialog_select("find_shovel"))

        elif aunt_drink_offered:
            action Hide("garden01_options"), Hide("dianes_garden"), Jump(game.dialog_select("drink_offered"))

        elif aunt_count == 5 and not aunt_dialogue_advance:
            action Hide("garden01_options"), Hide("dianes_garden"), Jump(game.dialog_select("before_masturbation"))

        elif aunt_count == 5 and aunt_dialogue_advance:
            action Hide("garden01_options"), Hide("dianes_garden"), Jump("after_masturbation")

        else:
            action If(
                game.timer.is_dark(),
                [Hide("garden01_options"), Hide("dianes_garden"), Jump(game.dialog_select("night_closed_garden"))],
                [Hide("garden01_options"), Hide("dianes_garden"), Jump("garden_listing")]
            )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
