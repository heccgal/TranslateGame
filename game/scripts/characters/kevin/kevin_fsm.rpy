label kevin_triggers_init:
    return

label kevin_machine_init:
    python:
        M_kevin = Machine("kevin", default_loc = [[L_school_cafeteria, L_school_cafeteria, L_NULL, L_NULL]],
                          vars = {"sex speed": .3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
