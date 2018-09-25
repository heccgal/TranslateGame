label erik_dialogue:
    call expression game.dialog_select("erik_dialogue_intro")
    menu:
        "Оптические линзы." if M_okita.is_state(S_okita_get_bifocal_lenses):
            call expression game.dialog_select("erik_dialogue_okita_get_bifocal_lenses")
        "Уйти":
            call expression game.dialog_select("erik_dialogue_leave")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
