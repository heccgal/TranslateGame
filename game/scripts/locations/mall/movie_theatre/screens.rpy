screen movie_options:
    frame:
        background "movie_options"
        has hbox
        vbox:
            imagebutton:
                focus_mask True
                pos (17,181)
                idle "images/buttons/movie_option_01.png"
                hover HoverImage("images/buttons/movie_option_01.png")
                action [Hide("movie_options"), Jump("movie_theatre_movie_select_after")]

            imagebutton:
                focus_mask True
                pos (359,-190)
                idle "images/buttons/movie_option_02.png"
                hover HoverImage("images/buttons/movie_option_02.png")
                action [Hide("movie_options"), Jump("movie_theatre_movie_select_after")]

            imagebutton:
                focus_mask True
                pos (739,-592)
                idle "images/buttons/movie_option_03.png"
                hover HoverImage("images/buttons/movie_option_03.png")
                action [Hide("movie_options"), Jump("movie_theatre_movie_select_after")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
