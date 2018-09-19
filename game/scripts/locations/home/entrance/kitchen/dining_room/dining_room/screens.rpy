screen dining_room:
    add game.timer.image("backgrounds/location_home_diningroom_day{}.jpg")

    if game.timer.is_morning() and sister.known(sis_breakfast) and not sister.over(sis_breakfast):
        imagebutton:
            focus_mask True
            pos (158,439)
            idle "images/objects/object_table_02_jenny.png"
            hover HoverImage("images/objects/object_table_02_jenny.png")
            action Hide("dining_room"), Function(renpy.call, "home_lock_check", "Dining Room Table Sis", "dining_room_table_sis")

    else:
        imagebutton:
            focus_mask True
            pos (158,484)
            idle game.timer.image("objects/object_table_02{}.png")
            hover HoverImage(game.timer.image("objects/object_table_02{}.png"))
            action Hide("dining_room"), Function(renpy.call, "home_lock_check", "Dining Room Table", "dining_room_table_dialogue")

    imagebutton:
        focus_mask True
        pos (952,288)
        idle game.timer.image("objects/object_door_45{}.png")
        hover HoverImage(game.timer.image("objects/object_door_45{}.png"))
        action Hide("dining_room"), Function(renpy.call, "home_lock_check", "Kitchen", "home_kitchen_dialogue")

    imagebutton:
        focus_mask True
        pos (27,293)
        idle game.timer.image("objects/object_door_46{}.png")
        hover HoverImage(game.timer.image("objects/object_door_46{}.png"))
        action Hide("dining_room"), Function(renpy.call, "home_lock_check", "Backyard", "backyard_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
