label mia_library_dialogue:
    scene librarydesk
    if M_bissette.is_state(S_bissette_find_poem_reference_book) and player.location.is_here(M_mia):
        call expression game.dialog_select("mia_library_dialogue_bissette_find_poem_reference_book")
        $ M_bissette.trigger(T_bissette_mia_poem_advice)

    elif M_bissette.is_set("mia book feedback") and player.has_item("french_love"):
        call expression game.dialog_select("mia_library_dialogue_bissette_mia_book_feedback")
        $ M_bissette.set("mia book feedback", False)
    else:

        call expression game.dialog_select("mia_library_dialogue_do_not_disturb")

    hide mia
    hide player
    with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
