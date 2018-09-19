screen hospital_2nd_floor_room:
    add game.timer.image("backgrounds/location_hospital_room{}.jpg")

    imagebutton:
        focus_mask True
        pos (69,274)
        idle "objects/object_door_79.png"
        hover HoverImage("objects/object_door_79.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        pos (433,428)
        idle "objects/object_bed_09.png"
        hover HoverImage("objects/object_bed_09.png")
        action Show("popup_unfinished")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("hospital_2nd_floor_room"), Jump("hospital_second_floor_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
