label music_classroom_dialogue:
    $ player.go_to(L_school_musicclassroom)
    call pa_announcement
    if player.location.is_here(M_dewitt):
        if M_dewitt.is_state(S_dewitt_intro):
            call expression game.dialog_select("music_classroom_dewitt_intro")
            $ M_dewitt.trigger(T_dewitt_mc_welcome_back)
            $ game.timer.tick()

        elif M_dewitt.is_state(S_dewitt_smith_berating):
            call expression game.dialog_select("music_classroom_dewitt_smith_berating")
            $ M_dewitt.trigger(T_dewitt_mc_overhear)

        elif M_dewitt.is_state(S_dewitt_talent_show_progress):
            call expression game.dialog_select("music_classroom_dewitt_talent_show_progress")

            $ M_dewitt.trigger(T_dewitt_talent_hunt)

        elif M_dewitt.is_state(S_dewitt_music_sheets):
            call expression game.dialog_select("music_classroom_dewitt_music_sheets")

            $ M_dewitt.trigger(T_dewitt_auditorium_problem)

        elif M_dewitt.is_state(S_dewitt_check_up):
            call expression game.dialog_select("music_classroom_dewitt_check_up")

            $ player.go_to(L_school_hall)
            $ M_dewitt.trigger(T_dewitt_crying)

        elif M_dewitt.is_state(S_dewitt_find_dewitt):
            call expression game.dialog_select("music_classroom_dewitt_find_dewitt")
            $ M_dewitt.trigger(T_dewitt_fetch_dewitt)

        elif M_dewitt.is_state(S_dewitt_talent_show_practice):
            call expression game.dialog_select("music_classroom_dewitt_talent_show_practice")
            $ game.timer.tick()
            $ M_dewitt.trigger(T_dewitt_smith_payback_plan)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
