label beth_dialogue_pre:
    scene donut_c
    show beth 2 zorder 1 at right
    show xtra 27 zorder 2 at center
    show player 1 zorder 3 at left
    with dissolve
    beth "Здравствуйте, Мистер!"
    show player 14
    show beth 1
    player_name "Привет."
    show player 1
    show beth 2
    beth "Разглядываешь, чтобы купить некоторые сладкие дыры?"
    show beth 1
    return

label beth_dialogue_do_not_know:
    show player 14
    player_name "Хм... Я не уверен, что мне нужно купить еще."
    show player 1
    show beth 2
    beth "Вы не знаете?"
    show player 14
    show beth 1
    player_name "Ну, я покупаю эти для кого-то в качестве подарка, но я не уверен, что он любит."
    show player 1
    show beth 2
    beth "Я не могу помочь, если вы не знаете, что нравится!"
    show player 14
    show beth 1
    player_name "Я вернусь позже, когда я узнаю начинку."
    return

label beth_dialogue_want_donuts:
    show player 14
    player_name "Я хотел бы купить маленькую коробку, пожалуйста."
    show player 1
    show beth 2
    beth "Хорошо!"
    beth "Какой глазури и Топпинг бы вы хотели нанести?"
    return

label beth_dialogue_leave:
    show player 14
    player_name "Я в порядке, спасибо!"
    player_name "Возможно, в другой раз..."
    show player 1
    show beth 2
    beth "Конечно, увидимся!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
