label eve_classroom_dialogue:
    scene classroom
    if M_eve.is_state(S_eve_intro):
        call expression game.dialog_select("eve_classroom_dialogue_eve_intro")
        $ L_park.unlock()
        $ M_eve.trigger(T_eve_park_hangout)
    else:

        call expression game.dialog_select("eve_classroom_dialogue_intro")
        menu eve_dialogue_options:
            "Шоу талантов." if M_dewitt.is_state([S_dewitt_talent_show_ask, S_dewitt_talent_show_ask_eve]) or M_dewitt.is_set("talent helping kevin"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin")
                else:

                    call expression game.dialog_select("eve_classroom_dialogue_talent_show_help")
                    $ M_dewitt.trigger(T_dewitt_eves_agreement)

            "Клей." if M_dewitt.is_state(S_dewitt_science_adhesive):
                call expression game.dialog_select("eve_classroom_dialogue_adehsive")
            "Награда {b}Мисс Биссетт{/b}.":

                call expression game.dialog_select("eve_classroom_dialogue_bissettes_reward")
                call expression game.dialog_select("eve_dialogue_options")
            "Тусоваться.":

                call expression game.dialog_select("eve_classroom_dialogue_hang_out")
                call expression game.dialog_select("eve_dialogue_options")
            "Уйти.":

                call expression game.dialog_select("eve_classroom_dialogue_leave")
    hide evedesk with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
