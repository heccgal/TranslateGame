label trailer_shack_dialogue:
    $ player.go_to(L_trailer_shack)
    $ game.main()

label trailer_shack_interior_dialogue:
    if L_trailer_shack_interior.locked:
        call expression game.dialog_select("trailer_shack_cant_go_in")
        $ game.main()
    $ player.go_to(L_trailer_shack_interior)
    $ game.main()

label shack_doghouse_dialogue:
    if M_roxxy.is_state(S_roxxy_get_uniform_on_doggo) and not player.has_item("roxxy_uniform"):
        call expression game.dialog_select("shack_doghouse_roxxy_get_uniform_on_doggo")
        $ player.get_item("roxxy_uniform")
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
