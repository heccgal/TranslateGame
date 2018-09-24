label button_dexter_talent_show:
    show dexter 1
    show player 10
    player_name "Эй, {b}Декстер{/b}, ты играешь на каких-нибудь инструментах?"
    show player 5
    show dexter 2
    dex "Что?"
    show player 12
    player_name "И-Н-С-Т-Р-У-М-Е-Н-Т-А-Х. Ты знаешь, это для музыки... Ты играешь на чём нибудь?"
    show player 5
    show dexter 8
    dex "Я похож на какого-то фаната группы?!"
    show dexter 2
    show player 12
    player_name "Эх, нет? Я просто подумал, Может у тебя есть скрытый талант стучать в барабаны или типа того?"
    show player 5
    show dexter 6 with dissolve
    dex "Я бы хотел постучать по твоему тупому лицу кулаками..."
    dex "Как ты думаешь, в этом будет какая-то музыка?"
    show dexter 5
    show player 29 with dissolve
    player_name "Хех, я как раз собирался уходить..."
    show player 3
    show dexter 4 with dissolve
    dex "Да, тебе лучше!"
    return

label button_dexter_challenge:
    show player 12
    player_name "Я здесь, чтобы бросить тебе вызов, {b}Декстер{/b}."
    show player 5
    show dexter 3
    dex "Ха-ха!"
    dex "К чему?!"
    show dexter 1
    show player 10
    player_name "В э..."
    show player 5
    show dexter 3
    dex "Ты же знаешь, я обхожу тебя в чем угодно."
    show dexter 4 with dissolve
    dex "А теперь отвали, пока я не решил выбить из тебя все дерьмо."
    return

label button_dexter_library_book:
    show player 10
    player_name "Хэй, эмм, {b}Декстер{/b}..."
    show player 5
    show dexter 3
    dex "Что тебе нужно, хамло?"
    show dexter 1
    show player 10
    player_name "Ты помнишь, где ты оставил библиотечную книгу, которую ты получил..."
    show player 5
    show dexter 8
    dex "Библиотечную книгу?"
    show dexter 4 with dissolve
    dex "Разве я не говорил тебе убираться отсюда, {b}[firstname]{/b}?"
    dex "Или ты хочешь отбивную!"
    show dexter 2 with dissolve
    show player 12
    player_name "Хорошо, хорошо, я ухожу!"
    hide dexter with dissolve
    show player 10f at center with dissolve
    player_name "Интересно, ошиблась ли библиотекарь?"
    show player 5f
    player_name "..."
    show player 12f
    player_name "Он может лгать. {b}Надо проверить его шкафчик{/b}!"
    player_name "Надеюсь, это там, иначе я не знаю, что я собираюсь сделать..."
    return

label button_dexter_nothing:
    show player 10
    player_name "Я... ухх... не хотел тебя беспокоить."
    player_name "Мне нужно попасть на занятия."
    show player 5
    show dexter 3
    dex "Беги, неудачник."
    return

label dexter_button_pushups:
    show player 16 at left
    show dexter 12 at right
    with dissolve
    dex "О, ты хочешь реванш, да?"
    dex "Без проблем, ботан!"
    dex "Я покажу тебе, как это делается!"
    show dexter 11
    scene gym
    show player 16 at left
    show dexter 11 at right
    with dissolve
    bri "Ладно, ребята. Вы знаете правила!"
    bri "Побеждает последний выживший!"
    show dexter 12
    dex "Хахаха, смотри и учись... БОТАНИК!"
    hide player
    hide dexter
    with dissolve
    bri "Начали!"
    return

label dexter_button_pushups_rematch:
    show player 5 at left
    show dexter 15 at right
    with dissolve
    dex "Как насчет реванша, ботаник?!"
    show dexter 14
    show player 12
    player_name "Что?! Да ладно, мужик... Ты проиграл."
    player_name "Просто двигайся дальше."
    show player 5
    show dexter 12 with dissolve
    dex "Ты боишься, что проиграешь?"
    show dexter 11
    show player 12
    player_name "Нет."
    show player 90
    show dexter 28 with dissolve
    dex "{b}[firstname]'s{/b} трус!"
    show dexter 11 with dissolve
    show player 12
    player_name "... Тч, хорошо."
    player_name "Давайте сделаем это!"
    hide player
    hide dexter
    with dissolve
    return

label button_dexter_intro_beginning:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "На что уставился, неудачник?!"
    show dexter 1
    show player 10
    player_name "Ничего."
    show player 5
    show dexter 3
    dex "Да, именно так!"
    dex "Продолжай идти сука!"
    dex "Хахахаха!"
    hide dexter with dissolve
    show player 12
    player_name "Ох, он такой засранец..."
    hide player with dissolve
    return

label button_dexter_intro:
    show player 5 at left
    show dexter 3 at right
    with dissolve
    dex "Я думал, что почувствовал запах маленькой сучки!"
    show dexter 2
    show player 12
    player_name "Пошел ты, {b}Декстер{/b}..."
    show player 90
    show dexter 6 with dissolve
    dex "ЧТО ТЫ СКАЗАЛ?!"
    show dexter 4 with dissolve
    show player 11
    dex "Ты хочешь, чтобы я надрал тебе задницу, прямо здесь?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "Да, это то, что я подумал."
    show dexter 6 with dissolve
    dex "Тебе лучше держаться подальше от моей девушки!"
    show dexter 2 with dissolve
    show player 5
    player_name "..."
    show dexter 4 with dissolve
    dex "Ты слышишь меня, сука?!"
    show dexter 2 with dissolve
    return

label button_dexter_intro_final:
    show player 90 at left
    show dexter 2 at right
    with dissolve
    dex "..."
    show player 12
    player_name "Прости, ты что-то сказал, {b}Декстер{/b}?"
    show player 91
    show dexter 8
    dex "Нет!"
    show dexter 2
    show player 12
    player_name "Да, это то, что я подумал."
    show player 91

    dex "..."
    return

label button_dexter_basketball_final:
    show player 12
    player_name "Все еще играешь в баскетбол?"
    show player 91
    dex "..."
    show player 12
    player_name "Ребята, вам удалось выиграть игру?"
    show player 91
    show dexter 8
    dex "Я не хочу об этом говорить!"
    show dexter 2
    show player 12
    player_name "Я просто пытаюсь-"
    show player 11
    show dexter 8
    dex "Оставь меня в покое, {b}[firstname]{/b}!"
    hide dexter with dissolve
    pause
    show player 10
    player_name "Хорошо."
    hide player with dissolve
    return

label button_dexter_basketball:
    show player 12
    player_name "Все еще играет в баскетбол?"
    show player 90
    show dexter 3
    dex "Конечно, я был рожден, чтобы играть!"
    show dexter 1
    show player 12
    player_name "Вы даже выиграли игру еще?"
    show player 90
    show dexter 3
    dex "Ну Да. Как сто миллионов..."
    show dexter 1
    show player 12
    player_name "Да, точно! Вы просто ужасны..."
    show player 90
    show dexter 4 with dissolve
    dex "Эй! Хочешь бутерброд с костяшками, неудачник?!"
    show dexter 2 with dissolve
    player_name "..."
    show dexter 3
    dex "Что такое маленькая сука, так ты знаешь о баскетболе?!"
    dex "Это мужской вид спорта!"
    show dexter 1
    show player 17
    player_name "О, ну тогда неудивительно, почему вы дамы не можете выиграть игру."
    show player 13
    show dexter 3
    dex "Что? Я не-"
    dex "О, ты думаешь это смешно?!"
    show dexter 8
    dex "Как насчет того, чтобы выбить тебе зубы?!"
    show player 5
    dex "Это было бы довольно забавно, не так ли?!"
    show dexter 2
    return

label button_dexter_whatever:
    show player 12
    player_name "Тч, Да. Неважно, чувак..."
    hide player with dissolve
    pause
    show dexter 8
    dex "Эй, я не шучу {b}[firstname]{/b}!"
    dex "Держись подальше от, {b}Рокси{/b}!"
    dex "Она моя!"
    hide dexter
    hide player
    with dissolve
    return

label button_dexter_behaving:
    show player 12
    player_name "Я верю, что ты себя ведешь."
    show player 90
    show dexter 8
    dex "... Да."
    show dexter 2
    show player 12
    player_name "Ты ведь помнишь, что случится, если я снова увижу, как ты играешь с моими друзьями, верно?"
    show player 92
    player_name "Вам нужно напоминание?!"
    show player 91
    show dexter 8
    dex "НЕТ!"
    dex "Я помню..."
    show dexter 2
    show player 92
    player_name "Хорошо."
    show player 91
    return

label button_dexter_run_along:
    show player 12
    player_name "Беги сейчас же, {b}Декстер{/b}."
    show player 91
    dex "..."
    show dexter 8
    dex "ГРРРР!!!"
    hide dexter with dissolve
    pause
    show player 17
    player_name "Хахаха!"
    player_name "Мне нравится ноый {b}Декстер{/b}!"
    hide player with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
