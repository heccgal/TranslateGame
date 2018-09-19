label judith_button_dialogue:
    if M_judith.is_state(S_judith_start):
        call expression game.dialog_select("judith_dialogue_start")
    else:

        if player.location == L_school_lefthallway:
            call expression game.dialog_select("judith_dialogue_left_hallway_intro")

        elif player.location == L_school_artclassroom:
            call expression game.dialog_select("judith_dialogue_art_classroom_intro")
        menu:
            "Bathroom Fun" if not M_judith.is_set("sex sequence locked"):
                call expression game.dialog_select("judith_dialogue_bathroom_fun")
                $ M_judith.set("in bathroom", True)
                $ M_judith.place(place = L_school_stall)
                $ M_judith.force(tod = [0,1])
                $ L_school_girlsroom.unlock()

            "Dictionary" if not M_bissette.is_set("judith return dictionary"):
                call expression game.dialog_select("judith_dialogue_dictionary_return")
                $ M_bissette.set("judith return dictionary", True)

            "Dictionary" if M_bissette.is_state(S_bissette_find_full_dictionary):
                call expression game.dialog_select("judith_dialogue_bissette_find_full_dictionary")
                $ M_bissette.trigger(T_bissette_judith_borrow_dictionary)

            "Flute." if M_dewitt.is_state([S_dewitt_find_flute, S_dewitt_judith_locker_search]):
                call expression game.dialog_select("judith_dialogue_dewitt_find_flute")
                $ M_dewitt.trigger(T_dewitt_judith_flute)

            "Talent Show." if M_dewitt.is_set("talent ask judith"):
                if M_dewitt.is_set("talent helping kevin"):
                    call expression game.dialog_select("dewitt_talent_show_helping_kevin")

                elif M_dewitt.is_set("talent helping eve"):
                    call expression game.dialog_select("dewitt_talent_show_helping_eve")
                else:

                    call expression game.dialog_select("judith_dialogue_talent_show_help")
                    $ M_dewitt.set("talent ask judith", False)

            "Glasses." if M_okita.is_state(S_okita_get_bifocal_lenses):
                call expression game.dialog_select("judith_dialogue_okita_get_bifocal_lenses")
                $ M_okita.trigger(T_okita_take_picture_judith)

            "Picture." if M_okita.is_state(S_okita_take_picture_judith):
                call expression game.dialog_select("judith_dialogue_okita_take_picture_judith")

            "Model." if M_ross.is_state(S_ross_ask_model):
                call expression game.dialog_select("judith_dialogue_ross_ask_model")
                $ M_ross.trigger(T_ross_find_model)
            "Leave.":


                if player.location == L_school_lefthallway:
                    call expression game.dialog_select("judith_dialogue_left_hallway_leave")

                elif player.location == L_school_artclassroom:
                    call expression game.dialog_select("judith_dialogue_art_classroom_leave")
    hide judith
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
