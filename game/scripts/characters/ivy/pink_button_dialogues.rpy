label button_ivy_start_intro:
    scene location_pink_closeup
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    ivy "Привет!"
    ivy "Могу я вам чем-нибудь помочь?"
    show player 29
    show ivy 1
    player_name "Это мой первый раз здесь. Я... Эмм..."
    show player 13
    show ivy 3
    ivy "Все нормально! Я понимаю! Все немного стесняются, когда впервые приходят сюда..."
    show ivy 2
    ivy "У нас есть большой выбор {b}игрушек{/b} и {b}сексуальной одежды{/b}, которые вы можете просмотреть на нашем настенном дисплее."
    show player 11
    ivy "Мы также можем предложить... {b}массаж всего тела сеанс{/b} в одном из наших... личных покой."
    ivy "Наша массажистка использует различные природные техники релаксации тела... Это, безусловно, удовлетворит ваши потребности..."
    show player 12
    show ivy 1
    player_name "О... Я не знала, что вы предлагаете здесь массаж."
    show player 1
    show ivy 3
    ivy "Это один из наших... меньше рекламируемых... услуг."
    show ivy 2
    ivy "Хотели бы вы увидеть нашу подборку {b}массажей{/b}?"
    return


label button_ivy_end_intro:
    scene pink
    show player 1 at left with dissolve
    show ivy 2 at right with dissolve
    ivy "Привет!"
    ivy "Могу я вам чем-нибудь помочь?"
    return

label button_ivy_package:
    show ivy 1
    show player 2
    player_name "Я здесь, чтобы забрать {b}посылку{/b}."
    show player 1
    show ivy 3
    ivy "Конечно!"
    show ivy 2
    ivy "На чье имя?"
    show ivy 1
    show player 12
    player_name "{b}Диана{/b}?"
    show player 1
    show ivy 11
    ivy "Дай мне проверить... Правильно! Вот она!"
    show ivy 1
    show player 170
    player_name "Благодарю!"
    show ivy 3
    show player 169
    ivy "Это для твоей {b}подружки{/b}?"
    show ivy 1
    show player 171
    player_name "!!!"
    show player 29
    player_name "О... Нет! Это для... Мммм... Кто-то попросил меня достать его для них!"
    show ivy 2
    show player 13
    ivy "Ну, это действительно хорошая вещь из нашей коллекции..."
    show ivy 3
    ivy "Я уверена, вам понравится!"
    show player 21
    show ivy 4
    player_name "Спасибо..."
    hide player 21
    hide ivy 4
    show unlock29 at truecenter
    with dissolve
    pause
    hide unlock29 with dissolve
    return

label button_ivy_massage:
    show ivy 5
    show player 21
    player_name "Могу ли я увидеть ... ваш {b}памфлет{/b}?"
    show player 13
    show ivy 4
    ivy "Конечно! Делай как знаешь!"
    player_name "Спасибо..."
    hide ivy
    hide player
    with dissolve
    return

label button_ivy_just_shopping:
    show player 10
    show ivy 1
    player_name "У меня все хорошо, спасибо."
    player_name "Я здесь, чтобы сделать покупки..."
    show player 13
    show ivy 3
    ivy "Тогда ладно! Дай знать, если что - то понадобится."
    return

label button_ivy_massage_first:
    show ivy 5
    show player 21
    player_name "Думаю, я могу на него взглянуть..."
    show player 13
    show ivy 4
    ivy "Конечно! Делай как знаешь!"
    hide ivy
    hide player
    with dissolve
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
