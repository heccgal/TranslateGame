label tony_dialogue_pre:
    scene pizza_behind_c
    show xtra 12 zorder 2
    with None
    show maria 1 zorder 1 at left
    show tony 2 zorder 1 at Position(xpos=400)
    show player 1f zorder 3 at right
    with dissolve
    return

label tony_dialogue_deliver_pizzas_first:
    tony "Hey, kid!"
    tony "Ready to work?"
    show tony 1
    show player 14f
    player_name "Sure!"
    show tony 2
    show player 1f
    tony "Good! Before we start, make sure you got a {b}bicycle{/b} or something - anything - to get you around faster."
    tony "Then grab those boxes on the counter, and deliver them to the right addresses!"
    tony "Oh! Our customers love their pizzas nice and hot."
    tony "So the faster you work, the more I'll pay ya!"
    show tony 1
    show player 14f
    player_name "Sounds good, {b}Tony{/b}!"
    return

label tony_dialogue_deliver_pizzas_repeat:
    tony "The boxes are right there, kid!"
    return

label tony_dialogue_default:
    show tony 1f at right
    show player 10 at left
    tony "You need to get a bike to deliver pizzas, kiddo!"
    show player 4
    player_name "( I bet I could buy a bike at {b}Consum'r{/b}... )"
    show player 2
    player_name "Thanks, Tony. I'll get a bike and come back!"
    show tony 2f
    tony "You do, you kid!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
