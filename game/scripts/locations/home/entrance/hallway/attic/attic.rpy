label attic_dialogue:
    $ player.go_to(L_home_attic)
    if L_home_attic.first_visit:
        $ L_home_attic.visited()
        call expression game.dialog_select("attic_first_visit")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
