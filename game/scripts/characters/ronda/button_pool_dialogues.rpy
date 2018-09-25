label ronda_pool_dialogue_pre_cassie_fun:
    show ronda 5 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "..."
    show ronda 6
    ron "Что ты вообще здесь делаешь?"
    show ronda 5
    if wearing_swimsuit:
        show player 50f
    else:
        show player 17
    player_name "Просто занимаюсь спортом!"
    player_name "Я решил, что должен где-то начать, и это может помочь мне подготовиться к отборочным!"
    show ronda 6
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Слушай, я не помогаю тебе, не говоря уже о том, чтобы идти в воду одновременно с тобой... Так что забудь об этом, ладно?"
    show ronda 5
    if wearing_swimsuit:
        show player 53
    else:
        show player 26
    player_name "Это нормально!"
    player_name "Я справлюсь..."
    show ronda 7
    if wearing_swimsuit:
        show player 51
    else:
        show player 11
    ron "Тьфу... чёрт с ним."
    return

label ronda_pool_dialogue_after_cassie_fun:
    show ronda 8 at right
    if wearing_swimsuit:
        show player 53f at left
    else:
        show player 1 at left
    with dissolve
    ron "Пришёл навестить Кэсси?"
    show ronda 10
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Ох... Я здесь, чтобы просто поплавать?"
    show ronda 8
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Ты можешь перестать притворяться..."
    ron "...Ты здесь не для того, чтобы тренироваться, как я."
    show ronda 8
    if wearing_swimsuit:
        show player 51f
    else:
        show player 12
    player_name "Ох... ладно?"
    show ronda 9
    if wearing_swimsuit:
        show player 51f
    else:
        show player 11
    ron "Тьфу... ты просто жалок."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
