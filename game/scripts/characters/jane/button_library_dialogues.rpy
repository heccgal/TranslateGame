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
    player_name "What were the students names again?"
    player_name "You know, the ones with the overdue books."
    show player 5f
    show jane 2f
    jan "One second..."
    show jane 2b
    jan "Hmm, {b}Miss Martinez{/b}, {b}Mr. Erik{/b}, and a {b}Dexter{/b}."
    show jane 1f
    show player 12f
    player_name "Ugh, I forgot about {b}Dexter{/b}..."
    player_name "Alright, I'm on it."
    return

label jane_library_dialogue_magazines_first:
    show player 2f
    player_name "I'm making a collage for Art class and I need some old magazines."
    player_name "Could you show me where to find some?"
    show player 1f
    show jane 2f
    jan "You're out of luck I'm afraid. We stopped carrying those a few months ago."
    show player 10f
    show jane 1f
    player_name "You don't have any?"
    show player 1f
    show jane 2f
    jan "I'm afraid not. We sent all the ones we had off to be recycled."
    show player 10f
    show jane 1f
    player_name "Oh man..."
    player_name "Thanks anyways."
    show player 11f
    show jane 2f
    jan "Sorry."

    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "What am I gonna do now?"
    show player 11
    player_name "..."
    show player 10
    player_name "I guess {b}I'll head back to school and look around{/b}."
    player_name "There's gotta be some magazines somewhere."
    return

label jane_library_dialogue_magazines_repeat:
    show player 10f
    player_name "So don't have a single magazine around here?"
    show player 11f
    show jane 2f
    jan "Nope."
    jan "We cancelled the subscriptions and tossed what we had out."
    show jane 1f
    show player 10f
    player_name "Okay, thanks anyways."
    hide jane
    hide xtra
    hide player
    with dissolve
    show player 10 with dissolve
    player_name "{b}*Sigh*{/b}"
    player_name "I guess I should {b}head back to school and look around there.{/b}"
    player_name "... Maybe I'll get lucky?"
    return

label jane_library_dialogue_return_books_pre:
    show player 14f
    player_name "I'd like to return a book."
    show player 13f
    show jane 3f
    jan "Great!"
    return

label jane_library_dialogue_return_books_first:
    show jane 2f
    jan "Not many people do."
    show jane 1f
    show player 10f
    player_name "What happens then?"
    show player 5f
    show jane 8f
    jan "I hunt them down and break one of their legs so they don't do it again."
    show jane 12f
    show player 22f
    player_name "!!!"
    show jane 3f
    jan "Just kidding!"
    show jane 1f
    show player 29f with dissolve
    player_name "Oh."
    show player 3f at Position (xoffset=-8)
    return

label jane_library_dialogue_return_books_after:
    show jane 2f
    jan "Just set the books you want to return on the counter and I'll take care of it."
    show jane 3f
    jan "And come back soon!"
    return

label jane_library_dialogue_leave:
    show player 24f
    show jane 4f
    player_name "Sorry. I'll return once I remember the book's name."
    show player 5f
    show jane 2f
    jan "See you then."
    return

label jane_library_dialogue_french_grammar_pre:
    scene librarydesk
    show jane 2f at Position (xpos=270)
    show xtra 42
    show player 1f at right
    with dissolve
    jan "Hi! How can I help you?"
    show player 2f
    show jane 1f
    player_name "Hi, I'm looking for a book."
    show player 1f
    show jane 2f
    jan "Sure thing, do you know its name?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1:
    show player 14f at right
    show jane 1f
    player_name "Yeah, I need \"{b}French Grammar - Volume 1{/b}\""
    show player 1f
    show jane 4f
    jan "Did you get me what I asked you for?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_1_have_webcam:
    show player 12f
    player_name "Yeah... Here's the {b}webcam{/b}."
    show player 239_240f
    pause
    show player 54 at Position(xoffset=-38) with fastdissolve
    pause
    show player 1f with fastdissolve
    show jane 3f
    jan "Thank you!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "What about my {b}textbook{/b}?"
    show player 11f
    show jane 3f
    jan "Oh! Right..."
    show player 11f
    jan "It came in earlier today, I put it on the {b}shelf{/b} over there."
    jan "Go ahead and take it."
    show player 1f
    show jane 3f
    jan "See you next time!"
    return

label jane_library_dialogue_french_grammar_volume_1_do_not_have_webcam:
    show player 24f
    player_name "I don't have it yet..."
    show player 5f
    show jane 2f
    jan "I can't get that {b}textbook{/b} order for you then, you know that."
    jan "Come back when you have the {b}webcam{/b}, and we'll talk."
    return

label jane_library_dialogue_french_grammar_volume_2_first:
    show player 14f
    player_name "I need the book: {b}French Grammar - Volume 2{/b}"
    show player 1f
    show jane 2f
    jan "You know how it is..."
    jan "I still can't make any new orders at this moment."
    show player 12f
    show jane 1f
    player_name "Still??"
    show player 5f
    show jane 4f
    jan "I would love to get that for you... But our funds are still low."
    show player 10f
    show jane 1f
    player_name "What do you mean? I thought the new {b}webcam{/b} was helping??"
    show player 5f
    show jane 4f
    jan "Don't get me wrong: It's helping..."
    jan "but people are getting tired of the same stuff!"
    show player 10f
    show jane 1f
    player_name "So... What can we do?"
    show player 5f
    show jane 4f
    jan "Well, our viewers want more variety..."
    show player 11f
    show jane 3f
    jan "...and I maybe you could help with that!"
    show player 12f
    show jane 1f
    player_name "But, how?"
    show player 11f
    show jane 2f
    jan "Don't you go to school?"
    show player 12f
    show jane 1f
    player_name "Yeah?"
    show player 11f
    show jane 3f
    jan "Well, just hide one of my remote controlled {b}webcams{/b} in the school!"
    show jane 1f
    player_name "..."
    show player 12f
    player_name "Are you crazy?!"
    player_name "What if I got caught!"
    show jane 3f
    show player 90f
    jan "Relax! Just go at night, when no one is around."
    show player 37f
    show jane 1f
    player_name "Ugh... I can't believe I have to do this..."
    show jane 2f
    jan "Do you want those books, or not?"
    show player 24f
    show jane 1f
    player_name "I'll see what I can do..."
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_pre:
    show player 14f
    player_name "I need the book: {b}French Grammar - Volume 2{/b}"
    show player 1f
    show jane 4f
    jan "Well? Did you do it?"
    show jane 1f
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_placed_webcam:
    show player 12f
    player_name "Yeah. I placed it in the {b}lockeroom{/b}..."
    player_name "It's in the ceiling {b}air vent{/b}..."
    show player 1f
    show jane 3f
    jan "Thank you!"
    show player 16f
    show jane 1f
    player_name "..."
    show player 12f
    player_name "What about my {b}textbook{/b}?!"
    show player 11f
    show jane 3f
    jan "Oh! Right..."
    show player 11f
    show jane 15
    jan "Here it is!"
    $ player.get_item("textbook2")
    show player 30f
    show jane 1f
    player_name "Thanks!"
    show player 1f
    show jane 3f
    jan "See you next time!"
    return

label jane_library_dialogue_french_grammar_volume_2_repeat_havent_placed_webcam:
    show player 24f
    show jane 4f
    player_name "I didn't do it yet..."
    show player 5f
    show jane 2f
    jan "I can't get that {b}textbook{/b} order for you, then. You know that."
    jan "Come back when you placed the {b}webcam{/b} at school."
    return

label jane_library_dialogue_french_grammar_volume_3:
    show popup_unfinished at truecenter with dissolve
    pause
    hide popup_unfinished with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
