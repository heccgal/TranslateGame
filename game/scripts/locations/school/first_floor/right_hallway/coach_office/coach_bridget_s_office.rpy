label coach_office_dialogue:
    $ player.go_to(L_school_bridgetoffice)
    if M_bissette.is_state(S_bissette_roxxy_pom_poms):
        call expression game.dialog_select("coachs_office_roxxy_pom_poms")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
