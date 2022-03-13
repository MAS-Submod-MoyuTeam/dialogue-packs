init -990 python:
    store.mas_submod_utils.Submod(
        author="P",
        name="话题整合包",
        description="包含了一些汉化或编写的话题,原作者请见{a=https://github.com/PencilMario/dialogue-packs/blob/main/README.md}{i}{u}>Github{/a}{/i}{/u}.",
        version='1.11.0',
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

init python:
    import os
    import shutil
    #删除原子模组教学文件夹
    if os.path.exists(renpy.config.basedir + "/game/Submods/MonikaSubmodT"):
        try:
            shutil.rmtree(renpy.config.basedir + "/game/Submods/MonikaSubmodT")
        except:
            raise Exception("delete submod MonikaSubmodT failed\n删除子模组MonikaSubmodT失败,  请手动删除文件夹后重启")
    dp_dirs = os.listdir(renpy.config.basedir + "/game/Submods/Dialogue Packs")

    def dp_showstatus(setting):
        if setting:
            return ">启用中"
        else:
            return ">禁用中"    

##设置项

#游戏更新
default persistent.submods_dp_enableUpdateHelper = True
#新版本对话删除检测 默认启用
default persistent.submods_dp_enableNewVersionDialogueFromdp = True

screen dp_setting_pane():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"


        textbutton ">对话管理(开发中)":
            ypos 1
            selected False
            action Show("dp_manager")
        
        textbutton ">功能设置":
            ypos 1
            selected False
            action Show("dp_setting")

screen dp_manager():
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

                    for dp_dir in dp_dirs:
                        #if dp_dir == "dialogue_pack_head.rpy" or dp_dir == "dialogue_pack_head.rpyc":
                        #    continue
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            text "[dp_dir]"
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            textbutton "√ - 点击禁用"
                            textbutton "查看简介"

                        
            hbox:           
                xalign 0.5
                spacing 100
                textbutton "关闭":
                    action Hide("dp_manager")

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
                xalign 0.5
                spacing 100
                textbutton "关闭":
                    action Hide("dp_setting")





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