label movie_theatre_dialogue:
    $ player.go_to(L_movie_theatre)
    if L_movie_theatre.first_visit:
        call expression game.dialog_select("movie_theatre_first_visit")
        $ L_movie_theatre.visited()

    if True:
        call expression game.dialog_select("movie_theatre_movie_select_pre")
        call screen movie_options
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
