label tatiana_dialogue_pre:
    scene comic_c
    show xtra 17 zorder 2
    show tatia 2 zorder 1 at right
    show player 1 zorder 3 at left
    with dissolve
    tati "What's up?"
    show tatia 1
    return

label tatiana_dialogue_familiar:
    show player 4
    player_name "I feel like I've seen you somewhere."
    show tatia 3
    show player 1
    tati "Right. Well, you've probably seen me on the internet..."
    show tatia 2
    tati "I do a lot of {b}video game streams{/b} and I post them on my {b}YT channel{/b}."
    show tatia 4
    tati "I usually go by the name of {b}PureRuby87{/b}."
    show tatia 5
    show player 17
    player_name "Oh, right! My friend {b}Erik{/b} loves your stuff!"
    show player 21
    player_name "He keeps talking about your videos and your {b}huge{/b}... err... fan base!"
    show tatia 3
    show player 1
    tati "Aww... You guys are so sweet."
    show tatia 2
    tati "Is there anything else you want to talk about?"
    show tatia 1
    return

label tatiana_dialogue_suggestions:
    show player 2
    player_name "Do you have any suggestions? New products that you would recommend?"
    show player 1
    tati "Hmmm..."
    show tatia 2
    tati "Well, I really love {b}cosplay{/b}!"
    show tatia 4
    tati "I like to wear {b}sexy outfits{/b}. Actually, we have a new line of costumes that just came in!"
    show tatia 5
    show player 21
    player_name "Oh, yeah? Sounds interesting..."
    show tatia 4
    show player 1
    tati "It's sometimes hard to fit my... umm... forms into them."
    tati "They make them so tight, you know?"
    show tatia 3
    tati "But guys usually don't seem to mind!"
    show tatia 5
    show player 29
    player_name "Haha. I see."
    show player 2
    player_name "Thanks, I'll have a look."
    show tatia 1
    return

label tatiana_dialogue_leave:
    show player 2
    player_name "Yeah, I think I have everything I need. Thanks!"
    show tatia 2
    show player 1
    tati "Great! Thanks for shopping at {b}Cosmic Cumics{/b}..."
    show tatia 3
    show player 13
    tati "And tell your friends about us!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
