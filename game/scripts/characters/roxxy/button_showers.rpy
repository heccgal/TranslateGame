label roxxy_button_showers_dialogue:
    if M_roxxy.is_state(S_roxxy_check_on_roxxy):
        call expression game.dialog_select("button_roxxy_showers_check_on_roxxy")
        $ M_roxxy.trigger(T_roxxy_go_to_cabin)
    elif M_roxxy.is_state(S_roxxy_in_cabin):
        call expression game.dialog_select("button_roxxy_showers_in_cabin")
    elif M_roxxy.is_state(S_roxxy_get_new_bikini):
        call expression game.dialog_select("button_roxxy_showers_get_new_bikini")
    elif M_roxxy.is_state(S_roxxy_get_oil) and player.has_item("massage_oil"):
        call expression game.dialog_select("button_roxxy_showers_get_oil")
    elif M_roxxy.is_state(S_roxxy_get_oil) and not player.has_item("massage_oil"):
        call expression game.dialog_select("button_roxxy_showers_no_oil")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
