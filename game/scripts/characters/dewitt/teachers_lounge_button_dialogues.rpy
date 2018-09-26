label dewitt_dialogue_lounge_intro:
    scene location_school_lounge_couch
    show player 10 at left
    show dewittl 5 at right
    with dissolve
    pause
    show dewittl 1 with dissolve
    player_name "О, привет, {b}Мисс Девитт{/b}."
    show player 11
    show dewittl 3 with dissolve
    dewitt "{b}[firstname]{/b}? Тебе нельзя здесь находиться..."
    show player 10
    show dewittl 2
    player_name "Да, простите."
    show player 2
    player_name "{b}Мисс Росс{/b} заставляет меня искать старые журналы."
    player_name "Мы делаем коллаж!"
    show player 1
    show dewittl 3
    dewitt "Коллаж, да?"
    dewitt "Я делала их все время, когда была моложе!"
    show player 2
    show dewittl 2
    player_name "Что вы там перекусывайте?"
    show player 1
    show dewittl 3b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "О, это?"
    show dewittl 3 at right with dissolve
    dewitt "Это один из {b}особенных пирожных Барбары{/b}."
    show player 2
    show dewittl 2
    player_name "Я не знал, что {b}Мисс Росс{/b} умеет печь?"
    show player 1
    show dewittl 3
    dewitt "Она делает ЛУЧШИЕ пирожные!"
    dewitt "Я просто не могу насытиться!"
    show player 2
    show dewittl 2
    player_name "... Аккуратно!"
    player_name "Как думаешь, можно мне взять несколько таких журналов на столе?"
    show player 1
    show dewittl 3
    dewitt "Не понимаю, почему бы и нет."
    show player 2
    show dewittl 2
    player_name "Страх-"
    show player 11
    show dewittl 6 with dissolve
    dewitt "Если вы можете ответить на вопрос от моего следующего теста!"
    show player 10
    show dewittl 2 with dissolve
    player_name "Серьёзно?"
    show player 11
    show dewittl 3
    dewitt "В жизни нет ничего бесплатного, {b}[firstname]{/b}."
    dewitt "Теперь давайте посмотрим..."
    dewitt "Флейта - член какой инструментальной семьи?"
    return

label dewitt_dialogue_lounge_stat_pass:
    show player 2 at left
    show dewittl 2 at right
    player_name "Это просто! Духовой."
    show player 1
    show dewittl 3
    dewitt "Отлично, {b}[firstname]{/b}!"
    dewitt "Наверное, ты все-таки уделял внимание обучению."
    show dewittl 4 with dissolve
    dewitt "Иди вперед и возьми столько журналов, сколько тебе нужно."
    show player 595 with dissolve
    show dewittl 2
    player_name "Отлично!"

    player_name "Спасибо, {b}Мисс Девитт{/b}! Насладитесь вашим пирожным!"
    show player 594
    show dewittl 1b at Position(xpos=0.965, ypos=1.0) with dissolve
    dewitt "Охм, так хорошо! Ммм..."
    return

label dewitt_dialogue_lounge_stat_fail:
    show player 10
    show dewittl 2
    player_name "[int_warn]Ошибка... У приборов есть семьи?"
    show player 11
    show dewittl 3
    dewitt "[int_warn]Хе-хе, ну это то, что вам лучше понять, если вы хотите эти журналы."
    dewitt "[int_warn]Вернись, когда узнаешь ответ."
    show dewittl 2
    show player 10
    player_name "[int_warn]Ах, хорошо..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
