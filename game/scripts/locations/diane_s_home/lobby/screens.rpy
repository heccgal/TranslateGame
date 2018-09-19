screen dianes_lobby:
    add "backgrounds/location_diane_entrance_day.jpg"

    if aunt.over(aunt_mouse_attack) and (not aunt.known(aunt_drunken_splur) or aunt.completed(aunt_drunken_splur)):
        imagebutton:
            focus_mask True
            pos (700,431)
            idle "objects/object_door_56.png"
            hover HoverImage("objects/object_door_56.png")
            action Hide("dianes_lobby"), Play("audio", sfxDoor()), Jump("diane_front_yard")

        imagebutton:
            focus_mask True
            pos (26,193)
            idle "objects/object_door_57.png"
            hover HoverImage("objects/object_door_57.png")
            action Hide("dianes_lobby"), Jump(game.dialog_select("kitchen_dialogue"))

    imagebutton:
        focus_mask True
        pos (369,93)
        idle "objects/object_door_58.png"
        hover HoverImage("objects/object_door_58.png")
        action Hide("dianes_lobby"), Play("audio", sfxDoor()), Jump("dianebedroom_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
