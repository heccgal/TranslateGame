label trailer_park_dialogue:
    $ player.go_to(L_trailerpark)
    if M_roxxy.is_state(S_roxxy_go_to_picnic) and game.timer.is_afternoon():
        call expression game.dialog_select("trailerpark_roxxy_go_to_picnic")
        $ M_roxxy.trigger(T_roxxy_picnic_done)

        $ game.timer.tick(2)
        $ player.go_to(L_trailer_interior)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
