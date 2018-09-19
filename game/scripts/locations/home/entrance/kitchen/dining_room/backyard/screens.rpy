screen backyard:
    add game.timer.image("backgrounds/location_home_backyard_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (544,365)
        idle game.timer.image("objects/object_door_65{}.png")
        hover HoverImage(game.timer.image("objects/object_door_65{}.png"))
        action Hide("backyard"), Function(renpy.call, "home_lock_check", "Dining Room", "dining_room_dialogue")

    if not game.timer.is_dark():
        imagebutton:
            focus_mask True
            pos (52,537)
            idle "objects/object_chair_02.png"
            hover HoverImage("objects/object_chair_02.png")
            action Show("popup_unfinished")

    if player.location.is_here(M_mom):
        imagebutton:
            focus_mask True
            pos (470,418)
            idle "objects/character_debbie_07.png"
            hover HoverImage("objects/character_debbie_07.png")
            action Hide("backyard"), Jump("mom_pool_dialogue")

screen mom_finger_options:
    imagebutton:
        focus_mask True
        pos (250,700)
        idle "buttons/judith_stage02_01.png"
        hover HoverImage("buttons/judith_stage02_01.png")
        action Hide("mom_finger_options"), Jump("mom_finger_loop")

    imagebutton:
        focus_mask True
        pos (450,700)
        idle "buttons/cam_stage01_02.png"
        hover HoverImage("buttons/cam_stage01_02.png")
        action Hide("mom_finger_options"), Jump("mom_finger_cum")

    if M_mom.get("sex speed") < .225:
        imagebutton:
            focus_mask True
            pos (250,735)
            idle "buttons/speed_02.png"
            hover HoverImage("buttons/speed_02.png")
            action Hide("mom_finger_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") + 0.05), Jump("mom_finger_loop")

    if M_mom.get("sex speed") > 0.126:
        imagebutton:
            focus_mask True
            pos (450,735)
            idle "buttons/speed_01.png"
            hover HoverImage("buttons/speed_01.png")
            action Hide("mom_finger_options"), Function(M_mom.set, "sex speed", M_mom.get("sex speed") - 0.025), Jump("mom_finger_loop")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
