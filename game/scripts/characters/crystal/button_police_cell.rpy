label crystal_cell_button:
    if M_roxxy.is_state(S_roxxy_talk_to_crystal):
        call expression game.dialog_select("crystal_police_cell_dialogue_roxxy_talk_to_crystal")
        $ player.go_to(L_map)
        $ M_roxxy.trigger(T_roxxy_find_evidence)
        $ game.timer.tick(2)
    else:
        call expression game.dialog_select("crystal_police_cell_dialogue_default")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
