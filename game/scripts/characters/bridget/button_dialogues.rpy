label coach_bridget_dialogue_office_intro:
    scene expression game.timer.image("coach_office{}_b")
    show player 11 at left
    show coach 3 at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "Что ты здесь делаешь??"
    show player 32
    show coach 7
    player_name "Извините, Мэм!!!"
    player_name "Я только спросить!"
    show player 31
    show coach 3
    bri "Спросить?!"
    bri "Что именно?"
    show coach 7
    return

label coach_bridget_dialogue_courtyard_intro:
    scene expression game.timer.image("backgrounds/location_school_gym{}.jpg")
    show player 11 at left
    show coach 3 at right
    with dissolve
    bri "{b}[firstname]{/b}!"
    bri "Тебе лучше тренировать свою задницу в {b}Тренажерном зале{/b}, или я засуну ногу в твою задницу!!"
    show player 32
    show coach 7
    player_name "Да, мэм!!!"
    show player 31
    show coach 3
    bri "Есть вопросы?!"
    show coach 7
    return

label coach_bridget_dialogue_training_advice:
    show player 10
    show coach 1
    player_name "Я... Ну, где я должен тренироваться?"
    show coach 7
    show player 5
    bri "..."
    show player 22
    show coach 3
    bri "Я только что сказал тебе!"
    show coach 4
    bri "В {b}Тренажерном зале{/b}!!!"
    show player 10
    show coach 7
    player_name "Но... Что именно нужно тренировать?"
    show player 11
    show coach 3
    bri "Вы должны работать над вашей {b}прочностью{/b} и {b}ловкостью{/b}, если вы хотите сделать это!"
    bri "Вы будете участвовать в гонке {b}110m с препятствиями{/b}, чтобы квалифицировать эту {b}школу{/b} и вашу команду в {b}чемпионате штата{/b}!"
    show player 10
    show coach 7
    player_name "То есть... Много препятствий."
    show player 23
    show coach 3
    bri "...И тебе лучше не подводить меня!"
    show player 32
    show coach 7
    player_name "Да, мэм!!!"
    hide coach
    hide player
    with dissolve
    return

label coach_bridget_dialogue_leave:
    show player 10
    show coach 1
    player_name "И... Я забыл."
    show player 11
    show coach 3
    bri "Забыл? Ты самый грустный кусок мяса, что я когда-либо видела!"
    show player 22
    show coach 4
    bri "Теперь убирайся отсюда и возьмись за {b}РАБОТУ{/b}!!"
    show player 32
    show coach 7
    player_name "Да, мэм!!!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
