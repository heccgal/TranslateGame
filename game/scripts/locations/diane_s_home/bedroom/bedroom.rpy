label dianebedroom_dialogue:
    $ player.go_to(L_diane_bedroom)
    if aunt.started(aunt_drunken_splur):
        call expression game.dialog_select("dianes_bedroom_diane_drunken_splur_started")
    $ game.main()

label diane_bedroom_dialogue:
    if aunt.known(aunt_drunken_splur) and not aunt.over(aunt_drunken_splur):
        call expression game.dialog_select("dianes_dialogue_diane_drunken_splur_known")

        $ aunt_drunken_splur.finish()

    elif aunt.known(aunt_mouse_attack) and not aunt.over(aunt_mouse_attack):
        call expression game.dialog_select("dianes_dialogue_diane_mouse_attack_known")

        $ aunt_mouse_attack.finish()
        $ aunt.complete_events(aunt_mouse_attack)
        call expression game.dialog_select("dianelobby_dialogue")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
