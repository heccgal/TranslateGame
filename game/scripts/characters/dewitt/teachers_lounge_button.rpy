label dewitt_button_dialogue_lounge:
    call expression game.dialog_select("dewitt_dialogue_lounge_intro")

    if player.has_required_int(5):
        call expression game.dialog_select("dewitt_dialogue_lounge_stat_pass")
        call expression "player_ross_magazines_{}_left".format(M_ross.get("magazines remaining"))
        $ M_ross.set("magazine dewitt", True)
    else:

        call expression game.dialog_select("dewitt_dialogue_lounge_stat_fail")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
