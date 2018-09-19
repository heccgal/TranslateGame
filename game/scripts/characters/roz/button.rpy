label roz_dialogue:
    call expression game.dialog_select("roz_dialogue_intro")
    if not Roz.known(roz_intro):
        $ Roz.add_event(roz_intro)
        $ roz_intro.finish()
    menu roz_dialogue_options:
        "1st floor?":
            call expression game.dialog_select("roz_dialogue_1st_floor")
            jump expression game.dialog_select("roz_dialogue_options")
        "2nd floor?":

            call expression game.dialog_select("roz_dialogue_2nd_floor")
            jump expression game.dialog_select("roz_dialogue_options")
        "Schedule.":

            call expression game.dialog_select("roz_dialogue_schedule")
            jump expression game.dialog_select("roz_dialogue_options")

        "Ancestry." if M_aqua.is_state(S_aqua_boatsmith_search) and M_roz.is_state(S_roz_start):
            call expression game.dialog_select("roz_dialogue_ancestory")
            $ M_roz.trigger(T_roz_favour)
            $ M_roz.set("fun time", True)

        "Go on break." if M_roz.is_state(S_roz_end) and not M_roz.is_set("fun time"):
            call expression game.dialog_select("roz_dialogue_go_on_break")
            $ M_roz.set("fun time", True)
        "Nothing.":

            call expression game.dialog_select("roz_dialogue_nothing")

    hide player
    hide roz
    hide roz_desk
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
