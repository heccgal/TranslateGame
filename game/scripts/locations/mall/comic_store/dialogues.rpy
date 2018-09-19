label comic_store_june_cosplay_started:
    scene comic_b
    show player 14 with dissolve
    player_name "Looks like they have some costumes hanging on the wall."
    player_name "I should have a look at them..."
    player_name "... maybe they have those orc cosplay pieces."
    hide player with dissolve
    return

label comic_store_erik_vr_started_have_all:
    show player 14 with dissolve
    player_name "( I think that's all {b}Erik{/b} wanted. )"
    player_name "( Let's get back to him... )"
    hide player with dissolve
    return

label comic_store_erik_vr_started_do_not_have_all:
    show player 35 with dissolve
    player_name "( They must have the things {b}Erik{/b} wanted in here somewhere. )"
    show player 12 with dissolve
    player_name "( Maybe in those shelves by the counter? )"
    hide player with dissolve
    return

label comic_store_first_visit:
    scene comic_b
    show player 1 at left
    show tatia 3 at right
    with dissolve
    tati "Hi!"
    show tatia 2
    tati "First time visiting {b}Cosmic Cumics{/b}?"
    show tatia 1
    show player 29
    player_name "Umm... Yeah! I didn't know this place existed..."
    show tatia 2
    show player 1
    tati "Yeah we just opened recently!"
    show tatia 1
    show player 2
    player_name "Oh, cool!"
    player_name "You guys sell video games, too?"
    show tatia 3
    show player 1
    tati "Of course."
    show tatia 2
    tati "We sell a variety of products ranging from {b}video games{/b},{b}comic books{/b}, {b}figurines{/b}, {b}posters{/b} and {b}collectibles{/b}!"
    show tatia 1
    show player 2
    player_name "Oh. So... nerd stuff..."
    show tatia 3
    show player 1
    tati "Yup!"
    tati "Have a look around, and let me know if you need help with anything!"
    hide tatia
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
