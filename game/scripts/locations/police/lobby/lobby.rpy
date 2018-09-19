label police_lobby_dialogue:
    $ player.go_to(L_police_lobby)
    if L_police_lobby.first_visit:
        call expression game.dialog_select("police_lobby_first_visit")
        $ L_police_lobby.visited()

    if M_mia.is_state(S_mia_clues):
        call expression game.dialog_select("police_lobby_mia_clues")

    elif M_roxxy.is_state(S_roxxy_ask_earl_release):
        call expression game.dialog_select("police_lobby_roxxy_ask_earl_release")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
