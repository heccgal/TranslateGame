label earl_triggers_init:
    return

label earl_fsm_init:
    return

label earl_machine_init:
    python:
        M_earl = Machine("earl", default_loc = [[L_police_office, L_police_office, L_police_office, L_NULL]],
                         vars = {'sex speed': .3},
        )
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
