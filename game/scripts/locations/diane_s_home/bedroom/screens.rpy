screen dianes_bedroom:
    add game.timer.image("backgrounds/location_diane_bedroom_day{}.jpg")

    if aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack):
        imagebutton:
            focus_mask True
            pos (228,141)
            idle "images/objects/object_bed_06.png"
            hover HoverImage("images/objects/object_bed_06.png")
            action Hide("dianes_bedroom"), Jump(game.dialog_select("diane_bedroom_dialogue"))

    if aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur):
        imagebutton:
            focus_mask True
            pos (228,141)
            idle "images/objects/object_bed_07.png"
            hover HoverImage("images/objects/object_bed_07.png")
            action Hide("dianes_bedroom"), Jump(game.dialog_select("diane_bedroom_dialogue"))

    if (not aunt.known(aunt_drunken_splur) or aunt.completed(aunt_drunken_splur)) and ( not aunt.known(aunt_mouse_attack) or aunt.over(aunt_mouse_attack)):
        imagebutton:
            focus_mask True
            pos (350,700)
            idle "boxes/door19_option_01.png"
            hover HoverImage("boxes/door19_option_01.png")
            action Hide("dianes_bedroom"), Jump(game.dialog_select("dianelobby_dialogue"))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
