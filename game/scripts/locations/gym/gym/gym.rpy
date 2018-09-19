label training_dialogue:
    $ player.go_to(L_gym)
    if training_count == 0:
        call expression game.dialog_select("gym_training_dialogue_first")
        if quest07 not in completed_quests:
            $ quest_list.append(quest07)
        $ sis_door_locked_count = 1
        $ training_count = 1
        $ training_tier = 1
        $ sister.add_event(sis_panty01)

    elif training_count == 1 and training_tier == 2 and sister.over(sis_shower_cuddle01):
        call expression game.dialog_select("gym_training_dialogue_second")
        $ training_count = 2
        $ sister.add_event(sis_panty02)

    elif training_count == 2 and training_tier == 3 and sister.over(sis_couch02):
        call expression game.dialog_select("gym_training_dialogue_third")
        $ training_count = 3
        $ sister.add_event(sis_panty03)

    elif training_count == 3 and training_tier == 4 and sister.over(sis_couch03):
        call expression game.dialog_select("gym_training_dialogue_fourth")
        $ training_count = 4
        $ sister.add_event(sis_panty04)
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
