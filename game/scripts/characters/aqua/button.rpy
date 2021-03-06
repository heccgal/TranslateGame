label aqua_dialogue:
    scene location_lair_mount
    if game.timer.is_night():
        $ player.go_to(L_map)
        call expression game.dialog_select("aqua_dialogue_night")
        $ game.main()

    elif M_aqua.is_state(S_aqua_found):
        call expression game.dialog_select("aqua_dialogue_aqua_found")
        $ player.get_item("special_lure")
        $ M_aqua.trigger(T_aqua_friended)
        $ game.main()

    elif M_aqua.is_state(S_aqua_mate):
        jump expression game.dialog_select("aqua_sex")
    else:

        call expression game.dialog_select("aqua_dialogue_pre")
    menu aqua_dialogue_options:
        "Другое.":
            call expression game.dialog_select("aqua_dialogue_the_others")
            jump expression game.dialog_select("aqua_dialogue_options")
        "Как ваши дела?":

            call expression game.dialog_select("aqua_dialogue_how_are_you")
            jump expression game.dialog_select("aqua_dialogue_options")

        "Спаривание." if M_aqua.is_state(S_aqua_mating_proposal):
            call expression game.dialog_select("aqua_dialogue_mating_pre")
            menu:
                "Меня?" if player.stats.chr() < 7:
                    call expression game.dialog_select("aqua_dialogue_mating_stat_fail")


                "Я могу помочь!" if player.stats.chr() >= 7:
                    call expression game.dialog_select("aqua_dialogue_mating_stat_pass")
                    $ M_aqua.trigger(T_aqua_mating_offer)

        "Спаривание." if M_aqua.is_state(S_aqua_valor_test):
            call expression game.dialog_select("aqua_dialogue_mating_hint")

        "Партнер." if M_aqua.is_state([S_aqua_seasucc_intro, S_aqua_seasucc_mushroom, S_aqua_end]):
            call expression game.dialog_select("aqua_dialogue_mate")
            jump expression game.dialog_select("aqua_sex")
        "Ничего.":

            call expression game.dialog_select("aqua_dialogue_nothing")

    hide player
    hide aqua
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
