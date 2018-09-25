label erik_dialogue_intro:
    scene location_school_computer_day_blur
    show player 2 at left
    show erik 1 at right
    with dissolve
    return

label erik_dialogue_okita_get_bifocal_lenses:
    show player 2
    player_name "Я помогаю Оките с проектом."
    show player 1
    show erik 4
    eri "Правда? Потрясающе!"
    eri "Что это за проект такой?"
    show player 2
    show erik 1
    player_name "Не думаю, что мне следует говорить об этом..."
    show player 1
    show erik 4
    eri "О, сверхсекретное исследование?"
    eri "Здорово, тебе помочь?"
    show player 2
    show erik 1
    player_name "Вообще-То Да!"
    player_name "Мне нужно найти пару {b}толстых линз{/b}."
    player_name "У тебя случайно нет запасного комплекта очков?"
    show player 1
    show erik 4
    eri "Ты шутишь?"
    eri "Знаешь, сколько раз {b}Декстер{/b} разбивал мне очки ?"
    eri "Я всегда держу запасной комплект близко."
    show player 2
    show erik 1
    player_name "Привосходно!!"
    player_name "Ты позволишь мне забрать их?"
    show player 1
    show erik 4
    eri "Конечно!"
    show player 2
    show erik 1
    player_name "Спасибо, чувак!"
    show player 1
    show erik 4
    eri "Не проблема, {b}[firstname]{/b}! Для чего еще нужны друзья?"
    show player 10
    show erik 1
    player_name "... О, подожди!"
    show player 29 with dissolve
    player_name "Я забыл, они должны быть {b}Варифокальными линзами{/b}..."
    show player 3
    show erik 5
    eri "Вари-Что?"
    show player 10 with dissolve
    show erik 1
    player_name "Ты дальнозоркий или близорукий?"
    show player 11
    show erik 5
    eri "Близорукий. А зачем?"
    show player 10
    show erik 1
    player_name "Дерьмо! Мне нужны линзы от того, кто является одновременно."
    show player 11
    show erik 5
    eri "Ох."
    show player 24
    show erik 1
    player_name "*Вздох*"
    show player 10
    player_name "Думаю, мне придется продолжать поиски."
    show player 11
    show erik 5
    eri "Прости, {b}[firstname]{/b}."
    show player 2
    show erik 1
    player_name "Всё нормально, {b}Эрик{/b}. Спасибо в любом случае."
    show player 1
    show erik 4
    eri "В Любое Время, Чувак."
    return

label erik_dialogue_leave:
    show player 14
    player_name "Да ничего!"
    player_name "Просто поздоровался."
    show player 1
    show erik 4
    june "О, хорошо..."
    show erik 1
    show player 29 at Position(xoffset=8)
    player_name "Эмм... Увидимся позже!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
