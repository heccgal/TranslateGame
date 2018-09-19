label church_angelicas_room_dialogue:
    $ player.go_to(L_church_angelica)
    if M_mia.is_state(S_mia_church_plan) and game.timer.is_weekend() and game.timer.is_morning():
        call expression game.dialog_select("church_angelicas_room_mia_church_plan")

    elif M_mia.is_state(S_mia_return_priest_outfit):
        call expression game.dialog_select("church_angelicas_room_mia_return_priest_outfit")

        $ game.timer.tick()

        $ M_mia.trigger(T_mia_priest_outfit)

    elif M_mia.is_state(S_mia_church_night_visit) and game.timer.is_dark():
        call expression game.dialog_select("church_angelicas_room_mia_church_night_visit")
        $ M_mia.trigger(T_angelica_ritual_deal)

    elif M_mia.is_state(S_mia_church_sacrement) and game.timer.is_dark():
        call expression game.dialog_select("church_angelicas_room_mia_church_sacrement")
        $ game.timer.tick()
        $ M_mia.trigger(T_helen_angelica_ritual)
        $ player.go_to(L_map)

    elif M_mia.is_state(S_mia_angelicas_order) and game.timer.is_dark():
        call expression game.dialog_select("church_angelicas_room_mia_angelicas_order")
        $ M_mia.trigger(T_angelica_sinful_thoughts)

    elif M_mia.is_state(S_mia_angelicas_final_request) and player.has_item("strapon") and game.timer.is_dark():
        $ player.go_to(L_church_stairs)
        call screen route_warning
        $ player.go_to(L_church_angelica)
        jump expression game.dialog_select("helen_final_sacrament")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
