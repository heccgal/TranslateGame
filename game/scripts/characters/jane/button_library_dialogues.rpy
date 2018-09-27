label jane_library_dialogue_bissette_find_dictionary:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 10f at right
    with dissolve
    player_name "Я не могу найти словарь {b}французского языка{/b}."
    show player 5f
    show jane 2f
    jan "Хм, дай посмотреть..."
    show jane 1b
    pause
    show jane 2b
    jan "Он должен быть там, на полке, рядом с задней комнатой."
    show jane 1f
    show player 14f
    player_name "Хорошо, я сейчас посмотрю. Спасибо."
    return

label jane_library_dialogue_bissette_get_dictionary:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 504f at right
    with dissolve
    player_name "Ну, я нашел часть французского словаря."
    show player 503f
    show jane 4f
    jan "Что?"
    show player 5f
    show jane 17bf
    with dissolve
    jan "О нет!"
    jan "Мне придется заказать новый, но это займет некоторое время."
    jan "Ты все еще хочешь проверить?"
    show jane 18bf
    show player 10f
    player_name "Да, я в полном отчаянии. Я просто надеюсь, что мне не нужны эти недостающие страницы..."
    show player 5f
    show jane 17bf
    jan "Ладно, что ж, простите еще раз!"
    show jane 18f
    jan "Ты можешь просто оставить его себе. Я не буду использовать здесь..."
    show jane 1f with dissolve
    show player 504f with dissolve
    player_name "Спасибо!"
    show player 503f
    show jane 3f
    jan "Нет проблем, хорошего дня!"
    hide player
    hide jane
    with dissolve

    scene library
    show player 34 with dissolve
    player_name "( Думаю, мне стоит отнести это {b}Мисс Биссетт{/b} и посмотреть, что она думает.... )"
    return

label jane_library_dialogue_bissette_return_overdue_books:
    show jane 1f at Position (xpos=270)
    show xtra 42
    show player 14f at right
    with dissolve
    player_name "Я нашел все просроченные книги!"
    show player 239_240f with dissolve
    pause
    show player 507f at Position (xoffset=-9) with dissolve
    show jane 2f
    jan "Правда? Давайте посмотрим..."
    show player 13f
    show jane 22f at Position (xoffset=-18) with dissolve
    jan "У тебя получилось! Большое спасибо!"
    jan "У меня тоже есть кое-что для тебя."
    show jane 21f at Position (xoffset=-18)
    show player 10f
    player_name "Что именно?"
    show jane 20f with dissolve
    jan "Да, пришла книга, которую ты заказал."
    show jane 19f with dissolve
    pause
    show player 521f
    show jane 1f
    with dissolve
    player_name "Спасибо!"
    player_name "{b}101 вид сыра{/b}..."
    show player 5f with dissolve
    show jane 2f
    jan "Это сработает?"
    show jane 1f
    show player 10f
    player_name "Мне придется обойтись без этого."
    show player 14f
    player_name "Спасибо снова!"
    show player 13f
    show jane 3f
    jan "Возвращайтесь поскорей!"
    return

label jane_library_dialogue_pre:
    show jane 2f at Position (xpos=270)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Привет! Чем я могу вам помочь?"
    show player 2f
    show jane 1f
    player_name "Привет, я ищу {b}книгу{/b}."
    show player 1f
    show jane 2f
    jan "Конечно же! Ты знаешь Название книги?"
    show jane 1f
    return

label jane_library_dialogue_milk_production_books:
    show player 14f
    player_name "Это может показаться странным, но у вас есть что-нибудь в библиотеке об увеличении производства молока?"
    show player 13f
    pause
    show jane 4f
    jan "Эм... Зачем? Не думаю, что ты когда-нибудь сможешь кормить грудью."
    show jane 2f
    jan "О! Упс! Ты, наверное, имеешь в виду фермерство, да?"
    show jane 1f
    show player 10f
    player_name "Мммм... На самом деле, я заинтересован в изучении любой темы, я думаю..."
    show player 13f
    show jane 4f
    jan "Проверь Книжную Полку вон там. У нас должно быть что-то."
    show jane 1f
    show player 14f
    player_name "Спасибо вам!"
    show player 13f
    show jane 2f
    jan "Всегда пожалуйста!"
    return

label jane_library_dialogue_french_poetry:
    show player 10f
    player_name "У вас есть французская поэзия?"
    show player 5f
    show jane 1b
    jan "Хмм..."
    show jane 2f
    jan "Фактически..."
    jan "Некоторые девушки читали что-то подобное {b}вчера днем{/b}."
    show jane 1f
    show player 10f
    player_name "Серьёзно?"
    show player 12f
    player_name "Они что-нибудь проверили?"
    show player 5f
    show jane 2f
    jan "Нет."
    show jane 1f
    show player 10f
    player_name "Вы знаете, где она находится?"
    show player 5f
    show jane 5f
    jan "..."
    show jane 4f
    jan "Нет..."
    jan "Но, может быть, они будут здесь снова в {b}этот день{/b}."
    jan "Вы можете спросить одного из них, куда они его положили."
    show jane 1f
    show player 12f
    player_name "Спасибо."
    return

label jane_library_dialogue_french_food_find_books:
    show player 10f
    player_name "Мне было интересно, есть ли у вас книги о французской еде?"
    show player 13f
    show jane 3f
    jan "Это интересная тема..."
    show jane 1f
    show player 14f
    player_name "Да, мне это нужно для школьного задания."
    show player 13f
    show jane 2f
    jan "Хорошо, Дай мне посмотреть, что у нас есть."
    show jane 1b
    jan "..."
    show player 11f
    player_name "..."
    show player 5f
    show jane 2b
    jan "Хм, у нас нет ничего подобного."
    show jane 1f
    show player 12f
    player_name "Прям ничего?"
    show player 5f
    show jane 2b
    jan "Нет... Ой, подожди секунду!"
    jan "Это говорит о том, что у нашей сестры бранч есть французская книга о сыре."
    show jane 2f
    jan "Это сработает?"
    show jane 1f
    show player 14f
    player_name "Конечно, мне нравится сыр! Где мне нужно его забрать?"
    show player 13f
    show jane 2f
    jan "Я могу попросить их прислать его сюда. Это займет всего несколько дней..."
    jan "А пока, не могли бы вы мне чем-нибудь помочь?"
    show jane 1f
    show player 10f
    player_name "... Конечно, я полагаю. Что именно вам необходимо?"
    show player 5f
    show jane 2f
    jan "{b}Некоторые из ваших одноклассников просрочили книги{/b}, которые я хотела бы вернуть."
    jan "Я отправляла письма к ним домой, но, похоже, это не работает."
    jan "Мне бы не хотелось потерять книги."
    show jane 1f
    show player 10f
    player_name "Да, я могу попробовать {b}поговорить с ними{/b}. Как их имена?"
    show player 5f
    show jane 2b
    jan "Во-первых, это {b}Мисс Мартинез{/b}."
    jan "Второй {b}Мр. Эрик{/b}."
    show jane 1f
    show player 14f
    player_name "{b}У Эрика{/b} вышла книга?!"
    player_name "Это должно быть просто."
    show player 13f
    show jane 2b
    jan "...И напоследок..."
    jan "Да. Там просто написано {b}Декстер{/b}."
    jan "Никого не припоминаешь?"
    show jane 1f
    show player 12f
    player_name "О боже, только не {b}Декстер{/b}... Вы уверены?"
    show player 11f
    show jane 2f
    jan "Так написано в журнале..."
    show jane 1f
    show player 12f
    player_name "Дерьмо! Хорошо, я посмотрю, что можно сделать."
    show player 5f
    show jane 3f
    jan "Спасибо, я действительно ценю это!"
    hide jane with dissolve
    show player 12 at center with dissolve
    player_name "Почему это должен был быть {b}Декстер{/b}?"
    return

label jane_library_dialogue_french_food_book_holders:
    show player 10f
    player_name "Еще раз, как зовут студентов?"
    player_name "Знаешь, те, у которых просроченные книги."
    show player 5f
    show jane 2f
    jan "Одну секунду..."
    show jane 2b
    jan "Хмм, {b}Мисс Мартинез{/b}, {b}Мр. Эрик{/b}, и {b}Декстер{/b}."
    show jane 1f
    show player 12f
    player_name "Тьфу, я совсем забыл про...  {b}Декстера{/b}..."
    player_name "Хорошо, я займусь этим."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "Я делаю коллаж для художественного класса и мне нужны старые журналы."
    player_name "Не могли бы вы мне показать, где они у вас находятся?"
    show player 1f
    show jane 2f
    jan "Боюсь, что вам не повезло. Мы перестали приносить их несколько месяцев назад."
    show player 10f
    show jane 1f
    player_name "У у вас ничего не осталось?"
    show player 1f
    show jane 2f
    jan "Боюсь, что нет. Мы отправили все, что у нас было, на переработку."
    show player 10f
    show jane 1f
    player_name "Ох боже..."
    player_name "Все равно спасибо."
    show player 11f
    show jane 2f
    jan "Жаль."

    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "Что же мне теперь делать?"
    show player 11
    player_name "..."
    show player 10
    player_name "Думаю, я {b}вернусь в школу и осмотрюсь{/b}."
    player_name "Где-то должны быть какие-то журналы."
    return

label jane_library_dialogue_magazines_repeat:
    show player 10f
    player_name "Так у вас здесь нет ни одного журнала?"
    show player 11f
    show jane 2f
    jan "Нет."
    jan "Мы отменили подписку и выбросили то, что у нас было."
    show jane 1f
    show player 10f
    player_name "Ладно, спасибо в любом случае."
    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "{b}*Вздох*{/b}"
    player_name "Думаю, мне стоит {b}вернуться в школу и осмотреться там{/b}."
    player_name "... Может быть, мне повезет?"
    return

label jane_library_dialogue_return_books_pre:
    show player 14f
    player_name "Я хотел бы вернуть книгу."
    show player 13f
    show jane 3f
    jan "Превосходно!"
    return

label jane_library_dialogue_return_books_first:
    show jane 2f
    jan "Не многие люди это делают."
    show jane 1f
    show player 10f
    player_name "Что тогда происходит?"
    show player 5f
    show jane 8f
    jan "Я выслеживаю их и ломаю им ноги, чтобы они больше так не делали."
    show jane 12f
    show player 22f
    player_name "!!!"
    show jane 3f
    jan "Просто шучу!"
    show jane 1f
    show player 29f with dissolve
    player_name "Ох."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane 2f
    jan "Просто поставь книги, которые ты хочешь вернуть, на прилавок, а я позабочусь об этом."
    show jane 3f
    jan "И возвращайтесь поскорее!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane 4f
    player_name "Простите. Я вернусь, как только вспомню название книги."
    show player 5f
    show jane 2f
    jan "Тогда увидимся."
    return

label jane_library_dialogue_french_grammar_pre:
    scene librarydesk
    show jane 2f at Position (xpos=270)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Привет! Чем я могу вам помочь?"
    show player 2f
    show jane 1f
    player_name "Здравствуйте, я ищу книгу."
    show player 1f
    show jane 2f
    jan "Конечно, ты знаешь её название?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1:
    show player 14f at right
    show jane 1f
    player_name "Да, мне нужно \"{b}Грамматика Французского Языка - Том 1{/b}\""
    show player 1f
    show jane 4f
    jan "Ты принес мне то, о чем я тебя просила?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1_have_webcam:
    show player 12f
    player_name "Да... Вот {b}веб-камера{/b}."
    show player 239_240f
    pause
    show player 54 at Position(xoffset=-38) with fastdissolve
    pause
    show player 1f with fastdissolve
    show jane 3f
    jan "Спасибо тебе!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Как насчет {b}моего учебника{/b}?"
    show player 11f
    show jane 3f
    jan "О! Боже правый..."
    show player 11f
    jan "Он пришел сегодня утром, и я положила его на {b}полку{/b} вон там."
    jan "Идите вперед и возьмите его."
    show player 1f
    show jane 3f
    jan "Увидимся в следующий раз!s"
    return

label jane_library_dialogue_french_grammar_volume_1_do_not_have_webcam:
    show player 24f
    player_name "Я пока не знаю..."
    show player 5f
    show jane 2f
    jan "Тогда я не могу заказать {b}учебник{/b} для тебя, ты же знаешь."
    jan "Возвращайся, когда у тебя будет {b}веб-камера{/b}, и мы поговорим."
    return

label jane_library_dialogue_french_grammar_volume_2_first:
    show player 14f
    player_name "Мне нужна книга: {b}Грамматика Французского Языка - Том 2{/b}"
    show player 1f
    show jane 2f
    jan "Вы знаете, но..."
    jan "Я все еще не могу делать новые заказы в данный момент."
    show player 12f
    show jane 1f
    player_name "До сих пор?"
    show player 5f
    show jane 4f
    jan "Я хотела бы дать её вам... Но наши средства все ещё низки."
    show player 10f
    show jane 1f
    player_name "Что вы имеете в виду? Я думал, что новая {b}веб камера{/b} вам помогла??"
    show player 5f
    show jane 4f
    jan "Не поймите меня неправильно: она помогает..."
    jan "но люди устают от одного и того же!"
    show player 10f
    show jane 1f
    player_name "Так... Что мы можем сделать?"
    show player 5f
    show jane 4f
    jan "Ну, нашим зрителям хочется большего разнообразия..."
    show player 11f
    show jane 3f
    jan "...и вы, возможно, могли бы мне с этим!"
    show player 12f
    show jane 1f
    player_name "Но, как?"
    show player 11f
    show jane 2f
    jan "Ты не ходишь в школу?"
    show player 12f
    show jane 1f
    player_name "Да?"
    show player 11f
    show jane 3f
    jan "Ну, просто спрячь одну из моих дистанционно управляемых {b}веб-камер{/b} в школе!"
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Вы с ума сошли?!"
    player_name "Что мне делать, если меня поймают!"
    show jane 3f
    show player 90f
    jan "Расслабься! Просто иди ночью, когда никого нет рядом."
    show player 37f
    show jane 1f
    player_name "Тьфу... Не могу поверить, что мне приходится это делать..."
    show jane 2f
    jan "Тебе нужны эти книги, или нет?"
    show player 24f
    show jane 1f
    player_name "Посмотрим, что я смогу сделать..."
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_pre:
    show player 14f
    player_name "Мне нужна книга: {b}Грамматика Французского Языка - Том 2{/b}"
    show player 1f
    show jane 4f
    jan "Ну? Ты это сделал?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_placed_webcam:
    show player 12f
    player_name "Да. Я положил её в {b}душевую{/b}..."
    player_name "Она в потолочном {b}вентиляционном отверстии{/b}..."
    show player 1f
    show jane 3f
    jan "Спасибо тебе!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Как насчет моего {b}учебника{/b}?!"
    show player 11f
    show jane 3f
    jan "О! Ты прав..."
    show player 11f
    show jane 15
    jan "Вот оно!"
    $ player.get_item("textbook2")
    show player 30f
    show jane 1f
    player_name "Спасибо!"
    show player 1f
    show jane 3f
    jan "Увидимся в следующий раз!"
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_havent_placed_webcam:
    show player 24f
    show jane 4f
    player_name "Я этого еще не сделал...."
    show player 5f
    show jane 2f
    jan "Тогда я не могу сделать этот заказ {b}учебника{/b} для тебя. Ты это знаешь."
    jan "Вернись, когда разместишь {b}веб-камеру{/b} в школе."
    return

label jane_library_dialogue_french_grammar_volume_3:
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
