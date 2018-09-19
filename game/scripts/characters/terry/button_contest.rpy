label terry_button_contest_dialogue:
    if M_roxxy.is_state(S_roxxy_go_see_contest):
        call expression game.dialog_select("terry_button_contest_roxxy_go_see_contest")
        $ M_roxxy.trigger(T_roxxy_check_on_roxxy)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
