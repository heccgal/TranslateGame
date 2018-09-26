label button_eve_intro:
    scene expression game.timer.image("backgrounds/location_school_right_hall{}_blur.jpg")
    show player 13 at left
    show eve 1 at right
    with dissolve
    return

label button_eve_talent_show_help:
    show player 10
    player_name "Ты играешь на каких-нибудь инструментах?"
    show player 5
    show eve 2
    eve "Нет, я не играю. Я всегда хотела научиться, но у меня просто не было времени, понимаешь?"
    show eve 1
    show player 10
    player_name "Хорошо, а как насчет пения?"
    show player 5
    show eve 6
    eve "Ох, эмм..."
    show eve 2b
    eve "Да, мне нравится петь, наверное. Не знаю, насколько я хороша."
    show eve 1
    show player 14
    player_name "Бьюсь об заклад! Ты должна подписаться на шоу талантов со мной!"
    player_name "Нам действительно не хватает добровольцев."
    show player 13
    show eve 2b
    eve "... Да, я не знаю."
    eve "Ты хочешь, чтобы я пела перед всей школой? Звучит довольно неловко."
    eve "... И я не пела некоторое время. С тех пор, как сломалась моя караоке-машина."
    eve "У меня совсем нет практики."
    show eve 1
    show player 4 with dissolve
    player_name "Хмм..."
    show player 14 with dissolve
    player_name "Ты знаешь, я думаю, что мой друг {b}Эрик{/b} имеет {b}караоке{/b} в своем подвале."
    show player 13
    show eve 2
    eve "О, правда?"
    show eve 1
    show player 17
    player_name "Точно! Приходи как-нибудь и потренируйся!"
    show player 13
    show eve 6
    eve "Ты хочешь, чтобы я спела для тебя и твоего друга?"
    show eve 5
    show player 14
    player_name "Нет, мы можем петь все вместе! Давай, сделаем это сегодня вечером, будет весело!"
    show player 13
    show eve 1
    eve "..."
    show eve 6b
    eve "Ладно, думаю, я могу заехать ненадолго."
    show eve 5
    show player 14
    player_name "Потрясающе! {b}Я буду ждать тебя в доме Эрика {/b} сегодня вечером."
    return

label button_eve_ross_find_art_pad:
    show player 2
    player_name "Мне нужно попросить тебя об одолжении."
    show player 1
    show eve 2
    eve "Ох?"
    show player 2
    show eve 1
    player_name "Видишь ли, я вроде как помогаю {b}Мисс Росс{/b} кое с чем, и нам нужен твой блокнот."
    show player 1
    show eve 2
    eve "Ну, это не проблема."
    eve "Сначала ты должен помочь мне найти {b}мой рюкзак{/b}."
    show player 10
    show eve 1
    player_name "Ты потеряла свой рюкзак?"
    show player 11
    show eve 2
    eve "Да..."
    eve "Мой блокнот должен быть внутри."
    show player 10
    show eve 1
    player_name "Где было последнее место, где ты его помнишь?"
    show player 11
    show eve 2
    eve "Хм, Ну, я думаю, что {b}у меня он было, когда я пошла тусоваться с парнями в парке прошлой ночью{/b}."
    show player 2
    show eve 1
    player_name "Хорошо, я займусь этим делом!"
    return

label button_eve_ross_find_eve_backpack_have_backpack:
    show player 610
    player_name "Посмотрите, что я нашел!"
    show player 609
    show eve 2
    eve "Класс!"
    show player 1 with dissolve
    eve "Спасибо, {b}[firstname]{/b}!"
    show player 2
    show eve 1
    player_name "Не беспокоиться. Я не смог найти {b}твой блокнот{/b} для рисования."
    show player 1
    show eve 2
    eve "Его не было в моей сумке?"
    show player 2
    show eve 1
    player_name "Нет."
    show player 1
    show eve 2
    eve "Таинственность."
    show eve 6b
    eve "Интересно, что если {b}Чад{/b} опять утащил?"
    show player 10
    show eve 1
    player_name "Чад?"
    show player 11
    show eve 2
    eve "Да, ему нравится мое искусство."
    show player 10
    show eve 1
    player_name "Интересно..."
    show player 2
    player_name "Пойду, спрошу у него."
    show player 1
    show eve 2
    eve "Класс. Увидимся, {b}[firstname]{/b}."
    show player 2
    show eve 1
    player_name "Увидимся, {b}Ева{/b}."
    return

label button_eve_ross_find_eve_backpack_no_backpack:
    show player 2
    player_name "Еще раз, Где ты оставила свой рюкзак?"
    show player 1
    show eve 2
    eve "Я не совсем уверена. Я помню, как он был со мной в {b}парке прошлой ночью{/b}."
    show player 2
    show eve 1
    player_name "Хорошо, я там все проверю!"
    return

label button_eve_ross_get_eve_drawing:
    show player 10
    player_name "Где, ты говоришь, был {b}Скетч бук{/b}?"
    show player 11
    show eve 6b
    eve "О, у {b}Чада{/b}, наверное, он есть."
    show eve 2
    eve "Ему нравится мое искусство."
    show player 2
    show eve 1
    player_name "Хорошо, спасибо!"
    return

label button_eve_ask_model:
    show player 2
    show eve 1
    player_name "Я работаю над проектом для {b}Мисс Росс{/b}, и для него нужна живая модель."
    player_name "Тебе это будет интересно?"
    show player 1
    show eve 2
    eve "{b}Моделью{/b}? Это может быть весело."
    show player 2
    show eve 1
    player_name "Правда!? Потрясающе! Я надеялся, что ты это скажешь!"
    show player 1
    show eve 2
    eve "Да, я не возражаю. Хорошо, что я сегодня надела этот милый наряд."
    show player 10
    show eve 1
    player_name "... Ох, Ммм. Это будет обнаженная модель."
    show player 11
    show eve 2b
    eve "Голой?!"
    show eve 6
    eve "О, черт возьми, нет!"
    show player 10
    show eve 5
    player_name "Так ты не будешь этого делать? Я думал, ты увлекаешься искусством?"
    show player 11
    show eve 6
    eve "Да, но это не значит, что мне нравится публичная нагота!"
    show player 10
    show eve 5
    player_name "Хорошо подметила. Прости."
    show player 11
    show eve 2
    eve "Все в порядке. Просто не интересно."
    show player 2
    show eve 1
    player_name "Ну, спасибо в любом случае..."
    return

label button_eve_ross_get_paint:
    show player 2
    show eve 1
    player_name "Мне нужно немного краски. Есть идеи, где я могу их найти?"
    show player 1
    show eve 6b
    eve "Не знаю, Может сходим в магазин?"
    show player 2
    show eve 1
    player_name "Ну да, я знаю..."
    player_name "... Но краска для {b}Мисс Росс{/b}, и она не может позволить себе купить ее."
    show player 1
    show eve 6
    eve "О, хе-хе."
    show eve 4 with dissolve
    eve "Хм, свободная краска. Это круто."
    show eve 3
    show player 2
    player_name "Расскажи мне об этом..."
    show player 1
    show eve 2 with dissolve
    eve "Мы можем попробовать спросить {b}мою сестру{/b}."
    show player 2
    show eve 5
    player_name "Она {b}татуировщик{/b}, верно?"
    show player 1
    show eve 6
    eve "Она {b}лучший татуировщик{/b}!"
    eve "Ты должен прийти и попробовать, это удивительно!"
    show player 2
    show eve 5
    player_name "Думаешь, она разрешит мне немного краски?"
    show player 1
    show eve 2
    eve "Мы можем пойти и спросить ее."
    show eve 5
    show player 10
    player_name "Разве ее кабинет не называется {b}Сахарные Таты{/b}?"
    show player 11
    show eve 6
    eve "Да. Это на {b}северной стороне{/b} города."
    show player 2
    show eve 5
    player_name "Хорошо, встретимся там!"
    return

label button_eve_ross_get_paint_grace:
    show player 10
    show eve 5
    player_name "Где ты говорила твоя сестра?"
    show player 11
    show eve 2
    eve "{b}Сахарные Таты{/b}. Это на северной стороне города."
    show player 2
    show eve 5
    player_name "Хорошо, {b}встретимся там{/b}!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
