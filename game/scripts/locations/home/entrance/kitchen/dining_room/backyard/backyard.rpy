label backyard_dialogue:
    $ player.go_to(L_home_backyard)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_mom.is_state(S_mom_midnight_search):
        jump expression game.dialog_select("mom_midnight_swim")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
