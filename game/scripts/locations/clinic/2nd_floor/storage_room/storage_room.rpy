label hospital_storage_room_dialogue:
    if M_roz.is_set("fun time"):
        jump expression game.dialog_select("roz_storage_sex")

    elif not player.has_item("hospital_access_card"):
        call expression game.dialog_select("hospital_storage_no_access_card")
        if not Roz.known(roz_storage):
            $ Roz.add_event(roz_storage)
        $ game.main()
    $ player.go_to(L_hospital_storageroom)
    $ roz_trick.finish()
    $ M_roz.unforce()
    $ roz_storage.finish()
    $ game.main()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
