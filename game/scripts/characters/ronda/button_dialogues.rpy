label ronda_dialogue_intro:
    scene gym
    show ronda 2 at right
    show player 36 at left
    with dissolve
    player_name "Hey, {b}Ronda{/b}. How are you?"
    show player 13 with dissolve
    show ronda 3
    ron "I'm doing fine. The question is have you been training?"
    show ronda 2
    show player 11
    player_name "..."
    show player 10
    player_name "No-"
    show player 11
    show ronda 4
    ron "Then stop moving those lips and start moving those... legs!"
    show ronda 2
    show player 34
    player_name "???"
    show ronda 3
    ron "Nevermind. It's just something my dad always says..."
    show player 5
    ron "Anyway, you better hurry up cause the trials are coming up fast!"
    show ronda 2
    return

label ronda_dialogue_talent_show_help:
    show player 10
    player_name "I don't suppose you'd be interested in volunteering for {b}Ms. Dewitt's{/b} musical talent show?"
    show player 5
    show ronda 3
    ron "Musical Talent? No, I would not be interested."
    show ronda 2
    show player 10
    player_name "Are you sure? You don't play any instruments or sing at all?"
    show player 5
    show ronda 3
    ron "Umm, can't you see I have more important things to focus on. Like track and swimming..."
    ron "Stuff you should be focusing on as well!"
    ron "You're never gonna make the team if you keep ignoring your training!"
    show ronda 2
    show player 30
    player_name "You know, there's more to life than sports, {b}Ronda{/b}..."
    show player 5
    show ronda 3
    ron "Pfft, yeah right."
    return

label ronda_dialogue_model_help:
    show player 2 at left
    show ronda 2 at right
    player_name "I'm working on a project for {b}Miss Ross{/b} and it requires a live model."
    player_name "Would you be interested?"
    show player 1
    show ronda 3
    ron "Busy."
    show player 10
    show ronda 2
    player_name "Busy?"
    player_name "Doing what?"
    show player 11
    show ronda 4
    ron "For real, {b}[firstname]{/b}?!"
    ron "I've gotta run 6 miles and hit an ice bath before soccer practice."
    show player 10
    show ronda 1
    player_name "Uhh..."
    show player 11
    show ronda 4
    ron "Afterwards, I've only got 40 minutes to get some laps in before the pool closes."
    show player 10
    show ronda 1
    player_name "That's cra-"
    show player 11
    show ronda 4
    ron "Then it's back home to a heating pad and crunches."
    show player 12
    show ronda 1
    player_name "OKAY! Okay! I got it..."
    hide ronda
    hide player
    show player 12
    with dissolve
    player_name "That girl is insane!"
    return

label ronda_dialogue_leave:
    show player 10
    player_name "Alright."
    player_name "See you later."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
