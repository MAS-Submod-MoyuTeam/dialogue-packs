init -100 python in mas_sprites:
    EXP_C_WET = "wet"
    EXP_C_BRS = "bare-right-shoulder"
    EXP_H_WET = "wet"
init -2 python in mas_sprites:
    def _hair_wet_entry(_moni_chr, **kwargs):
        """
        Entry prog point for wet hair
        """
        # We remove ahoge as it doesn't make sense on wet hair
        # We don't restore it on hair change either
        _moni_chr._set_ahoge(None)
    def _clothes_bath_towel_white_entry(_moni_chr, **kwargs):
        """
        Entry prog point for bath towel
        """
        outfit_mode = kwargs.get("outfit_mode", False)

        if outfit_mode:
            _moni_chr.change_hair(store.mas_hair_wet, by_user=False)
        # Always add water drops, otherwise why would you wear a towel
        _moni_chr.wear_acs(store.mas_acs_water_drops)

    def _clothes_bath_towel_white_exit(_moni_chr, **kwargs):
        """
        Exit prog point for bath towel
        """
        # Remove water drops
        _moni_chr.remove_acs(store.mas_acs_water_drops)
init -1 python:
    ### WET HAIR
    ## wet
    # Wet hairdown (this isn't selectable by user)
    # Thanks Orca/Briar/Mocca
    mas_hair_wet = MASHair(
        "wet",
        "wet",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        ex_props={
            store.mas_sprites.EXP_H_RQCP: [store.mas_sprites.EXP_C_WET, store.mas_sprites.EXP_C_BRS],
            store.mas_sprites.EXP_H_NT: True,
            store.mas_sprites.EXP_H_WET: True
        },
        entry_pp=store.mas_sprites._hair_wet_entry
    )
    if p_is_old_ver:
        store.mas_sprites.init_hair(mas_hair_wet)

    mas_clothes_bath_towel_white = MASClothes(
        "bath_towel_white",
        "bath_towel_white",
        MASPoseMap(
            default=True,
            use_reg_for_l=True
        ),
        stay_on_start=True,
        ex_props={
            store.mas_sprites.EXP_C_BRS: True,
            store.mas_sprites.EXP_C_WET: True
        },
        entry_pp=store.mas_sprites._clothes_bath_towel_white_entry,
        exit_pp=store.mas_sprites._clothes_bath_towel_white_exit,
        pose_arms=MASPoseArms({}, def_base=False)
    )
    if p_is_old_ver:
        store.mas_sprites.init_clothes(mas_clothes_bath_towel_white)

    mas_acs_water_drops = MASAccessory(
        "water_drops",
        "water_drops",
        MASPoseMap(
            default="0",
            p5="5"
        ),
        acs_type="water-drops",
        priority=1,
        stay_on_start=True,
        rec_layer=MASMonika.MAB_ACS,
    )
    if p_is_old_ver:
        store.mas_sprites.init_acs(mas_acs_water_drops)
