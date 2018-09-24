label debbie_dialogue_master_room_pre:
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with dissolve
    deb "Привет, дорогой..."
    deb "ты меня искал?"
    show debbie 54
    show player 111
    player_name "Да..."
    show player 110
    show debbie 55
    deb "Ты что-то хотел от меня?"
    show debbie 54
    return

label debbie_dialogue_master_room_after_kiss_dialogue:
    deb "Теперь, что бы ты ещё хотел?"
    show debbie 54
    return

label debbie_dialogue_master_room_kiss:
    show player 111 at right
    show debbie 54 at left
    player_name "Можно тебя поцеловать?"
    show player 110
    show debbie 55
    deb "Конечно, дорогой! Подойди сюда."
    scene debbie_bedroom
    show debbie 79
    with fade
    deb "Мммм..."
    show debbie 80_79
    pause 3
    show debbie 75 at Position(xpos=750)
    show player 227 at Position(xpos=200)
    with fastdissolve
    deb "Ты становишься лучше!"
    scene debbie_bedroom_closeup2
    show debbie 55 at left
    show player 110 at right
    with fade
    return

label debbie_dialogue_master_room_shower:
    show player 111
    player_name "Хэй, {b}[deb_name]{/b}!"
    player_name "Хочешь принять со мной душ?"
    show player 110
    show debbie 55
    deb "В доме становится довольно жарко..."
    deb "Конечно! Душ прямо сейчас звучит прекрасно."
    deb "Иди вперед, милый. Я буду через минуту."
    scene shower_closeup
    show debbies 27
    with dissolve
    pause
    show debbies 28 at Position(xpos=487,ypos=768) with dissolve
    pause
    show debbies 34 with dissolve
    deb "Извини, что заставила ждать..."
    return

label debbie_dialogue_master_room_sex_random_true:
    show debbie 54 at left
    show player 111 at right
    player_name "Мне нравится... Быть с тобой."
    show player 110
    show debbie 55
    deb "Все хорошо!"
    deb "Я надеялся, что ты захочешь..."
    show player 111
    show debbie 54
    player_name "Правда?"
    show player 110
    show debbie 58 with dissolve
    deb "Конечно! Ты мой мужчина, в конце концов."
    show debbie 57
    player_name "!!!"
    show debbie 58
    deb "Снимай свою одежду, сладенький."
    show debbie 57
    show player 8f
    pause
    show player 261
    pause
    show player 263
    pause
    show debbie 103
    deb "Ммм, возьми меня, милый!"
    show player 262 at right
    show debbie 102 at left
    player_name "Не нужно повторять дважды..."
    return

label debbie_dialogue_master_room_sex_random_false:
    show debbie 54 at left
    show player 111 at right
    player_name "{b}[deb_name]{/b}, хочешь повеселиться?"
    show player 110
    show debbie 54
    deb "Ох?"
    show debbie 56 with dissolve
    deb "Как... это любопытное развлечение?"
    show debbie 57
    show player 111
    player_name "Конечно..."
    show player 110
    show debbie 58
    deb "Позволь мне увидеть, твой член..."
    show debbie 57
    show player 8f with dissolve
    pause
    show debbie 101
    show player 261 with dissolve
    pause
    show player 263 with dissolve
    pause
    show debbie 58
    deb "Похоже, что ты готов!"
    show debbie 57
    show player 262
    player_name "Я ждал этого с тех пор, как проснулся сегодня утром."
    show player 263
    show debbie 58
    deb "Я тоже."
    show debbie 102 with dissolve
    pause
    show debbie 103
    deb "Подойди и возьми меня, дорогой."
    return

label debbie_dialogue_master_room_sex_after:
    hide player
    show debbie 104 at left
    with dissolve
    pause
    hide debbie
    hide player
    with dissolve
    scene debbie_bedroom_closeup_sex
    return

label debbie_dialogue_master_room_laundry_sex:
    show debbie 54
    show player 111
    player_name "Мне было интересно, не нужна ли тебе помощь в подвале."
    show player 110
    show debbie 55
    deb "В подвале? Зачем?"
    show player 111
    show debbie 54
    player_name "Может быть, я могу помочь тебе со стиркой... Как в прошлый раз?"
    show player 110
    show debbie 55
    deb "А, понятно... Я точно знаю, чего ты хочешь!"
    deb "Дай мне минутку подготовиться."
    deb "Увидимся там..."
    hide debbie
    hide player
    with dissolve
    return

label debbie_dialogue_master_room_watch_movie:
    show player 111
    player_name "Я подумал, что нам стоит посмотреть другой фильм Сегодня вечером. Заинтересована?"
    show player 110
    show debbie 55
    deb "Мм, вечернее кино, да?"
    deb "Звучит как отличная идея, милый!"
    show player 111
    show debbie 54
    player_name "Потрясающе!"
    player_name "Увидимся вечером в гостиной?"
    show player 110
    show debbie 55
    deb "Не могу дождаться..."
    return

label debbie_dialogue_master_room_leave:
    show debbie 54
    show player 111
    player_name "Ничего, {b}[deb_name]{/b}."
    player_name "Просто хотел поздороваться."
    show player 110
    show debbie 55
    deb "О, хорошо..."
    deb "Возвращайся, если хочешь... Мне немного скучно..."
    deb "Мы можем повеселиться, когда захочешь."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
