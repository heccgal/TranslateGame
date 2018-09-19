label waterfall_dialogue:
    $ player.go_to(L_waterfall)
    if M_okita.is_state(S_okita_get_ingredients) and not player.has_picked_up_item("toad"):
        call expression game.dialog_select("waterfall_okita_get_ingredients")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
