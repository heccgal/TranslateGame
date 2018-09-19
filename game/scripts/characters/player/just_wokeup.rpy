label player_just_wokeup:
    scene expression player.location.background_blur
    if game.timer.is_morning() and not L_home_shower.is_here(M_jenny) and (
            sister.started(sis_webcam01) or
            sister.started(sis_webcam02) or
            sister.started(sis_webcam03) or
            (sister.over(sis_webcam04) and not sis_lastwebcam_show_seen)
            ):
        call expression game.dialog_select("bedroom_sis_webcam_show")

    elif sister.started(sis_telescope01) and (not L_home_shower.is_here(M_jenny) and game.timer.is_morning()):
        call expression game.dialog_select("bedroom_sis_telescope_1")

    elif sister.started(sis_telescope02) and (not L_home_shower.is_here(M_jenny) and game.timer.is_morning()):
        call expression game.dialog_select("bedroom_sis_telescope_2")

    elif sister.started(sis_telescope03) and (not L_home_shower.is_here(M_jenny) and game.timer.is_morning()):
        call expression game.dialog_select("bedroom_sis_telescope_3")

    elif (training_count == 1 and training_tier == 2 and sister.over(sis_shower_cuddle01)) or (training_count == 2 and training_tier == 3 and sister.over(sis_couch02)) or (training_count == 3 and training_tier == 4 and sister.over(sis_couch03)):
        call expression game.dialog_select("bedroom_master_somrak_training")

    if M_mom.is_set("chores"):
        call expression game.dialog_select("bedroom_mom_chores")

    elif M_mom.is_state(S_mom_search_panties):
        call expression game.dialog_select("bedroom_mom_search_panties")

    elif M_mom.is_state(S_mom_kissing_practice):
        call expression game.dialog_select("bedroom_mom_kissing_practice")

    elif M_roxxy.is_state(S_roxxy_spin_bottle) and game.timer == Date(dow="saturday"):
        call expression game.dialog_select("bedroom_roxxy_spin_bottle")
        if not player.has_item("goldschwagger"):
            call expression game.dialog_select("bedroom_roxxy_spin_bottle_no_goldschwagger")
        hide player with dissolve
    $ M_player.set("just wokeup", False)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
