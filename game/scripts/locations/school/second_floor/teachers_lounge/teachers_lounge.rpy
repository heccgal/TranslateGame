default teach_lounge_first_visit = True

label teach_lounge_dialogue:
    $ player.go_to(L_school_teacherslounge)
    call pa_announcement
    if teach_lounge_first_visit and not game.timer.is_dark():
        call expression game.dialog_select("teachers_lounge_first_visit")
        $ teach_lounge_first_visit = False

    elif M_okita.is_state(S_okita_dose_smith) and game.timer.is_afternoon():
        call expression game.dialog_select("teachers_lounge_okita_dose_smith")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
