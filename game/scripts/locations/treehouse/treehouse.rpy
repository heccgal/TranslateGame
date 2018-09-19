label treehouse_dialogue:
    $ player.go_to(L_treehouse)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if L_treehouse.first_visit:
        call expression game.dialog_select("treehouse_first_visit")
        $ L_treehouse.visited()
    $ game.main()

label treehouse_closeup_dialogue:
    $ player.go_to(L_treehouse_closeup)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if L_treehouse_closeup.first_visit:
        call expression game.dialog_select("treehouse_closeup_first_visit")
        $ L_treehouse_closeup.visited()
    $ player.location.call_screen(False)

label treehouse_interior_dialogue:
    $ player.go_to(L_treehouse_interior)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if L_treehouse_interior.first_visit:
        call expression game.dialog_select("treehouse_interior_first_visit")
        $ L_treehouse_interior.visited()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
