label cassie_pool_dialogue_rules:
    scene location_pool_closeup1
    show cassie 2 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    cas "Могу я вам чем-нибудь помочь?"
    show cassie 4
    if wearing_swimsuit:
        show player 45
    else:
        show player 108f
    player_name "Хмм... Каковы {b}правила{/b}?"
    if wearing_swimsuit:
        show player 53f
    else:
        show player 1
    show cassie 2
    cas "Ну, ты не можешь плавать в одежде..."
    show cassie 3
    cas "Вы должны использовать одну из {b}раздевалок{/b}, чтобы надеть {b}купальник{/b}!"
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    show cassie 4
    player_name "О. Отлично! Благодарю!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
