label veronica_button_dialogue:
    call expression game.dialog_select("veronica_dialogue_pre")
    menu:
        "Vegetable Stock" if M_okita.is_state(S_okita_get_ingredients):
            call expression game.dialog_select("veronica_dialogue_vegatable_stock")
            $ M_okita.set("talked with veronica", True)

        "Bug spray?" if quest10 in quest_list and not infestation_done:
            call expression game.dialog_select("veronica_dialogue_bug_spray")
            menu:
                "Large wings.":
                    call expression game.dialog_select("veronica_dialogue_bug_spray_large_wings")
                "Pincers on back.":

                    call expression game.dialog_select("veronica_dialogue_bug_spray_pincers")
                "White spots.":

                    call expression game.dialog_select("veronica_dialogue_bug_spray_white_spots")
        "I'm fine.":

            call expression game.dialog_select("veronica_dialogue_leave")

    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
