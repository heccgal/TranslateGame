label park_bushes_dialogue:
    $ player.go_to(L_park_bushes)
    if not game.timer.is_dark():
        if getPlayingSound("<loop 7 to 114>audio/ambience_suburb.ogg"):
            $ playSound("<loop 7 to 114>audio/ambience_suburb.ogg", 1.0)
    else:
        if getPlayingSound("<loop 8 to 179>audio/ambience_suburb_night.ogg"):
            $ playSound("<loop 8 to 179>audio/ambience_suburb_night.ogg", 1.0)

    if M_mia.is_state(S_mia_stolen_goods) and not erik.started(erik_father_treasure):
        call expression game.dialog_select("park_bushes_mia_stolen_goods")

    elif erik.started(erik_father_treasure):
        call expression game.dialog_select("park_bushes_erik_father_treasure_started")
    $ game.main()

label park_bushes_bag_dialogue:
    $ player.go_to(L_park_bushesbag)
    scene park_bag
    show expression "objects/object_key_02.png" at Position(xpos = 594, ypos = 473)
    if M_mia.is_state(S_mia_stolen_goods) and not erik.started(erik_father_treasure):
        call expression game.dialog_select("park_bushes_bag_mia_stolen_goods")

    elif erik.started(erik_father_treasure):
        call expression game.dialog_select("park_bushes_bag_erik_father_treasure_started")
        $ erik_father_treasure.finish()
    $ M_mia.trigger(T_harold_found_goods)
    $ M_mia.set('stolen goods recovered', True)
    $ player.location.call_screen(False)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
