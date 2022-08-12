default persistent.CloudBackupLastTime = [None, None, None]

init python:
    # -*- coding: utf-8 -*-
    from ftplib import FTP
    import time,tarfile,os,sys,datetime
    import zipfile
    appdata = os.getenv("APPDATA")
    m_name = persistent._mas_monika_nickname
    p_name = persistent.playername
    savefile = ""

    #连接ftp
    def ftpconnect(host,port, username, password):
        ftp = FTP()
        # 打开调试级别2，显示详细信息
        # ftp.set_debuglevel(2)
        ftp.connect(host, port)
        ftp.login(username, password)
        return ftp
    
    #从ftp下载文件
    def downloadfile(ftp, remotepath, localpath):
        # 设置的缓冲区大小
        bufsize = 1024
        fp = open(localpath, 'wb')
        ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
        ftp.set_debuglevel(0)# 参数为0，关闭调试模式
        fp.close()
    
    #从本地上传文件到ftp
    def uploadfile(ftp, remotepath, localpath):
        bufsize = 1024
        fp = open(localpath, 'rb')
        ftp.storbinary('STOR ' + remotepath, fp, bufsize)
        ftp.set_debuglevel(0)
        fp.close()
    #上传存档文件
    def uploadSave():
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except:
            return False
        if not renpy.android:
            dataDir = os.getenv("APPDATA") + "/RenPy/Monika After Story"
        else:
            dataDir = renpy.config.savedir
        
        #os.rename(dataDir + "/persistent",dataDir + "/persistent")
        uploadfile(ftp,"persistent" ,dataDir + "/persistent")
        #os.rename(dataDir + "/persistent",dataDir + "/persistent")
    
        try:
            ftp.delete(m_name + p_name)
        except Exception as e:
            pass
        ftp.rename("persistent", m_name + "_" + p_name)
        ftp.quit()
        #保存上传的时间
        persistent.CloudBackupLastTime = [datetime.date.today(), datetime.datetime.today(), int(time.time())]
        return True
    
    #下载存档文件
    def downloadSave():
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except:
            return False
        if not renpy.android:
            dataDir = renpy.config.basedir + "/characters"
        else:
            dataDir = "/storage/emulated/0/MAS/characters"
        try:
            downloadfile(ftp, m_name + "_" + p_name, dataDir + "/persistent")
        except TypeError as e:
            renpy.notify("在下载存档时出现了问题")
            mas_submod_utils.submod_log.info("云端存档下载失败：{}".format(e))
        ftp.quit()
        renpy.notify("存档已保存至characters/persistent")
        return True
    
    def downloadOneSave(save):
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except Exception as e:
            mas_submod_utils.submod_log.error("云端备份失败：{}".format(e))
            renpy.show_screen("dp_message","服务器连接失败",Hide("dp_message"))
        if not renpy.android:
            dataDir = renpy.config.basedir + "/characters"
        else:
            dataDir = "/storage/emulated/0/MAS/characters"
        try:
            downloadfile(ftp, save, dataDir + "/persistent")
            renpy.show_screen("dp_message","存档已保存至[renpy.config.basedir]/character",Hide("dp_message"))
        except:
            renpy.show_screen("dp_message","下载失败, 请检查输入名称.",Hide("dp_message"))
            return False
        ftp.quit()
        return True

    def checkSaveTime(debug = False):
        timeD = 0
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except:
            timeD = -2
            return timeD
        try:
            L = list(ftp.sendcmd('MDTM ' + m_name + "_" + p_name))
            ftp.quit()
            dir_t=L[4]+L[5]+L[6]+L[7]+'-'+L[8]+L[9]+'-'+L[10]+L[11]+' '+L[12]+L[13]+':'+L[14]+L[15]+':'+L[16]+L[17]
            timeArray = time.strptime(dir_t, "%Y-%m-%d %H:%M:%S")
            #转换为时间戳:
            timeStamp = int(time.mktime(timeArray)) + 28790
            atime=int(time.time())
            #检查时间差距
            timeD = timeStamp - persistent.CloudBackupLastTime[2]
            if debug == True:
                return dir_t
            if timeD < 0:
                timeD = 0 - timeD
        except:
            timeD = -1
        return timeD

    def FinishEnterSave():
        downloadOneSave(savefile)
        renpy.hide_screen("save_input")

    ################
    #自动备份
    ################

    if persistent.submods_dp_CloudBackup:
        if datetime.datetime.today() != persistent.CloudBackupLastTime[1]:
            mas_submod_utils.submod_log.info("话题包开始备份: 本地 '{}' -> 云端 '{}'".format(datetime.datetime.today(), persistent.CloudBackupLastTime[1]))
            uploadSave()
        else:
            mas_submod_utils.submod_log.info("话题包今日已经备份过，本次不备份：'{}' ".format(persistent.CloudBackupLastTime[1]))


screen dp_cloudSetting():
    python:
        submods_screen_dp = store.renpy.get_screen("submods", "screens").scope["tooltip"]
        _cst = checkSaveTime()
        
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
                        text "每天第一次启动时即会进行一次自动备份. 下载的存档文件位于[renpy.config.basedir]/characters文件夹.\n文件在服务器以'[m_name]_[player]'命名, 请注意是否和其他人重复:)\n自动备份导致的时间戳差距通常在40s左右, 取决于你游戏的启动时间.\n如果下载时出现问题，可以联系qq1951548620帮助恢复存档\n"
                    if _cst == -2:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            text "服务器链接失败!"
                    if _cst == -1:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            text "当前云端没有存档!"
                    elif _cst < 15:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            text "云端文件与本地记录时间戳差距<15s, 可以认为是同一个存档"
                    elif _cst < 60:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            text "云端文件与本地记录时间戳差距小于1分钟, 有与他人重名的可能性"
                    elif _cst < 180:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            text "{b}云端文件与本地记录时间戳差距为1~3分钟, 有与他人重名的可能性{/b}"
                    else:
                        hbox:
                            xpos 20
                            spacing 10
                            xmaximum 780
                            text "{b}{color=#f00}警告:云端文件与本地记录时间戳差距为[checkSaveTime()]s, 有极高与他人重名的可能性!!{/color}{/b}"

                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton "立刻备份":
                            action Function(uploadSave)
                        textbutton "下载备份":
                            action Function(downloadSave)
                        textbutton "下载指定存档":
                            action Show(screen="save_input", message="请输入存档名称, 格式为‘monika的名称_玩家的名称’, 严格区分大小写", ok_action=Function(FinishEnterSave))

            hbox:           
                xalign 0.5
                spacing 100
                textbutton "关闭":
                    action Hide("dp_cloudSetting")

screen save_input(message, ok_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
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

            input default "" value VariableInputValue("savefile") length 25

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action


init -990 python:
    import os
    if not store.mas_submod_utils.isSubmodInstalled("话题整合包"):
        store.mas_submod_utils.Submod(
            author="P",
            name="云端备份",
            description="使用本模组的功能, 即表示你接受将存档文件上传至mas.backup.0721play.icu.\n自动备份依赖于话题整合包(1.14+), 安装它来获取完整功能.",
            version='1.0.0',
            settings_pane="cloudBackup_settingpane"
        )
screen cloudBackup_settingpane():
    vbox:
        xmaximum 800
        xfill True
        style_prefix "check"

        if persistent.submods_dp_gameStatus:
            textbutton ">打开菜单":
                ypos 1
                selected False
                action Show("dp_cloudSetting")

