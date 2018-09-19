label police_cell_larry_dialogue:
    scene police_cell
    if not erik.known(erik_father_forgive):
        call expression game.dialog_select("larry_police_cell_dialogue_erik_father_forgive_known")
        $ erik.add_event(erik_father_forgive)

    elif erik.started(erik_father_forgive):
        call expression game.dialog_select("larry_police_cell_dialogue_erik_father_forgive_started")

    elif erik.completed(erik_father_forgive) and not erik.known(erik_father_treasure):
        call expression game.dialog_select("larry_police_cell_dialogue_erik_father_treasure_not_known")
        $ erik.add_event(erik_father_treasure)

    elif erik.known(erik_father_treasure):
        call expression game.dialog_select("larry_police_cell_dialogue_erik_father_treasure_known")

    hide player
    hide larry
    hide cell_bars
    hide larry_hands
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
