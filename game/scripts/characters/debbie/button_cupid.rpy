label mom_cupid_outing:
    scene location_mall_cupid_blur
    if M_mom.is_state(S_mom_choose_gift):
        call expression game.dialog_select("mom_cupid_outing_choose_gift")

    elif M_mom.is_state(S_mom_show_necklace):
        $ player.remove_item("pearl_necklace")
        call expression game.dialog_select("mom_cupid_outing_show_necklace")
        $ M_mom.trigger(T_mom_give_necklace)
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
