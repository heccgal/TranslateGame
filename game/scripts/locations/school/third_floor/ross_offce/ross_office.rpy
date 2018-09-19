default ross_office_first_visit = True

label ross_office_dialogue:
    $ player.go_to(L_school_rossoffice)
    if game.timer.is_night():
        call expression game.dialog_select("bissette_office_night_lock")
        $ player.go_to(L_school_floor3)

    if ross_office_first_visit and not game.timer.is_dark():
        call expression game.dialog_select("ross_office_first_visit")
        $ ross_office_first_visit = False
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
