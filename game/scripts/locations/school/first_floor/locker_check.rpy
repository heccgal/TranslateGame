label locker_check(direction, locker):
    if direction == "left":
        show expression game.timer.image("backgrounds/location_school_lefthall{}.jpg")
    else:
        show expression game.timer.image("backgrounds/location_school_right_hall{}.jpg")
    show player 1 at center
    if player.has_picked_up_item("master_key"):
        if not locker.is_visited:
            $ charname = locker.name.split("'")[0]
            player_name "Using the master key I was able to open {b}[charname]'s{/b} locker."
        $ player.location = locker
    else:
        call expression "locker_locked_{}".format(random.randint(1,2))
        $ game.main()
    scene expression locker.background
    return

label locker_locked_1:
    show player 10 with dissolve
    player_name "That's not my locker... I would need a key to open it."
    return

label locker_locked_2:
    player_name "It's locked and I don't have the key."
    player_name "{b}Principal Smith{/b} probably has a key to everything."
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
