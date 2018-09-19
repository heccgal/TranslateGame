label pizza_exterior_first_visit:
    scene expression game.timer.image("backgrounds/location_pizza_outside_day{}.jpg")
    show player 14 with dissolve
    player_name "( Tony’s Pizza. He’s known to make the best pizza in town. )"
    hide player with dissolve
    return

label pizza_interior_pizza_count_0:
    scene location_pizza_day_blur
    show player 10f at right with dissolve
    show tony 1 at Position(xpos = 300, ypos = 768) with dissolve
    player_name "Hey! Is anyone in-"
    show tony 2
    show player 11f
    tony "Eyyy, look at this one!"
    tony "Tall, young, handsome."
    tony "He reminds me of myself, when I was younger."
    show tony 1
    show player 10f
    player_name "Me?"
    show tony 3
    show player 13f
    tony "Yes you, tell you what: You looking for a job?"
    show tony 1
    show player 14f
    player_name "Yeah, I've been looking for one."
    show tony 2
    show player 203f
    tony "Good. I could use someone like you."
    show player 10f
    show tony 1
    player_name "Someone like me?"
    show player 11f
    show tony 2
    tony "Of course! Someone like you! Wait here let me get my wife."
    show player 203f
    show maria 1 at left
    show tony 2
    tony "Maria: this is {b}[firstname]{/b}, {b}[firstname]{/b}: this is Maria."
    show tony 1
    show maria 2
    maria "Hey, {b}[firstname]{/b}. I'm guessing you're going to be the new help."
    show player 14f
    show maria 1
    player_name "Yeah, seems like it."
    show player 203f
    show maria 3
    maria "Tony quick question: Do we know if this kid is any good?"
    show maria 1
    show tony 2
    tony "We don't, but look at him! He's young, full of energy, and he looks healthy!"
    tony "What else would you need?"
    show maria 2
    show player 11f
    show tony 1
    maria "Someone who works, because the last kid you hired was another lazy teen."
    show maria 1
    show tony 3
    tony "He'll work. I can promise you that. Right {b}[firstname]{/b}?"
    show tony 1
    show player 14f
    player_name "Yeah. You're offering, and I need the job."
    show tony 2
    show player 203f
    tony "Then it's settled! Come in later, and we'll discuss things further."
    show maria 2
    tonymaria "Have a great day!"
    hide tony
    hide maria
    hide player
    with dissolve
    return

label pizza_closed:
    scene expression "backgrounds/location_pizza_outside_night.jpg"
    show player 14 with dissolve
    player_name "I can't go there at night!"
    hide player with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
