default current_camshow = 1

label MC_computer:
    if game.timer.is_night():
        call expression game.dialog_select("MC_computer_night_locked")
        $ game.main()
    call screen MC_computer

label MC_pass_check:
    if MC_pass.lower().strip() == "cookies":
        scene expression game.timer.image("backgrounds/location_computer_player_01{}.jpg")
        $ MC_comp_locked = False
    else:

        scene expression game.timer.image("backgrounds/location_computer_player_01{}.jpg")
        show jenny_wrong_pass at Position(xpos=570, ypos= 448) with dissolve
        pause
        hide jenny_wrong_pass with dissolve
    call screen MC_computer
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
