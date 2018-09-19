label mias_bedroom_screen:
    $ player.go_to(L_miahouse_miaroom)
    if M_mia.is_state(S_mia_tattoo_help):
        call expression game.dialog_select("mias_bedroom_mia_tattoo_help")
        $ game.timer.tick()
        $ M_mia.trigger(T_mia_delay)
        $ player.go_to(L_miahouse)

    elif M_mia.is_state(S_mia_midnight_help):
        call expression game.dialog_select("mias_bedroom_mia_midnight_help")

    elif M_mia.is_state(S_mia_study_sex):
        jump expression game.dialog_select("mia_bedroom_sex")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
