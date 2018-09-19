label church_graveyard_dialogue:
    $ player.go_to(L_church_graveyard)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 2>audio/ambience_graveyard.ogg"):
            $ playSound("<loop 2>audio/ambience_graveyard.ogg")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
