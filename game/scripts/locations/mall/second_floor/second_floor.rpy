label mall_second_floor:
    $ player.go_to(L_mall_floor2)
    $ playSound("<loop 2 to 59>audio/ambience_mall.ogg", 1.0)
    $ game.main()

label photo_booth_dialogue:
    $ player.go_to(L_mall_photobooth)
    if M_roxxy.is_state(S_roxxy_fake_id_ask_terry) and M_roxxy.get("take roxxy mall"):
        call expression game.dialog_select("photo_booth_roxxy_take_picture")
        $ player.get_item("roxxy_picture")
        $ M_roxxy.trigger(T_roxxy_take_picture)
        $ game.timer.tick(1)
    else:

        if not L_mall_photobooth.visited:
            call expression game.dialog_select("photo_booth_first_visit")
        call expression game.dialog_select("photo_booth_generic_dialogue")
    $ player.go_to(L_mall_floor2)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
