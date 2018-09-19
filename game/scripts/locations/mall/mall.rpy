label mall_dialogue:
    $ player.go_to(L_mall)
    $ playSound("<loop 2 to 59>audio/ambience_mall.ogg", 1.0)

    if L_mall.first_visit:
        call expression game.dialog_select("mall_first_visit")
        $ L_mall.visited()

    if M_mom.is_state(S_mom_mall_outing):
        call expression game.dialog_select("mall_mom_mall_outing")
        $ M_mom.trigger(T_mom_mall_arrival)

    elif M_roxxy.is_state(S_roxxy_fake_id_ask_terry) and M_roxxy.get("take roxxy mall"):
        call expression game.dialog_select("mall_roxxy_fake_id_ask_terry")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
