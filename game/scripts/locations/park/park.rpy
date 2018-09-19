label park_dialogue:
    $ player.go_to(L_park)
    if game.timer.is_dark():
        if getPlayingMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg"):
            $ playMusic("<loop 108.292 to 180.658>audio/music_rap_distant.ogg")

    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:

        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if game.timer.is_dark() and L_park.first_visit:
        call expression game.dialog_select("park_count_night_0")
        $ L_park.visited()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
