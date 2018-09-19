label home_garage:
    $ player.go_to(L_home_garage)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_dewitt.is_state([S_dewitt_garage_find_paint, S_dewitt_ask_deb_paint]):
        call expression game.dialog_select("garage_dewitt_find_paint")
        $ M_dewitt.trigger(T_dewitt_no_paint)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
