label maze_minigame_prepare:
    $ A_gamer.unlock()
    call screen maze_scr

label computer_maze_fail:
    hide screen maze_scr
    scene expression "backgrounds/location_computer_minigame03_blur.jpg"
    $ renpy.suspend_rollback(False)
    $ game.timer.tick()
    show popup_bad at truecenter with dissolve
    pause
    hide popup_bad with dissolve
    jump MC_computer

label computer_maze_success:
    hide screen maze_scr
    $ game.timer.tick()
    $ player.stats.increase("int")
    scene expression "backgrounds/location_computer_minigame03b_blur.jpg"
    show popup_good at truecenter with dissolve
    pause
    hide popup_good with dissolve
    hide expression "backgrounds/location_computer_minigame03b_blur.jpg"
    jump MC_computer
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
