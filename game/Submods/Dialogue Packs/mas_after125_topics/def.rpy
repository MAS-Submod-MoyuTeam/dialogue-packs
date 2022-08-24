init -995 python:
    import os
    import shutil
    newversion=["0.12.6","0.12.7","0.12.8", "0.12.9"]
    #假设现在为老版本
    p_is_old_ver = True

    for x in newversion:
        if not persistent.submods_dp_enableNewVersionDialogueFromdp:
            p_is_old_ver = False
            break
        if renpy.config.version == x and not renpy.android:
            p_is_old_ver = False
            if renpy.loadable(renpy.config.basedir + "/game/Submods/Dialogue Packs/mas_after125_topics"):
                try:
                    shutil.rmtree(renpy.config.basedir + "/game/Submods/Dialogue Packs/mas_after125_topics")
                    mas_submod_utils.submod_log.info("[DMR_C] 移除了新版本对话")
                except:
                    mas_submod_utils.submod_log.info("[DMR_C] 移除新版本对话时发生异常")
            break
                   
