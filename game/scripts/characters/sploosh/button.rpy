label sploosh_button_dialogue:
    scene expression game.timer.image("backgrounds/location_pier_boxes{}.jpg")
    show player 10 at left with dissolve
    show sploosh 1 at right
    player_name "Привет?"
    Sploosh "ZZZzzzz..."
    show player 4
    player_name "(Хм... Он должно быть спит)"
    menu:
        "Проснуться Адмирал Сплушш":
            show player 10
            player_name "Э... Простите?"
            show sploosh 2
            show player 11
            python:
                if store.sploosh["amount"] != 0:












                    dialogues = store.sploosh["dialogues"][random.randint(0, store.sploosh["amount"]-1)]
                    for dialogue in dialogues:
                        d = re.sub("\\\\n", "\\n", dialogue)
                        Sploosh(d)
                else:
                    renpy.show("player 23")
                    Sploosh("Я-король всего мира!!!")
            show player 23
            player_name "!!!" with hpunch
            show sploosh 1
            Sploosh "ZZZzzzz..."
            show player 1
            player_name "What a strange pirate..."
            hide player with dissolve
        "Уйти":
            player_name "Я лучше не буду его беспокоить..."
            Sploosh "ZZZzzzz..."
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
