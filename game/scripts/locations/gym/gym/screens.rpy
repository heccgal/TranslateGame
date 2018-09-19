screen gym:
    add game.timer.image("backgrounds/location_gym_day{}.jpg")

    if player.location.is_here(M_kevin):
        imagebutton:
            focus_mask True
            pos (136,378)
            idle "objects/object_bench_01c.png"
            hover HoverImage("objects/object_bench_01c.png")
            action Show("bench01_options")
    else:
        imagebutton:
            focus_mask True
            pos (136,458)
            idle "objects/object_bench_01.png"
            hover HoverImage("objects/object_bench_01.png")
            action Show("bench01_options")

    imagebutton:
        pos (32,380)
        focus_mask True
        idle "images/objects/character_cedric_01.png"
        hover HoverImage("images/objects/character_cedric_01.png")
        action Hide("gym"), Jump("cedric_dialogue")

    imagebutton:
        focus_mask True
        pos (414,383)
        idle "objects/object_door_10.png"
        hover HoverImage("objects/object_door_10.png")
        action Hide("gym"), Jump("yoga_room")

    imagebutton:
        focus_mask True
        pos (498,0)
        idle "objects/object_bag_01.png"
        hover HoverImage("objects/object_bag_01.png")
        action Show("bag01_options")

    imagebutton:
        focus_mask True
        align (0.5,0.97)
        idle "boxes/auto_option_generic_01.png"
        hover HoverImage("boxes/auto_option_generic_01.png")
        action Hide("gym"), Jump("gym_front")

screen bag01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bag01_options")

    imagebutton:
        focus_mask True
        align (0.5,0.82)
        idle "boxes/training_option_02.png"
        hover HoverImage("boxes/training_option_02.png")
        action If(
            game.timer.is_dark() or training_done,
            [Hide("bag01_options"), Hide("gym"), Jump("tired_training_dialogue")],
            [Hide("bag01_options"), Hide("gym"), Jump("training01_payment_dialogue")]
        )

screen bench01_options:
    imagebutton:
        idle "backgrounds/menu_ground.png"
        action Hide("bench01_options")

    imagebutton:
        focus_mask True
        align (0.5,0.82)
        idle "boxes/training_option_01.png"
        hover HoverImage("boxes/training_option_01.png")
        action If(
            game.timer.is_dark(),
            [Hide("bench01_options"), Hide("gym"), Jump("tired_training_dialogue")],
            If(
                erik.completed(erik_favor_2),
                [Hide("bench01_options"), Hide("gym"), Jump("weightlifting_dialogue")],
                [Hide("bench01_options"), Hide("gym"), Jump("cant_solo_lift")]
            )
        )
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
