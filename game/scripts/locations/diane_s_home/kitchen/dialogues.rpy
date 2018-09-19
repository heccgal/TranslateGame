label dianes_kitchen_diane_breeding_bull_started:
    scene location_diane_kitchen_closeup with None
    show player 1 at left
    show diane 88 at right
    with dissolve
    pause
    show diane 89
    dia "Good morning, handsome!"
    show diane 88
    show player 36
    player_name "Good morning, {b}Diane{/b}."
    show player 13
    show diane 92
    dia "So... I've been thinking about what you said ALL night."
    dia "It's not an easy decision, and I don't want it to be something I regret."
    show diane 87
    dia "But, your proposal sounds so tempting and it has several benefits, so..."
    show diane 89
    dia "I've decided to entertain your idea and be bred!"
    show player 17
    show diane 88
    player_name "Really? I'm glad you liked the idea!"
    show player 13
    show diane 90
    dia "If I'm going to make it in this milking business, I'm going to need real, working udders!"
    show diane 87
    dia "I really want this to be a success, so I'm going to stick to the literature!"
    show diane 89
    dia "Plus the thought of {b}being bred like a bitch in heat{/b}... It turns me on more than you can imagine!"
    show diane 88
    show player 21
    player_name "Really?"
    show player 13
    show diane 90
    dia "I had to change my sheets twice lastnight!"
    show diane 92
    show player 11
    dia "But, I have this little problem..."
    show diane 89
    dia "I'm just not sure I can find, you know... a young, healthy bull!"
    dia "But, it's okay. I can start working out the details."
    show diane 88
    show player 14
    player_name "Glad I could help! I'm happy that you're happy!"
    show player 13
    show diane 89
    dia "Thank you."
    dia "Oh, and if you think you know anyone who would, you know, be suitable for me, will you let me know?"
    show diane 88
    show player 21
    player_name "Uhh... Alright!"
    hide player
    hide diane
    with dissolve
    return

label dianes_kitchen_diane_mouse_attack_started:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "Weird. She's not in here either."
    player_name "( I thought for sure... )"
    show player 11
    dia "EEEEEEKKKKKKK!"
    show player 23f
    player_name "What the..."
    player_name "( Is that {b}Diane{/b} screaming?! )"
    hide player with dissolve
    return

label dianes_kitchen_diane_drunken_splur_not_known:
    scene dianekitchen1
    player_name "( There's no one here. )"
    player_name "( {b}Diane{/b} is outside by the garden. )"
    return

label mouse_attack:
    scene dianekitchen with None
    show player 10 with dissolve
    player_name "( I can't just leave, {b}Diane{/b} might be in trouble. )"
    hide player with dissolve
    $ game.main()

label dianes_kitchen_diane_kitchen_drink_intro:
    scene dianekitchen
    show player 133 with dissolve
    player_name "( This should be it... )"
    show player 135
    player_name "Annnd... there."
    show player 132
    show expression "characters/xtra/char_xtra_01.png" at Position(xpos = 638, ypos = 519)
    player_name "Hmm..."
    show player 133
    player_name "( Maybe I should add a bit more? )"
    return

label dianes_kitchen_diane_kitchen_drink_no:
    show player 133
    player_name "Nah. That should be enough..."
    player_name "( {b}Diane{/b} gets a little bit too... Loving, when she has a few drinks. )"
    show player 134
    player_name "( That'll do... )"
    return

label dianes_kitchen_diane_kitchen_drink_yes:
    show player 135
    player_name "Juuuust... a {b}little bit more{/b}!"
    show player 134
    player_name "( That'll do... )"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
