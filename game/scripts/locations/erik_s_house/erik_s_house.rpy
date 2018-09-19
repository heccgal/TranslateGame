label erik_house_dialogue:
    $ player.go_to(L_erikhouse)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_morning():
        if not erik.known(erik_intro):
            call expression game.dialog_select("erikshouse_erik_intro_known")
            $ L_school_hall.unlock()
            $ erik.add_event(erik_intro)
        elif erik.started(erik_intro):
            call expression game.dialog_select("erikshouse_erik_intro_started")
        elif erik.over(erik_intro) and not game.timer.is_weekend():
            call expression game.dialog_select("erikshouse_erik_intro_over")
        elif erik.over(erik_intro) and game.timer.is_weekend():
            call expression game.dialog_select("erikshouse_erik_intro_over_weekend")
        $ game.main()
    else:
        if not mrsj.known(mrsj_intro) and game.timer.is_afternoon():
            call expression game.dialog_select("mrs_j_intro")
            $ mrsj.add_event(mrsj_intro)
    $ game.main()

label erik_house:
    $ player.go_to(L_erikhouse)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
