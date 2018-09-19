label erik_backyard_dialogue:
    $ player.go_to(L_erikhouse_backyard)
    if erik.in_progress(erik_thief):
        call expression game.dialog_select("eriks_backyard_erik_thief_in_progress")
    $ game.main()

label erik_thief:

    call expression game.dialog_select("erik_thief_confront")
    if player.has_required_dex(5):
        call expression game.dialog_select("erik_thief_dex_pass")
        $ L_police_lobby.unlock()
        jump sleeping
    else:
        call expression game.dialog_select("erik_thief_dex_fail")
        jump sleeping
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
