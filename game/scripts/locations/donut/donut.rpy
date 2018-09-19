label donut_shop_dialogue:
    $ player.go_to(L_donutshop)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ game.main()

label donut_interior_dialogue:
    $ player.go_to(L_donutshop_interior)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
