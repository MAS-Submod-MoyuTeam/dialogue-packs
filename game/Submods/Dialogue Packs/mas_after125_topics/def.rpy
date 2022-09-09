init -995 python:
    import os
    import shutil
    DP_NEW_VERSION=[0, 12, 5]
    splitver = renpy.config.version.split('.')
    DP_CURR_VERSION = [splitver[0], splitver[1], splitver[2]]
    p_is_old_ver = store.mas_utils.compareVersionLists(DP_CURR_VERSION, DP_NEW_VERSION) == -1
    #-1 0 1

    if not p_is_old_ver:
        if renpy.loadable(renpy.config.basedir + "/game/Submods/Dialogue Packs/mas_after125_topics"):
            try:
                shutil.rmtree(renpy.config.basedir + "/game/Submods/Dialogue Packs/mas_after125_topics")
                mas_submod_utils.submod_log.info("[DMR_C] 移除了新版本对话")
            except:
                mas_submod_utils.submod_log.info("[DMR_C] 移除新版本对话时发生异常")

                   
