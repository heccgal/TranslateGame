label right_hall_dialogue:
    $ player.go_to(L_school_righthallway)
    call pa_announcement
    if getPlayingSound("<loop 7 to 115>audio/ambience_school_hallway.ogg") and not game.timer.is_dark():
        $ playSound("<loop 7 to 115>audio/ambience_school_hallway.ogg", 1.0)
    if M_roxxy.is_state(S_roxxy_go_in_auditorium):
        call expression game.dialog_select("school_righthallway_roxxy_go_in_auditorium")
        $ M_roxxy.trigger(T_roxxy_invitation_bikini)
        $ player.go_to(L_school_hall)
        $ game.main()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
