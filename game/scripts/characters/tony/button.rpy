label tony_dialogue:
    call expression game.dialog_select("tony_dialogue_pre")
    if not M_tony.is_set("deliver") and player.transport_level > 0:
        call expression game.dialog_select("tony_dialogue_deliver_pizzas_first")
        $ M_tony.set("deliver", True)

    elif M_tony.is_set("deliver"):
        call expression game.dialog_select("tony_dialogue_deliver_pizzas_repeat")
    else:
        call expression game.dialog_select("tony_dialogue_default")

    hide player
    hide tony
    hide maria
    with dissolve
    hide xtra
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
