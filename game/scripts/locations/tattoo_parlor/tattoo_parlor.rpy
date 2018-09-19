label tattoo_parlor_dialogue:
    $ player.go_to(L_tattooparlor)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)
    $ game.main()

label tattoo_parlor_interior_dialogue:
    $ player.go_to(L_tattooparlor_interior)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if L_tattooparlor_interior.first_visit:
        $ L_tattooparlor_interior.visited()
        call expression game.dialog_select("tattooparlor_first_visit")

    if M_mia.is_state(S_mia_get_tattoo) and player.location.is_here(M_mia):
        call expression game.dialog_select("tattooparlor_mia_get_tattoo")
        $ M_mia.trigger(T_mia_visit_tattoo_parlor)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
