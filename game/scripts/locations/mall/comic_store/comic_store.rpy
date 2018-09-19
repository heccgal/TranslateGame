label comic_store_dialogue:
    $ player.go_to(L_comicstore)
    if June.started(june_cosplay) and not player.has_item("orcette_cosplay"):
        call expression game.dialog_select("comic_store_june_cosplay_started")

    elif erik.started(erik_vr):
        scene comic_b
        if player.has_item("game02") and player.has_item("virtualsaga"):
            call expression game.dialog_select("comic_store_erik_vr_started_have_all")
        else:

            call expression game.dialog_select("comic_store_erik_vr_started_do_not_have_all")

    elif L_comicstore.first_visit:
        call expression game.dialog_select("comic_store_first_visit")
        $ L_comicstore.visited()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
