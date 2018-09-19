screen pizzeria_exterior:
    add game.timer.image("backgrounds/location_pizza_outside_day{}.jpg")

    imagebutton:
        focus_mask True
        pos (353,465)
        idle game.timer.image("objects/object_door_37{}.png")
        hover HoverImage(game.timer.image("objects/object_door_37{}.png"))
        if not game.timer.is_dark():
            action Hide("pizzeria_exterior"), Jump("pizza_interior_dialogue")
        else:
            action Hide("pizzeria_exterior"), Jump("pizza_closed")

screen pizzeria_interior:
    add L_pizzeria_interior.background

    if M_tony.is_state(S_tony_end):
        imagebutton:
            focus_mask True
            pos (163,256)
            idle "objects/character_tony_01.png"
            hover HoverImage("objects/character_tony_01.png")
            action Hide("pizzeria_interior"), Jump("tony_dialogue")

    if M_tony.get("deliver"):
        imagebutton:
            focus_mask True
            pos (380,400)
            idle "objects/object_pizza_01.png"
            hover HoverImage("objects/object_pizza_01.png")
            action Hide("pizzeria_interior"), Jump("pizza_minigame")
    imagebutton:
        focus_mask True
        pos (0,223)
        idle game.timer.image("objects/object_door_125{}.png")
        hover HoverImage(game.timer.image("objects/object_door_125{}.png"))
        action Hide("pizzeria_interior"), Jump("pizzeria_kitchen_dialogue")

    imagebutton:
        focus_mask True
        pos (350,700)
        idle "boxes/auto_option_08.png"
        hover HoverImage("boxes/auto_option_08.png")
        action Hide("pizzeria_interior"), Jump("pizza_exterior_dialogue")

screen pizzeria_kitchen:
    add L_pizzeria_kitchen.background

    imagebutton:
        focus_mask True
        pos (142,307)
        idle game.timer.image("objects/object_door_127{}.png")
        hover HoverImage(game.timer.image("objects/object_door_127{}.png"))
        action Hide("pizzeria_kitchen"), Jump("pizza_interior_dialogue")

    imagebutton:
        focus_mask True
        pos (386,316)
        idle game.timer.image("objects/object_door_126{}.png")
        hover HoverImage(game.timer.image("objects/object_door_126{}.png"))
        action Hide("pizzeria_kitchen"), Jump("pizzeria_storage_dialogue")

screen pizzeria_storage:
    add L_pizzeria_storage.background

    imagebutton:
        focus_mask True
        pos (68,226)
        idle game.timer.image("objects/object_door_128{}.png")
        hover HoverImage(game.timer.image("objects/object_door_128{}.png"))
        action Hide("pizzeria_storage"), Jump("pizzeria_kitchen_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
