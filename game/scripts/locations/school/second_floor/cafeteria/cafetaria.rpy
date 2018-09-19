label cafeteria_dialogue:
    $ player.go_to(L_school_cafeteria)
    call pa_announcement
    if quest09 in quest_list and quest09 not in completed_quests and quest09_1 == False and quest09_2 == False and quest09_3 == False:
        call expression game.dialog_select("cafeteria_milk_delivery")
        $ quest09_1 = True


    elif quest09 in quest_list and quest09 not in completed_quests and quest09_2 == True:
        call expression game.dialog_select("cafeteria_milk_delivery_invoice")
        $ player.remove_item("milk_carton")
        $ quest09_2 = False
        $ quest09_3 = True


    elif not erik.known(erik_favor) and player.location.is_here(M_kevin):
        call expression game.dialog_select("cafeteria_erik_favor_not_known")
        $ erik.add_event(erik_favor)

    elif erik.known(erik_favor) and not erik.completed(erik_favor_2) and player.location.is_here(M_kevin):
        call expression game.dialog_select("cafeteria_erik_favor_known")

    elif player.location.is_here(M_erik) and erik.completed(erik_favor_2):
        call expression game.dialog_select("cafeteria_erik_favor_2_completed")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
