label trailer_interior_dialogue:
    $ player.go_to(L_trailer_interior)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_roxxy.is_state(S_roxxy_get_cheerleader_outfit):
        call expression game.dialog_select("trailer_interior_roxxy_get_cheerleader_outfit")
        $ M_roxxy.trigger(T_roxxy_confront_clyde)

        $ player.go_to(L_trailer)

    elif M_roxxy.get("roxxy trailer sex") >= 3 and not M_crystal.is_set("crystal sex offer") and not game.timer.is_dark():
        call expression game.dialog_select("trailer_interior_crystal_sex_offer_pre_first")
        $ M_crystal.set("crystal sex offer", True)
        jump expression game.dialog_select("trailer_interior_crystal_sex_offer_menu")

    elif L_trailer_interior.first_visit:
        $ L_trailer_interior.visited()
        call expression game.dialog_select("trailer_park_first_visit")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
