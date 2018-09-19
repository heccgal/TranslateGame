label backroom_dialogue:
    $ player.go_to(L_library_backroom)
    if backroom_count == 0:
        call expression game.dialog_select("backroom_dialogue_backroom_count")
        call screen backroom_couple_sex
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
