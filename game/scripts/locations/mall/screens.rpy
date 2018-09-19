screen mall:
    add "backgrounds/location_mall_day.jpg"

    imagebutton:
        focus_mask True
        pos (612,364)
        idle "objects/object_stairs_06.png"
        hover HoverImage("objects/object_stairs_06.png")
        action Hide("mall"), Jump("mall_second_floor")

    imagebutton:
        focus_mask True
        pos (761,234)
        idle "objects/object_door_22.png"
        hover HoverImage("objects/object_door_22.png")
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump(game.dialog_select("consumr"))]
        )

    imagebutton:
        focus_mask True
        pos (42,156)
        idle "objects/object_door_23.png"
        hover HoverImage("objects/object_door_23.png")
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("movie_theatre_dialogue")]
        )

    imagebutton:
        focus_mask True
        pos (541,321)
        idle "objects/object_door_53.png"
        hover HoverImage("objects/object_door_53.png")
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("comic_store_dialogue")]
        )

    imagebutton:
        focus_mask True
        pos (285,317)
        idle "objects/object_door_52.png"
        hover HoverImage("objects/object_door_52.png")
        action Hide("mall"), If(
                                M_mom.get_state() == S_mom_cupid_store,
                                Jump("mom_mall_outing_block"),
                                [Function(playSound), Jump("mall_toilets")]
        )

    if game.timer.is_weekend():
        imagebutton:
            focus_mask True
            pos (354,308)
            idle "objects/object_podium_01.png"
            hover HoverImage("objects/object_podium_01.png")
            action Hide("mall"), Jump("rump_mall_dialogue")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
