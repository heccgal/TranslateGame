label third_floor_dialogue:
    $ player.go_to(L_school_floor3)
    call pa_announcement
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)

    if M_okita.is_state(S_okita_get_ingredients) and not player.has_item("tissue") and not M_dewitt.is_state(S_dewitt_paint_trail):
        call expression game.dialog_select("third_floor_okita_get_ingredients")
    elif M_roxxy.is_state(S_roxxy_teachers_event) and not game.timer.is_dark():
        call expression game.dialog_select("third_floor_roxxy_intro")
    if M_bissette.is_state(S_bissette_end):
        $ M_bissette.set("night visit", True)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
