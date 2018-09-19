label harolds_office:
    $ player.go_to(L_miahouse_haroldsoffice)
    if M_mia.is_state(S_mia_midnight_help):
        call expression game.dialog_select("harolds_office_mia_midnight_help")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
