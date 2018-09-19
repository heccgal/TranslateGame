label yoga_room:
    $ player.go_to(L_yoga_room)
    if mrsj.started(mrsj_yoga_help) and player.location.is_here(M_anna):
        jump expression game.dialog_select("yoga_room_mrsj_yoga_help_started")

    elif not player.location.is_here(M_mrsj) and not player.location.is_here(M_anna):
        call expression game.dialog_select("yoga_room_strangers_only")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
