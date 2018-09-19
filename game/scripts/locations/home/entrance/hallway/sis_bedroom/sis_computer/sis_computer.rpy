label sis_computer:
    if comp_locked == True:
        call expression game.dialog_select("sis_computer_locked")
        if sis_diary_unlocked == False:
            call expression game.dialog_select("sis_computer_locked_diary_locked")
            $ in_sis_room = True
            hide screen sis_computer
            hide screen comp_screen
            jump expression game.dialog_select("sis_bedroom_dialogue")
        else:

            call expression game.dialog_select("sis_computer_locked_diary_unlocked")

    if comp_locked == False and sis_email_04_read == False:
        call expression game.dialog_select("sis_computer_unlocked_unread_email")
    call screen sis_computer

label pass_check:
    if sis_pass.lower().strip() == "bad monster" or sis_pass.lower().strip() == "badmonster":
        scene jenny_comp
        $ comp_locked = False
        if sispc_desktop_seen == False:
            call expression game.dialog_select("sispc_desktop_response")
        $ sispc_desktop_seen = True
    else:

        scene jenny_comp
        show jenny_wrong_pass at Position(xpos=570, ypos= 448) with dissolve
        $ renpy.pause()
        hide jenny_wrong_pass with dissolve
    call screen sis_computer
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
