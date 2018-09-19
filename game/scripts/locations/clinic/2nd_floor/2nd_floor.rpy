label hospital_second_floor_dialogue:
    $ player.go_to(L_hospital_floor2)
    if mrsj.started(mrsj_sex_ed) and not Roz.completed(roz_storage):
        scene expression game.timer.image("hospital_second{}_b")
        if Roz.started(roz_storage) and player.has_item("hospital_access_card"):
            call expression game.dialog_select("hospital_second_floor_have_access_card")

        elif Roz.started(roz_storage):
            call expression game.dialog_select("hospital_second_floor_roz_storage_started")
        else:

            call expression game.dialog_select("hospital_second_floor_mrsj_sex_ed_started")
        hide player
        with dissolve
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
