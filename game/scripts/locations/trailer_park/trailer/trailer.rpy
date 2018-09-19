label trailer_dialogue:
    $ player.go_to(L_trailer)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_roxxy.is_state(S_roxxy_studying_at_roxxys) and game.timer.is_evening():
        call expression game.dialog_select("trailer_roxxy_studying_at_roxxys")
        $ M_roxxy.trigger(T_roxxy_study_at_mcs)

    elif M_roxxy.is_state(S_roxxy_get_uniform_on_doggo) and player.has_item("roxxy_uniform"):
        call expression game.dialog_select("trailer_roxxy_get_uniform_on_doggo")
        $ player.remove_item("roxxy_uniform")
        $ M_roxxy.trigger(T_roxxy_wait_in_her_room)
    $ game.main()

label trailer_foreclosed_dialogue:
    if M_roxxy.is_state(S_roxxy_check_trailer):
        call expression game.dialog_select("trailer_roxxy_check_trailer")
        $ M_roxxy.trigger(T_roxxy_checked_trailer)
    else:

        call expression game.dialog_select("trailer_roxxy_trailer_foreclosed")
    $ player.go_to(L_trailer)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
