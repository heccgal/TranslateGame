label cupid_dialogue:
    $ player.go_to(L_cupid)
    if M_mom.is_state(S_mom_cupid_store):
        call expression game.dialog_select("cupid_mom_cupid_store")
        $ M_mom.trigger(T_mom_cupid_arrival)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
