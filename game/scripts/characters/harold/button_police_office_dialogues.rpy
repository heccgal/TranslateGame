label harold_police_office_dialogue_mia_route:
    show harold 1 at right
    show player 14 at left
    with dissolve
    player_name "Привет, {b}Гарольд{/b}!"
    show player 13
    show harold 2
    harold "А вот и мой человек!"
    show harold 1
    show player 14
    player_name "Как дела идут в последнее время?"
    show player 13
    show harold 2
    harold "Лучше не бывало! Наша семья - самое счастливое, что когда-либо было!"
    harold "{b}Хелен{/b} действительно изменилась. Действительно... изменилась."
    harold "Разные горячие вещи в посте-"
    show harold 4
    harold "В любом случае, ты знаешь, что я имею в виду."
    show harold 1
    show player 21
    player_name "Хе-хе... Да, я полагаю..."
    show player 13
    show harold 2
    harold "Я должен вернуться к работе."
    harold "Не стесняйся заходить в дом в любое время, малыш!"
    show harold 1
    show player 14
    player_name "Спасибо, {b}Гарольд{/b}!"
    player_name "Увидимся."
    return

label harold_police_office_dialogue_helen_route_split:
    show player 22f at right
    show harold 51 at left
    with dissolve
    pause
    show harold 52
    show yum 12f at Position (xpos=395)
    with dissolve
    yum "!!!"
    show player 5f
    yum "О! Я не видела тебя там..."
    show yum 14f at Position (xpos=382) with dissolve
    show harold 53
    harold "Не волнуйся, {b}Юми{/b}, это просто маленький приятель моей дочери."
    show harold 52
    show player 10f
    player_name "Привет..."
    show player 5f
    show yum 13f
    yum "Привет... О! Я забыла, что у меня есть кое-что... нужно позаботиться о моем офисе."
    hide yum
    show harold 54
    with dissolve
    harold "..."
    show harold 55
    harold "Прости, что тебе пришлось это увидеть, малыш."
    harold "{b}Юми{/b} больше рук для партнера..."
    harold "Решил попробовать научить ее паре вещей..."
    show harold 54
    show player 11f
    player_name "..."
    show player 10f
    player_name "Итак, ты и {b}Хелен{/b}..."
    show player 5f
    show harold 55
    harold "Смотри. Этот корабль уплыл, малыш. {b}Хелен{/b}, кажется, приняла наше расставание."
    harold "Я подумал, что мне тоже лучше двигаться дальше."
    harold "Чтобы сказать тебе правду."
    harold "Я никогда не была счастливее, и я начал встречаться с кем-то другим."
    show harold 54
    show player 12f
    player_name "Интересно, кто..."
    show player 10f
    player_name "По крайней мере, ты счастлив..."
    show player 5f
    pause
    show player 10f
    player_name "Но как {b}Мия{/b} справляется с этим? С ней все будет в порядке?"
    show player 5f
    show harold 55
    harold "Я не откажусь от {b}Мии{/b}."
    harold "Я навещаю ее каждый день. Она моя сильная маленькая девочка."
    harold "Ей всегда приходилось мириться с {b} Хелен{/b} и со мной."
    harold "С ней все будет в порядке."
    show harold 54
    show player 12f
    player_name "Отлично."
    show player 5f
    show harold 55
    harold "Ты хороший парень, {b}[firstname]{/b}. Еще раз спасибо за заботу о моей дочери."
    harold "Я ценю, что вы с ней пытаетесь вернуть меня к {b}Хелен{/b}..."
    harold "Просто, некоторые вещи просто так не работают..."
    show harold 54
    show player 21f
    player_name "Хе хе..."
    player_name "Добро пожаловать."
    show player 5f
    show harold 55
    harold "Не бойся навещать меня, если тебе понадобится помощь."
    show harold 54
    show player 36f with dissolve
    player_name "Ну так, пока, {b}Гарольд{/b}."
    return

label harold_police_office_dialogue_mia_harold_backup:
    show harold 1 at Position (xpos=762)
    show player 23 at left
    with dissolve
    player_name "{b}Гарольд{/b}!!"
    show player 22
    show harold 6
    harold "Что происходит?? Ты нашёл {b}Юми{/b}?"
    show harold 1
    show player 38 with dissolve
    player_name "Да! Но она нуждается в вашей помощи, сейчас!!"
    show player 3 with dissolve
    show harold 3
    harold "Что?!"
    show harold 1
    show player 10 with dissolve
    player_name "В камеру! {b}Юми{/b}... Она борется с заключенным!!"
    show player 5
    show harold 29
    harold "!!!"
    show harold 30 at right with dissolve
    harold "Я... Я должен вызвать подкрепление. Может быть, сначала я должен сказать {b}Ярлу{/b}?"
    show player 12
    player_name "{b}Гарольд{/b}! Нет времени!"
    hide harold
    show harold 25 at Position (xpos=762)
    with dissolve
    player_name "Ты должен взять ситуацию под контроль."
    show player 11
    show harold 26
    harold "Но сначала я должен сказать {b}Ярлу{/b} ..."
    harold "...Я давно не имел дела с заключенными и-"
    show harold 25
    show player 15
    player_name "{b}Юми{/b} - ваш партнер и нуждается в вашей помощи!"
    player_name "Ты должен идти! СЕЙЧАС!!!"
    show player 16
    show harold 24
    harold "..."
    show harold 6
    harold "Ты прав. Я должен принять меры."
    harold "Пойдем."
    return

label harold_police_office_dialogue_mia_harolds_thoughts:
    show harold 1 at right
    show player 36 at left
    with dissolve
    player_name "Привет, {b}Гарольд{/b}."
    show player 13 with dissolve
    show harold 2
    harold "И снова здравствуй, малыш."
    show harold 1
    show player 14
    player_name "Решил заглянуть и узнать, как прошел ужин с {b}Мия{/b} и {b}Хелен{/b}."
    show player 13
    show harold 6
    harold "О... Ммм... Это было хорошо, я думаю. Еда была действительно хорошей."
    show harold 1
    show player 10
    player_name "Как ты думаешь, что-то есть... становилось лучше между Хелен... И тобой?"
    show player 5
    show harold 4
    harold "..."
    show harold 6
    harold "Я знаю, {b}Миа{/b} пытается получить {b}Хелен{/ b} и меня, снова вместе."
    harold "Ты ей тоже помогаешь. Ты хороший парень."
    show harold 1
    harold "..."
    show harold 6
    harold "Я полагаю, что вещи между {b}Хелен{/b} и мной лучше, чем когда вы видели, как мы извергались друг на друга."
    show harold 4
    pause
    harold "И... я просто не знаю..."
    show harold 1
    pause
    show player 10
    player_name "Почему ты ничего не знаешь?"
    show player 5
    show harold 26
    harold "О, малыш."
    harold "Теперь мы можем быть в хороших отношениях, но мы снова можем перехватить друг друга."
    harold "На этот раз я думаю, что могу быть счастливее сам по себе."
    harold "Мой брак лучше оставить позади."
    harold "Возможно... если {b}Хелен{/b} действительно изменилась к лучшему."
    harold "Возможно, нам удастся снова быть вместе."
    show harold 1
    show player 14
    player_name "Я... Я понимаю."
    show player 13
    show harold 6
    harold "Мне лучше вернуться к работе. У меня только что был очередной прорыв в деле."
    show harold 2
    harold "Увидимся, {b}[firstname]{/b}."
    show harold 1
    show player 14
    player_name "Пока, {b}Гарольд{/b}."
    show player 13
    hide harold with dissolve
    pause
    show player 14
    player_name "( Звучит так, будто {b}Гарольд{/b} говорит мне, что есть шанс, что он вернется с {b}Хелен{/b}. )"
    show player 35
    player_name "( Возможно обучение {b}Сестры Анжелики{/b} на самом деле помогает ей и {b}Гарольду{/b}. )"
    show player 10
    player_name "( Но... он сейчас выглядит счастливым без {b}Хелен{/b}... )"
    player_name "( {b}Мия{/b} будет опустошена, если он не вернется к {b}Хелен{/b}. )"
    show player 5
    player_name "..."
    show player 12
    player_name "( Думаю, на данный момент это не зависит от меня... )"
    player_name "( Возможно также помочь {b}Сестре Анжелике{/b}. )"
    show player 35
    player_name "( Ещё раз, чего она хотела? )"
    hide player with dissolve
    return

label harold_police_office_dialogue_roxxy_ask_earl_release:
    scene police_c_2
    show harold 1 at right
    show roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Эй, эмм..."
    player_name "{b}Мать моей подруги{/b} сегодня была взята под стражу, и нам нужно выяснить, что происходит."
    show player 5
    show harold 2
    harold "Хмм?"
    show harold 2
    harold "О, ты должно быть дочь {b}Кристи{/b}!"
    show harold 1
    show roxxy 33f
    rox "... Да."
    show roxxy 32f
    show harold 2
    harold "Послушай, ты её копия по младше!"
    show harold 1
    rox "..."
    show player 10
    player_name "Не могли бы вы рассказать нам, почему вы держите её?"
    show player 5
    show harold 2
    harold "Извините, детки."
    harold "Ребенок с наркотиками, этот большой, намного выше моего уровня оплаты."
    harold "Вам придется поговорить с шефом, если хотите подробностей."
    show harold 1
    show player 10
    player_name "... Ох."
    player_name "Хорошо, спасибо."
    show player 5
    hide harold with dissolve
    pause
    show roxxy 2c at center
    show roxxy 2c at Position (xoffset=-33)
    with dissolve
    rox "О, Боже... Должно быть, они нашли тайник {b}Клайда{/b} целиком!"
    show roxxy 2b at Position (xoffset=-33)
    show player 12
    player_name "Сколько мета у твоего кузена вообще?!"
    show player 5
    show roxxy 1j with dissolve
    rox "..."
    show roxxy 1l
    rox "Я... эмм..."
    rox "... Я не уверена."
    show roxxy 1j
    show player 12
    player_name "Ну, думаю, нам лучше поговорить с {b}шефом{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label harold_police_office_dialogue_pre:
    show player 1 at left
    show harold 2 at right
    with dissolve
    harold "Привет, это снова ты. Что-то нужно?"
    show harold 1
    show player 14
    player_name "Привет, у меня есть несколько вопросов."
    show player 1
    return

label harold_police_office_dialogue_wheres_mia:
    show player 14
    player_name "Мне просто интересно, ты знаешь, где сейчас {b}Мия{/b}?"
    show player 11
    show harold 2
    harold "Прости, ничем не могу помочь, у нас новое дело...."
    harold "Но, она должна быть в школе или дома."
    show harold 1
    show player 14
    player_name "Окей. Спасибо, Сэр!"
    return

label harold_police_office_dialogue_the_chief:
    show player 12
    player_name "Кто такой {b}шеф?{/b}?"
    show player 5
    show harold 2
    harold "Ох, тебе нужен {b}Ярл{/b}."
    show player 13
    harold "Он прямо там, на другой стороне офиса."
    show harold 1
    show player 14
    player_name "Хорошо, спасибо!"
    return

label harold_police_office_dialogue_larry:
    show player 10
    player_name "Что тебе нужно, чтобы я узнал о {b}Ларри{/b}?"
    show player 5
    show harold 6
    harold "{b}Ларри{/b} не раскрывает местонахождение товара."
    show harold 1
    show player 33
    player_name "О, да!"
    show player 12
    player_name "Я буду с ним разговаривать. Я знаю его жену."
    player_name "Если я не смогу узнать его местоположение, может, я смогу попросить {b}Миссис Джонсон{/b} помочь нам."
    show player 5
    show harold 2
    harold "Спасибо, {b}[firstname]{/b}."
    return

label harold_police_office_dialogue_thief:
    show player 10
    player_name "Что мне нужно сделать, если я снова увижу вора?"
    show player 5
    show harold 6
    harold "Если заметишь его, позвони мне напрямую."
    show harold 1
    show player 12
    player_name "Ну конечно! Я буду присматривать за ним."
    player_name "Он всегда пробирается ночью во двор моей соседки, {b}Миссис Джонсон{/b}."
    show player 5
    show harold 6
    harold "Также были сообщения о нем рядом с парком. Если вы заметите его там, держите меня в курсе."
    show harold 1
    show player 12
    player_name "Хорошо, я проверю и там."
    show player 5
    show harold 2
    harold "Спасибо, {b}[firstname]{/b}."
    return

label harold_police_office_dialogue_donuts:
    show player 14
    player_name "Какие ... пончики, эмм... тебе нравится?"
    show player 11
    show harold 3
    harold "Простите?"
    show player 14
    show harold 1
    player_name "Просто интересно!"
    show player 11
    show harold 2
    harold "Слушай, у меня сейчас нет времени болтать, я завален работой..."
    harold "... Почему бы тебе не сбегать в школу, ладно?"
    show player 10
    show harold 1
    player_name "Но-"
    show player 5
    show harold 2
    harold "Мне нужно идти, прости."
    return

label harold_police_office_dialogue_donuts_wrong:
    show player 437 at left with fastdissolve
    player_name "У меня есть кое-что для тебя."
    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "Это для тебя!"
    show harold 8
    show player 1
    with fastdissolve
    harold "Ты принес мне коробку... пончики?!"
    show player 14
    show harold 7
    player_name "Да! Я подумала, Может ты захочешь перекусить ими на работе..."
    show player 1
    show harold 9
    harold "Ох..."
    harold "Честно говоря, я не большой поклонник такого рода."
    show player 11
    show harold 10
    player_name "..."
    show harold 11
    harold "Но я... Я ценю эту мысль!"
    harold "Я уверен, что {b}Ярл{/b} будет более чем счастлив иметь их..."
    show player 10
    show harold 10
    player_name "Хорошо."

    show player 5
    hide harold with dissolve
    pause
    show player 10
    player_name "( Черт! )"
    player_name "( Наверное, я купил не тот сорт. )"
    player_name "( Я должен убедиться, что получу нужные ингредиенты... )"
    return

label harold_police_office_dialogue_donuts_correct:
    show player 437 at left with fastdissolve
    player_name "У меня есть кое-что для тебя."
    show player 1
    show player 436
    harold "..."
    show player 437
    player_name "Это для тебя!"
    show harold 8
    show player 1
    with fastdissolve
    harold "Ты принес мне коробку... пончики?!"
    show player 14
    show harold 7
    player_name "Да! Я подумала, Может ты захочешь перекусить ими на работе..."
    show player 1
    show harold 9
    harold "Позвольте мне посмотреть..."
    harold "Святой... [harold_glaze]... с... [harold_topping]?!"
    show player 14
    show harold 7
    player_name "Я думал, тебе понравится!"
    show player 1
    show harold 8
    harold "Это мои любимые... Как ты..."
    show player 17
    show harold 44
    player_name "Мне повезло, я полагаю."
    show player 1
    show harold 45
    harold "*Омном мном*"
    show harold 46
    harold "Ну, парень, ты хорошо справился."
    show player 17
    show harold 45
    player_name "Рад, что они вам понравились!"
    show player 1
    harold "..."
    show player 11
    show harold 46
    harold "Подожди, пока ты не ушел..."
    show player 1
    harold "Я знаю, что тебе и {b}Мие{/b} это нравится... тусоваться и все такое."
    harold "Ты кажешься хорошим ребенком, так что я поговорю со своей женой и посмотрю, сможет ли она немного отвлечься."
    show player 14
    show harold 45
    player_name "То есть, я могу навестить ее сейчас?"
    show player 1
    show harold 46
    harold "Не так быстро!"
    harold "Я этого не говорил... но... Ты мог бы прокрасться, как раньше, а я постараюсь отвлечь жену, хорошо?"
    show player 14
    show harold 45
    player_name "Серьёзно?"
    show player 1
    show harold 46
    harold "Я сказал, что постараюсь, ничего не могу обещать."
    show player 14
    show harold 45
    player_name "Спасибо, {b}Гарольд{/b}."
    show player 1
    show harold 46
    harold "А теперь убирайся отсюда, пока мой босс не увидел нас с этими пончиками!"
    show player 17
    show harold 45
    player_name "Ха-ха."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
