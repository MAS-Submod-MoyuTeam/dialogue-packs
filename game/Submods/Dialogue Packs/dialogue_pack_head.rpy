init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="话题整合包",
        description="包含了一些汉化或编写的话题,原作者请见{a=https://github.com/PencilMario/dialogue-packs/blob/main/README.md}{i}{u}>Github{/a}{/i}{/u}.",
        version='1.18.3',
        settings_pane="dp_setting_pane"
    )

init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="话题整合包",
            user_name="PencilMario",
            repository_name="dialogue-packs",
            update_dir="",
            attachment_id=None
        )

init -900 python:
    import os
    import shutil
    try:
        #删除原子模组教学文件夹
        if os.path.exists(renpy.config.basedir + "/game/Submods/MonikaSubmodT"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/MonikaSubmodT")
        if os.path.exists(renpy.config.basedir + "/game/Submods/MoreTopic"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/MoreTopic")
        #删除DaN子模组
        if os.path.exists(renpy.config.basedir + "/game/Submods/Dialogue Packs/DrakeTheDuelist"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Dialogue Packs/DrakeTheDuelist")
        #删除原钢琴对话子模组
        if os.path.exists(renpy.config.basedir + "/game/Submods/Custom Postpiano"):
            shutil.rmtree(renpy.config.basedir + "/game/Submods/Custom Postpiano")
    except:
        pass

    def dp_showstatus(setting):
        if setting:
            return ">启用中"
        else:
            return ">禁用中"    
    dp_authors = """\
    以下为作者和汉化者名单, 排名不分先后:\n
    JmDemisana, ThePersonYou_Hate,{a=https://www.reddit.com/user/mayday-mayjay/}mayday-mayday{/a},{a=https://www.reddit.com/user/UnexplainedYeet}UnexplainedYeet{/a},{a=https://www.reddit.com/user/ryuujjy/}ryuujjy{/a},{a=https://www.reddit.com/user/geneTechnician/}geneTechniman{/a},{a=https://www.reddit.com/user/mkam23-Maya/}mkam23-maya{/a},TK,Sir.P,星光,莫秋纱,{a=https://github.com/DrakeTheDuelist}DrakeTheDuelist{/a},Mon-ika,{a=https://www.reddit.com/user/AmyKawa}AmyKawa{/a},ddy,Founxious\n
    因为个人精力有限, 如果本子模组内有您的作品却没有注明您的名字, 请及时与{a=https://github.com/PencilMario/dialogue-packs}我{/a}告知.
    """
    if renpy.android:
        #为PE声明未包含的方法
        def mas_progressionDataDump():
            """
            Dumps progression data as a string
            """
            return (
                "Last XP rate reset: {0}\n"
                "Hours spent today: {1}\n"
                "XP to next level: {2}\n"
                "Current level: {3}\n"
                "Current xp rate: {4}\n"
                "XP last granted: {5}\n\n"
            ).format(
                persistent._mas_xp_rst,
                persistent._mas_xp_hrx,
                persistent._mas_xp_tnl,
                persistent._mas_xp_lvl,
                mas_xp.xp_rate,
                mas_xp.prev_grant,
            )
        def mas_sessionDataDump():
            """
            Dumps session data as a string
            """
            if persistent.sessions is None:
                return "No session data found."
    
            # grab each data element
            first_sesh = persistent.sessions.get("first_session", "N/A")
            total_sesh = persistent.sessions.get("total_sessions", None)
            curr_sesh_st = persistent.sessions.get("current_session_start", "N/A")
            total_playtime = persistent.sessions.get("total_playtime", None)
            last_sesh_ed = persistent.sessions.get("last_session_end", "N/A")
    
            if total_sesh and total_playtime is not None:
                avg_sesh = total_playtime / total_sesh
    
            else:
                avg_sesh = "N/A"
    
            # which ones do we actually have
            def cts(sesh):
                if sesh is None:
                    return "N/A"
    
                return sesh
    
    
            # assemble output
            output = [
                first_sesh,
                cts(total_sesh),
                cts(total_playtime),
                avg_sesh,
                curr_sesh_st,
                last_sesh_ed
            ]
    
            # NOTE: curr_sesh_st -> last session start because it gets updated
            # during ch30
            outstr = (
                "First session: {0}\n" +
                "Total sessions: {1}\n" +
                "Total playtime: {2}\n" +
                "Avg playtime per session: {3}\n" +
                "Last session start: {4}\n" +
                "Last session end: {5}\n\n"
            )
    
            return outstr.format(*output)

##设置项

#游戏更新
default persistent.submods_dp_enableUpdateHelper = True
#新版本对话删除检测 默认启用
default persistent.submods_dp_enableNewVersionDialogueFromdp = True
#在选项里显示游戏数据
default persistent.submods_dp_gameStatus = False
#云备份
default persistent.submods_dp_CloudBackup = False
#离别对话
default persistent.submods_dp_Leave = False

screen dp_setting_pane():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"

        if persistent.submods_dp_gameStatus:
            textbutton ">游戏统计":
                ypos 1
                selected False
                action Show("dp_gameStatus")
        
        textbutton ">功能设置":
            ypos 1
            selected False
            action Show("dp_setting")
        
        textbutton ">特别感谢":
            ypos 1
            selected False
            action Show(screen = "dialog", message = dp_authors, ok_action = Hide("dialog"))

        if persistent.submods_dp_CloudBackup:
            textbutton ">云端备份":
                ypos 1
                selected False
                action Show("dp_cloudSetting")
            
screen dp_gameStatus():
    key "noshift_T" action NullAction()
    key "noshift_t" action NullAction()
    key "noshift_M" action NullAction()
    key "noshift_m" action NullAction()
    key "noshift_P" action NullAction()
    key "noshift_p" action NullAction()
    key "noshift_E" action NullAction()
    key "noshift_e" action NullAction()

    modal True

    zorder 200

    style_prefix "check"
    add mas_getTimeFile("gui/overlay/confirm.png")

    frame:
        vbox:
            ymaximum 300
            xmaximum 800
            xfill True
            yfill False
            spacing 5

            viewport:
                id "viewport"
                scrollbars "vertical"
                ymaximum 250
                xmaximum 780
                xfill True
                yfill False
                mousewheel True
                
                vbox:
                    xmaximum 780
                    xfill True
                    yfill False
                    box_wrap False

                    hbox:
                        text "Current Affection:[_mas_getAffection()]\n"
                    hbox:
                        text "[mas_progressionDataDump()][mas_sessionDataDump()]"
                    hbox:
                        text "共计上限次数:[store.mas_games._total_games_played()]"
                    hbox:
                        text "上次云端备份时间:[persistent.CloudBackupLastTime[1]]"
                    hbox:
                        text "验证云端文件时间差:[checkSaveTime()]s"

                    if not renpy.android:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "创建完整的 ev_dump.log":
                                action Jump("create_evdump")
                    else:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "创建完整的 ev_dump.log (不可用 - PE版本)"
                    
                    if _mas_getAffection() <= 100:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "打开发型切换界面 (需要 100+ 好感)"
                    else:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "打开发型切换界面":
                                action Jump("unlockHairChange")

                    if _mas_getAffection() <= 100:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "打开衣服切换界面 (需要 100+ 好感)"
                    else:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "打开衣服切换界面":
                                action Jump("unlockClothesChange")

                    if not renpy.android:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "尝试创建所有礼物文件":
                                action Jump("createAllGiftFile")
                    else:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "尝试创建所有礼物文件(不可用 - PE版本)"

                        
            hbox:           
                xalign 0.5
                spacing 100
                textbutton "关闭":
                    action Hide("dp_gameStatus")

screen dp_setting():
    python:
        submods_screen_dp = store.renpy.get_screen("submods", "screens").scope["tooltip"]
        
    key "noshift_T" action NullAction()
    key "noshift_t" action NullAction()
    key "noshift_M" action NullAction()
    key "noshift_m" action NullAction()
    key "noshift_P" action NullAction()
    key "noshift_p" action NullAction()
    key "noshift_E" action NullAction()
    key "noshift_e" action NullAction()

    modal True

    zorder 200

    style_prefix "confirm"
    add mas_getTimeFile("gui/overlay/confirm.png")

    frame:
        vbox:
            ymaximum 300
            xmaximum 800
            xfill True
            yfill False
            spacing 5

            viewport:
                id "viewport"
                scrollbars "vertical"
                ymaximum 250
                xmaximum 780
                xfill True
                yfill False
                mousewheel True
                
                vbox:
                    xmaximum 780
                    xfill True
                    yfill False
                    box_wrap False

                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        text "\"辅助更新\"话题"
                        textbutton "[dp_showstatus(persistent.submods_dp_enableUpdateHelper)]":
                            selected False
                            action NullAction()
                        
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton _("启用"):
                            action Jump("show_sub_update_helper")
                        textbutton _("禁用"):
                            action Jump("hide_sub_update_helper")
                        textbutton _("?"):
                            action Show(screen = "dialog", message = "即话题“准备一下更新吧”.此功能面向于PC, 对手机无用.", ok_action = Hide("dialog"))
                    
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        text "新版本话题解锁检测"
                        textbutton "[dp_showstatus(persistent.submods_dp_enableNewVersionDialogueFromdp)]":
                            selected False
                            action NullAction()
                        
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton _("启用"):
                            action Jump("enableNewVersionDialogueFromdp")
                        textbutton _("禁用"):
                            action Jump("disableNewVersionDialogueFromdp")
                        textbutton _("?"):
                            action Show(screen = "dialog", message = "本模组会为0.12.5及以前版本提供新版本的话题.\n在0.12.6及以后本模组将会自动删除相关脚本文件.\n禁用后, 不再检测并删除文件, 也不会重新恢复脚本文件. 可能会导致意料之外的问题.\n如果已删除, 禁用该选项且更新子模组可恢复文件.\n该选项对手机版无实际作用.", ok_action = Hide("dialog"))

                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        text "游戏统计"
                        textbutton "[dp_showstatus(persistent.submods_dp_gameStatus)]":
                            selected False
                            action NullAction()
                        
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton _("启用"):
                            action Jump("enableGameStatus")
                        textbutton _("禁用"):
                            action Jump("disableGameStatus")
                        textbutton _("?"):
                            action Show(screen = "dialog", message = "在本模组的设置项展示游戏统计", ok_action = Hide("dialog"))

                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        text "云备份"
                        textbutton "[dp_showstatus(persistent.submods_dp_CloudBackup)]":
                            selected False
                            action NullAction()
                        
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton _("启用"):
                            action Jump("enableCloudBackup")
                        textbutton _("禁用"):
                            action Jump("disableCloudBackup")
                        textbutton _("?"):
                            action Show(screen = "dialog", message = "启用云同步即表示你允许本模组将存档文件上传至mas.backup.0721play.icu\nPE无法链接至服务器", ok_action = Hide("dialog"))
                    
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        text "最终告别(务必看按钮说明)"
                        textbutton "[dp_showstatus(persistent.submods_dp_Leave)]":
                            selected False
                            action NullAction()
                        
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton _("启用"):
                            action Jump("enableLeave")
                        textbutton _("禁用"):
                            action Jump("disableLeave")
                        textbutton _("?"):
                            action Show(screen = "dialog", message = "影响话题是否被初始化, 重启生效。\n本话题为我个人写的badend。\n启用可能会导致{b}无法挽回的删除存档{/b}。\n触发方式为连续点击三次‘我想走了’话题，并且在接下来的选项中选择‘抱歉...’。\n公开本话题内容将按{b}粉信{/b}处理。\n在启用前，请反省自己是否要确定离开。", ok_action = Hide("dialog"))


          
            hbox:           
                xalign 0.5
                spacing 100
                textbutton "关闭":
                    action Hide("dp_setting")


screen dp_message(message, ok_action):
    ## Ensure other screens do not get input while this screen is displayed.
    zorder 225

    style_prefix "confirm"

    frame:
        vbox:
            ymaximum 300
            xmaximum 800
            xfill True
            yfill False
            spacing 5

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            #input default "" value VariableInputValue("savefile") length 25

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action



label show_sub_update_helper:
    $ mas_showEVL("sub_update_helper", "EVE", unlock=True, _pool=True)
    $ persistent.submods_dp_enableUpdateHelper = True
    return
label hide_sub_update_helper:
    $ mas_hideEVL("sub_update_helper","EVE",lock=True,depool=True)
    $ persistent.submods_dp_enableUpdateHelper = False
    return

label enableNewVersionDialogueFromdp:
    $ persistent.submods_dp_enableNewVersionDialogueFromdp = True
    return
label disableNewVersionDialogueFromdp:
    $ persistent.submods_dp_enableNewVersionDialogueFromdp = False
    return

label enableCloudBackup:
    $ persistent.submods_dp_CloudBackup = True
    return
label disableCloudBackup:
    $ persistent.submods_dp_CloudBackup = False
    return

label enableGameStatus:
    $ persistent.submods_dp_gameStatus = True
    return
label disableGameStatus:
    $ persistent.submods_dp_gameStatus = False
    return

label enableLeave:
    $ persistent.submods_dp_Leave = True
    return
label disableLeave:
    $ persistent.submods_dp_Leave = False
    return


label create_evdump:
    if renpy.android:
        "Fail"
        return
    $ mas_unstableDataDump()
    "OK"
    return

label unlockHairChange:
    jump monika_hair_select
    return

label unlockClothesChange:
    jump monika_clothes_select
    return

label createAllGiftFile:
    python:
        check_json(renpy.config.basedir + "/game/mod_assets",None)
    return
