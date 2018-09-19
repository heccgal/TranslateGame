label helens_locked_room:
    $ player.go_to(L_miahouse_lockedroom)
    if M_mia.is_state(S_mia_locked_room):
        call expression game.dialog_select("helens_locked_room_mia_locked_room")
        $ player.remove_item("key03")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
