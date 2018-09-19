label lair_dialogue:
    $ player.go_to(L_lair)
    if getPlayingMusic("<loop 89.4>audio/music_specuw.ogg"):
        $ playMusic("<loop 89.4>audio/music_specuw.ogg", 1.0)
    if getPlayingSound("<loop 8>audio/ambience_cave.ogg"):
        $ playSound("<loop 8>audio/ambience_cave.ogg", 1.0)

    if M_aqua.is_state(S_aqua_lair):
        call expression game.dialog_select("lair_aqua_lair")
        $ M_aqua.trigger(T_aqua_lair_found)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
