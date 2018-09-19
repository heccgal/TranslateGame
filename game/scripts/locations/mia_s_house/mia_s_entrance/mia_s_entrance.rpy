label mias_entrance:
    $ player.go_to(L_miahouse_entrance)
    if not game.timer.is_dark():
        $ playSound("<loop 7 to 114>audio/ambience_house_entrance.ogg")

    if M_mia.is_state(S_mia_parent_blocking):
        call expression game.dialog_select("mias_entrance_mia_parent_blocking")
        $ L_church_front.unlock()
        $ L_police_lobby.unlock()
        $ M_mia.trigger(T_mia_kicked_out)
        jump expression game.dialog_select("mias_house_dialogue")

    elif M_mia.is_state(S_mia_helen_fight):
        call expression game.dialog_select("mias_entrance_mia_helen_fight")
        $ M_mia.trigger(T_mias_request)

    elif M_mia.is_state(S_mia_helen_refusal):
        call expression game.dialog_select("mias_entrance_mia_helen_refusal")
        $ M_mia.trigger(T_mia_church_mention)


    elif M_mia.is_state(S_mia_urgent_help):
        call expression game.dialog_select("mias_entrance_mia_urgent_help")
        $ M_mia.trigger(T_harold_missing)

    elif M_mia.is_state(S_mia_harold_found_news):
        call expression game.dialog_select("mias_entrance_mia_harold_found_news")
        $ M_mia.trigger(T_mia_give_news)

    elif M_mia.is_state(S_mia_route_split):
        call expression game.dialog_select("mias_entrance_mia_route_split")
        $ M_mia.trigger(T_mia_family_reunion)

    elif M_helen.is_state([S_helen_route_split, S_helen_harold_moved_on]):
        call expression game.dialog_select("mias_entrance_helen_route_split")
        $ M_helen.trigger(T_helen_master_servant)

    elif M_mia.is_state(S_mia_unexpected_visit) and game.timer.is_afternoon():
        call expression game.dialog_select("mias_entrance_mia_unexpected_visit")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
