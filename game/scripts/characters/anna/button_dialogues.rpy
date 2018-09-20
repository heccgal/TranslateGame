label anna_dialogue_anna_dog_hunt:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Эй {b}[firstname]{/b}, вы видели {b}маленькую собаку{/b} без поводка??"
    show anna 4
    show player 10
    player_name "Я так не думаю..."
    show anna 5
    show player 11
    anna "Кажется, я его потеряла."
    anna "Я бежал по тропе мимо {b}леса{/b}, и когда я оглянулся назад, его уже не было рядом.!!"
    show anna 4
    show player 10
    player_name "Вы осматривали вдоль тропы?"
    show anna 5
    show player 11
    anna "Ну конечно! Я искала везде!"
    anna "Но я не могу пройти по тропе в лесу в одиночку...."
    show anna 4
    show player 10
    player_name "Как он выглядит?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "Ох, конечно. он {b}мопс{/b}, и вообщем-то всё!"
    show anna 5 at right
    anna "Его зовут {b}Шикардос{/b}."
    anna "У него немного избыточный вес, поэтому он не мог уйти далеко."
    anna "Пожалуйста! Ты поможешь мне найти его?"
    show anna 4
    return

label anna_dialogue_anna_dog_hunt_yes:
    show player 14
    player_name "Конечно. Я буду искать его."
    player_name "Что я ещё должен знать о нем?"
    player_name "Что-то, что поможет мне найти его?"
    show player 1
    show anna 5
    anna "Ну... Он действительно любит есть {b}печенье{/b}."
    anna "Если у вас есть, я уверен, что он их понюхает и покажется..."
    show anna 11
    show player 14
    player_name "Хорошо! Я приду к тебе, если найду его!"
    show anna 12
    show player 1
    anna "Огромное спасибо!"
    return

label anna_dialogue_anna_dog_hunt_no:
    show player 10
    player_name "Я хотел бы помочь, но у меня есть кое-что, что мне нужно для участия в..."
    show player 11
    show anna 5
    anna "О, извините, что беспокою вас..."
    return

label anna_dialogue_anna_find_dog_have_dog:
    scene location_park_closeup
    show player 247 at left with dissolve
    show anna 4 at right with dissolve
    player_name "Угадай, кого я нашел?"
    show anna 5 with vpunch
    anna "!!!"
    show anna 12
    anna "{b}Шикардос{/b}!!!"
    show player 1
    show anna 9
    with dissolve
    anna "Где вы его нашли?!"
    show anna 8
    show player 14
    player_name "Он был в лесу неподалеку, недалеко от тропы..."
    player_name "И вы оказались правы! Несколько печенья сделали свое дело."
    show anna 10
    show player 1
    anna "Спасибо вам {b}огромное{/b}!"
    show anna 9
    anna "Я обязательно вам как-нибудь отплачу."
    show anna 7
    anna "Я должна отвезти его домой. Он, наверное, проголодался после всего этого."
    show anna 10
    anna "Увидимся!"
    return

label anna_dialogue_anna_find_dog_do_not_have_dog:
    show player 11 at left with dissolve
    show anna 5 at right with dissolve
    anna "Вы его нашли???"
    show anna 4
    show player 10
    player_name "Еще нет..."
    player_name "Не могли бы вы еще раз описать? И где я могу его найти?"
    show player 11
    show anna 6 at Position(xpos=1002)
    anna "Он такой большой и он {b}мопс{/b}!"
    show anna 5 at right
    anna "Он должен быть где-то рядом с тропой в {b}лесу{/b}..."
    anna "...И он любит {b}печенье{/b}!"
    anna "Возможно, вы можете использовать несколько {b}печенья{/b}, чтобы заманить его."
    show anna 11
    show player 14
    player_name "Хорошо! Я пойду его искать!"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
