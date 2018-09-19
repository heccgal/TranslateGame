label mias_upstairs:
    $ player.go_to(L_miahouse_upstairs)
    if M_mia.is_state([S_mia_consult, S_mia_impress_harold, S_mia_parent_unblock, S_mia_strip_aftermath, S_mia_midnight_call]) and game.timer.is_dark():
        call expression game.dialog_select("mias_upstairs_mia_parent_unblock")
        $ player.go_to(L_miahouse)

    elif M_mia.is_state([S_mia_midnight_help, S_mia_locked_room]):
        call expression game.dialog_select("mias_upstairs_mia_midnight_help")

    elif M_mia.is_state(S_mia_unexpected_visit) and game.timer.is_afternoon():
        call expression game.dialog_select("mias_upstairs_mia_unexpected_visit")

    elif M_helen.is_state(S_helen_aftersex_mia_suspicious):
        call expression game.dialog_select("mias_upstairs_helen_aftersex_mia_suspicious")

        $ game.timer.tick()
        $ M_helen.trigger(T_mia_stay_alone)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
