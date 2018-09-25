label ronda_dialogue_intro:
    scene gym
    show ronda 2 at right
    show player 36 at left
    with dissolve
    player_name "Эй, {b}Ронда{/b}. Как поживаешь?"
    show player 13 with dissolve
    show ronda 3
    ron "У меня все хорошо получается. Вопрос, ты тренировался?"
    show ronda 2
    show player 11
    player_name "..."
    show player 10
    player_name "Нет-"
    show player 11
    show ronda 4
    ron "Тогда перестань шевелить губами и начинай шевелить ими... ногами!"
    show ronda 2
    show player 34
    player_name "???"
    show ronda 3
    ron "Неважно. Это просто то, что мой папа всегда говорит..."
    show player 5
    ron "Во всяком случае, вам лучше поторопиться, потому что испытания идут быстро!"
    show ronda 2
    return

label ronda_dialogue_talent_show_help:
    show player 10
    player_name "Я не думаю, что ты была бы заинтересована в волонтерстве для музыкального шоу талантов {b}Мисс Девитт{/b}?"
    show player 5
    show ronda 3
    ron "Музыкальный Талант? Нет, мне было бы неинтересно."
    show ronda 2
    show player 10
    player_name "- Ты уверена? Ты вообще не играешь на инструментах и не поешь?"
    show player 5
    show ronda 3
    ron "Разве ты не видишь, что у меня есть более важные вещи, на которых нужно сосредоточиться. Как трек и плавание..."
    ron "Вещи, на которых ты должен сосредоточиться!"
    ron "Ты никогда не попадешь в команду, если будешь игнорировать свои тренировки!"
    show ronda 2
    show player 30
    player_name "Знаешь, в жизни есть нечто большее, чем спорт, {b}Ронда{/b}..."
    show player 5
    show ronda 3
    ron "Пффф, да, конечно."
    return

label ronda_dialogue_model_help:
    show player 2 at left
    show ronda 2 at right
    player_name "Я работаю над проектом для {b}Мисс Росс{/b}, и для него требуется живая модель."
    player_name "Тебе это будет интересно?"
    show player 1
    show ronda 3
    ron "Занята."
    show player 10
    show ronda 2
    player_name "Занята?"
    player_name "Всм?"
    show player 11
    show ronda 4
    ron "Серьёзно, {b}[firstname]{/b}?!"
    ron "Я должена бежать 6 миль и должна принять ледяную баню до тренировки."
    show player 10
    show ronda 1
    player_name "Ухх..."
    show player 11
    show ronda 4
    ron "После этого у меня есть только 40 минут, чтобы сделать несколько кругов до закрытия бассейна."
    show player 10
    show ronda 1
    player_name "Это..."
    show player 11
    show ronda 4
    ron "Затем я возвращаюсь домой к тёплой подушке и хрущу."
    show player 12
    show ronda 1
    player_name "Окей! Окей! Я понял..."
    hide ronda
    hide player
    show player 12
    with dissolve
    player_name "Эта девчонка ненормальная!"
    return

label ronda_dialogue_leave:
    show player 10
    player_name "Хорошо."
    player_name "Увидимся."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
