label consumr:
    $ player.go_to(L_consumr)
    if quest10 in quest_list and not infestation_done:
        call expression game.dialog_select("consumr_quest10_not_completed")

    elif M_okita.is_state(S_okita_get_ingredients):
        call expression game.dialog_select("consumr_okita_get_ingredients")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
