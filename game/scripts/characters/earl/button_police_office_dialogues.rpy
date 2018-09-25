label earl_police_office_dialogue_roxxy_ask_earl_release:
    show earl 1 at right
    show roxxy 1of at Position (xpos=400)
    show player 10 at left
    with dissolve
    player_name "Простите, сэр?"
    show player 5
    show earl 2
    ear "Да?"
    ear "Что вы здесь делаете?"
    show earl 3 with dissolve
    show player 10
    player_name "Мы просто пытаемся получить информацию об аресте, который вы сегодня произвели."
    show player 5
    show earl 2 with dissolve
    ear "Хм, ты ведь дочь {b}Кристи{/b}, не так ли?"
    show earl 1
    show roxxy 1jf
    rox "..."
    show player 10
    player_name "Да, именно так и есть, сэр."
    player_name "Не могли бы вы рассказать нам, что происходит?"
    show player 5
    show earl 2
    ear "Боюсь, мне запрещено обсуждать эти вопросы с кем-либо, кроме ее семьи."
    ear "Если вы хотите пойти со мной, Мисс. Я расскажу вам, как все это работает."
    show earl 1
    show player 10
    player_name "... Да, хорошо. Я подожду-"
    show player 11
    show roxxy 2c at Position (xpos=500) with dissolve
    rox "Нет!"
    show roxxy 2cf at Position (xpos=434)
    with dissolve
    rox "... Я имею в виду."
    show roxxy 33f at Position (xpos=400) with dissolve
    rox "Я хочу, чтобы он остался. Все в порядке."
    show roxxy 32f
    show player 13
    ear "..."
    show earl 2
    ear "Ты уверена."
    show earl 1
    show roxxy 33f
    rox "Да."
    show roxxy 32f
    show earl 2
    ear "Делай как знаешь."
    ear "Сегодня утром мы получили анонимную наводку о большом запасе наркотиков в вашей резиденции."
    ear "Поэтому мы поехали посмотреть."
    ear "Вы знали, что у {b}вашей матери{/b} было более фунта кристаллического метамфетамина, спрятанного под диваном?"
    show earl 1
    show roxxy 1if
    show player 23
    player_name "Фунт?!"
    show player 22
    show roxxy 27f at Position (xoffset=67)
    rox "..."
    show earl 2
    ear "Боюсь, что так."
    ear "Это уголовное обвинение за наркотики."
    ear "Мы удерживаем {b}твою мать{/b} за хранение с намерением продать."
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "..."
    show player 10
    player_name "В этом нет ничего хорошего."
    show player 5
    show roxxy 1jf with dissolve
    show earl 2
    ear "Нет, сынок. Это определенно не так."
    ear "... Теперь, я знаю {b}Кристи{/b} в течение длительного времени."
    ear "Когда-то мы вместе ходили в школу."
    ear "Она всегда умела попадать в неприятности..."
    ear "... Но после допроса сегодня утром, я могу сказать вам без сомнения, что она не знает ничего о приготовлении метамфетамина."
    ear "Теперь она утверждает, что она сделала все сама и искала, чтобы переместить его..."
    ear "... Но я бы поставил хорошие деньги, что она просто держала его для кого-то другого!"
    show earl 1
    rox "..."
    show earl 2
    ear "К сожалению, если я не получу доказательств. Она надолго попадет в тюрьму."
    show earl 1
    show roxxy 33bf at Position (xoffset=34) with dissolve
    rox "{b}*Сопит*{/b}."
    show player 10
    player_name "Хорошо, а что насчет дома моей подруги?"
    show roxxy 1jf with dissolve
    show player 5
    show earl 2
    ear "О, Этот трейлер?"
    ear "... Ну, если {b}Кристи{/b} будет осуждена, он будет возвращен государством и продан."
    show earl 1
    show player 25
    player_name "Шиш..."
    show player 12
    player_name "Мы можем что-нибудь сделать, чтобы предотвратить это?"
    show player 5
    show earl 2
    ear "Нет, если только ты не убедишь {b}Кристи{/b} отказаться от того, кого она защищает...."
    show earl 1
    rox "..."
    show player 11
    player_name "..."
    show player 5
    show earl 2
    ear "Мне очень жаль, что все так вышло, Мисс."
    show earl 1
    rox "{b}*Сопит*{/b}"
    show earl 2
    ear "Вы все можете {b}спуститься в камеру и навестить ее{/b}, если хотите."
    ear "Они уже должны были допросить ее."
    show earl 1
    show player 14
    player_name "Хорошо, Спасибо за информацию, офицер."
    show player 13
    hide earl with dissolve
    pause
    show player 5
    show roxxy 33bf
    rox "... {b}*Сопит*{/b} Все это для этого врожденного идиота..."
    show roxxy 1j with dissolve
    show player 10
    player_name "Давай, пойдем поговорим с {b}твоей мамой{/b}."
    hide player
    hide roxxy
    with dissolve
    return

label earl_police_office_dialogue_first_visit:
    show earl 2 at right
    show player 11 at left
    with dissolve
    ear "Что ты здесь делаешь?!"
    show earl 3
    ear "Это еще один из тех дней \"приведи своих детей на работу\"?"
    show earl 1
    show player 14
    player_name "О, Нет, я просто проезжаю мимо, сэр."
    player_name "Я хотел поговорить с {b}Гарольдом{/b}."
    show earl 2
    show player 1
    ear "Подожди минутку... Ты не ходишь в школу с моей дочерью?"
    show earl 3
    show player 14
    player_name "А, точно! Dы {и}Отец Ронды{/b}!"
    show earl 2
    show player 1
    ear "Вот дерьмо!"
    show player 11
    ear "Ты лучше следи за моей малышкой, или мне придется поставить наблюдение за {b}тобой{/b}."
    show earl 4
    ear "Понял?!"
    show earl 1
    show player 29
    player_name "Ох... конечно, сэр!"
    player_name "Я бы никогда-"
    show earl 2
    show player 13 at left
    ear "Расслабься, я просто прикалываюсь! Живо, живо."
    return

label earl_police_office_dialogue_pre:
    show earl 2 at right
    show player 1 at left
    with dissolve
    ear "Привет, что случилось?"
    show earl 3
    return

label earl_police_office_dialogue_donuts:
    show earl 1
    show player 14
    player_name "Это может показаться глупым вопросом,но какие пончики нравятся {b}Гарольду{/b}?"
    show player 1
    show earl 2
    ear "Хах!"
    ear "{b}Гарольд{/b} ест их, только если они в {b}[harold_glaze]{/b}..."
    show earl 3
    ear "... Но я не знаю, что еще он на них сыпит."
    show player 14
    show earl 1
    player_name "Я вижу."
    show player 11
    show earl 2
    ear "Почему вы спрашиваете?"
    show player 17
    show earl 1
    player_name "О, без причины."
    show player 11
    show earl 4
    ear "Подожди, разве ты не должна быть в школе? Что ты здесь делаешь-"
    show player 14
    show earl 3
    player_name "Эмм..."
    show player 17
    player_name "Спасибо, пока!"
    return

label earl_police_office_dialogue_harold:
    show player 10
    player_name "Ты знаешь, где может быть {b}Гарольд{/b}?"
    player_name "Я возможно ошибаюсь... но он должен быть здесь!"
    show player 11
    show earl 2
    ear "Я не уверен, куда он пошел, но я видела его вчера в офисе..."
    ear "...Он выглядел в плохом состоянии, это точно!"
    ear "На секунду мне показалось, что он уходит..."
    ear "...Поэтому я сказала ему взять перерыв."
    show earl 1
    show player 12
    player_name "Он не упоминал, где будет во время дежурства?"
    show player 5
    show earl 2
    ear "Я не хотел задавать слишком много вопросов, понимаешь?"
    ear "Иногда парням нужно побыть наедине..."
    show earl 1
    show player 14
    player_name "Хорошо, спасибо."
    return

label earl_police_office_dialogue_roxxys_mom:
    show earl 1
    show player 12
    player_name "Где мы можем поговорить с {b}мамой моей{/b} подруги?"
    show player 5
    show earl 2
    ear "Она внизу, в {b}камере{/b}."
    ear "Офицер {b}Юми{/b} внизу, но она даст вам немного личного пространства, чтобы поговорить."
    show earl 1
    show player 14
    player_name "Хорошо, спасибо."
    return

label earl_police_office_dialogue_leave:
    show player 14
    player_name "Прошу прощения, сэр."
    show earl 2
    show player 1
    ear "Ладно."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
