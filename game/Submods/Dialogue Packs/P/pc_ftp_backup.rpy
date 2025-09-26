
default persistent.CloudBackupLastTime = [None] * 3
default persistent.CloudBackupUsingSlot = 0

init python:
    import uuid, base64
    if isinstance(persistent._CloudBackupUUID, uuid.UUID):
        persistent._CloudBackupUUID = str(persistent._CloudBackupUUID)
    if persistent._CloudBackupUUID is None:
        persistent._CloudBackupUUID = str(uuid.uuid1())
    # -*- coding: utf-8 -*-
    from ftplib import FTP
    import time,tarfile,os,sys,datetime
    import zipfile
    appdata = os.getenv("APPDATA")
    newuuid = ""
    m_name = ""
    p_name = ""

    def setName():
        m_name = persistent._mas_monika_nickname
        p_name = persistent.playername
        if (m_name, p_name) != persistent._CloudBackupUsedName:
            persistent._CloudBackupUsedName = (m_name, p_name)
    def nameChanged():
        return (persistent._mas_monika_nickname, persistent.playername) != persistent._CloudBackupUsedName

    setName()
    if persistent._CloudBackupUsedName is None:
        persistent._CloudBackupUsedName = (m_name, p_name)

    def encodeBase64(uuid_str):
        # 移除 UUID 中的横杠
        uuid_str = uuid_str.replace('-', '')
        # 将 UUID 转换为字节
        uuid_bytes = uuid.UUID(uuid_str).bytes
        # 使用 base64 编码
        uuid_base64 = base64.urlsafe_b64encode(uuid_bytes)
        # 去除末尾的等号
        return uuid_base64.decode('utf-8').rstrip('=')
    def decodeBase64(short_uuid):
        # 补全末尾的等号
        short_uuid += '=' * (4 - len(short_uuid) % 4)
        # 解码 base64
        uuid_bytes = base64.urlsafe_b64decode(short_uuid)
        # 转换为 UUID 对象
        return uuid.UUID(bytes=uuid_bytes)
    def getSaveName(base64, slot):
        return "{}_{}_{}_{}".format(base64, persistent._CloudBackupUsedName[0], persistent._CloudBackupUsedName[1], slot)
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

    #删除存档文件
    def delSave(slot = persistent.CloudBackupUsingSlot):
        fname = getSaveName(encodeBase64(str(persistent._CloudBackupUUID)), persistent.CloudBackupUsingSlot)
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except:
            return False
        try:
            ftp.delete(fname)
        except Exception as e:
            pass
        #保存上传的时间
        persistent.CloudBackupLastTime[slot] = None
        return True
    def getAllCloudFiles():
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except Exception as e:
            mas_submod_utils.submod_log.error("获取云端文件列表失败：{}".format(e))
            return []

        try:
            # 获取当前UUID的base64编码
            current_uuid_base64 = encodeBase64(str(persistent._CloudBackupUUID))

            # 获取FTP服务器上的所有文件
            file_list = ftp.nlst()

            # 筛选出以当前UUID base64编码开头的文件
            matching_files = [f for f in file_list if f.startswith(current_uuid_base64)]

            ftp.quit()
            return matching_files
        except Exception as e:
            mas_submod_utils.submod_log.error("获取云端文件列表失败：{}".format(e))
            return []

    #上传存档文件
    def uploadSave():
        fname = getSaveName(encodeBase64(str(persistent._CloudBackupUUID)), persistent.CloudBackupUsingSlot)
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
            ftp.delete(fname)
        except Exception as e:
            pass
        ftp.rename("persistent", fname)
        ftp.quit()
        #保存上传的时间
        persistent.CloudBackupLastTime[persistent.CloudBackupUsingSlot] = datetime.datetime.today()
        return True
    
    #下载存档文件
    def downloadSave(slot):
        fname = getSaveName(encodeBase64(str(persistent._CloudBackupUUID)), slot)
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except Exception as e:
            renpy.show_screen("dp_message","下载存档时出现了问题.{}".format(e),Hide("dp_message"))
            mas_submod_utils.submod_log.error("云端存档下载失败：{}".format(e))
        if not renpy.android:
            dataDir = renpy.config.basedir + "/characters"
        else:
            dataDir = "/storage/emulated/0/MAS/characters"
        try:
            downloadfile(ftp, fname, dataDir + "/persistent")
        except Exception as e:
            renpy.show_screen("dp_message","下载存档时出现了问题.{}".format(e),Hide("dp_message"))
            mas_submod_utils.submod_log.error("云端存档下载失败：{}".format(e))
        ftp.quit()
        renpy.show_screen("dp_message","存档已保存至[renpy.config.basedir]/character",Hide("dp_message"))
        return True
    
    def getCloudSaveTime(afile):
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except:
            return 0, False
        try:
            L = list(ftp.sendcmd('MDTM ' + afile))
            ftp.quit()
            dir_t=L[4]+L[5]+L[6]+L[7]+'-'+L[8]+L[9]+'-'+L[10]+L[11]+' '+L[12]+L[13]+':'+L[14]+L[15]+':'+L[16]+L[17]
            timeArray = time.strptime(dir_t, "%Y-%m-%d %H:%M:%S")
            #转换为时间戳:
            timeStamp = int(time.mktime(timeArray)) + 28790
            return timeStamp, str(datetime.datetime.fromtimestamp(timeStamp))
        except Exception as e:
            mas_submod_utils.submod_log.error("云端备份查询时间失败：{}".format(e))
            return 0, False


    def checkSaveTime(slot = persistent.CloudBackupUsingSlot):
        file = getSaveName(encodeBase64(str(persistent._CloudBackupUUID)), slot)
        return getCloudSaveTime(file)[1]
    def FinishEnterSave(file):
        fname = file
        try:
            ftp = ftpconnect("mas.backup.0721play.icu", 21, "mas_backup_0721play_icu", "3RNNNwYYetBi3LHw")
        except Exception as e:
            renpy.show_screen("dp_message","下载存档时出现了问题.{}".format(e),Hide("dp_message"))
            mas_submod_utils.submod_log.error("云端存档下载失败：{}".format(e))
        if not renpy.android:
            dataDir = renpy.config.basedir + "/characters"
        else:
            dataDir = "/storage/emulated/0/MAS/characters"
        try:
            downloadfile(ftp, fname, dataDir + "/persistent")
        except Exception as e:
            renpy.show_screen("dp_message","下载存档时出现了问题.{}".format(e),Hide("dp_message"))
            mas_submod_utils.submod_log.error("云端存档下载失败：{}".format(e))
        ftp.quit()
        renpy.show_screen("dp_message","存档已保存至[renpy.config.basedir]/character",Hide("dp_message"))
        return True

        renpy.hide_screen("save_input")

    def FinishUUIDSet():
        try:
            if len(store.newuuid) < 32:
                renpy.notify("uuid的长度不正确")
                raise("UUID的长度不正确")
            store.newuuid = uuid.UUID(store.newuuid)
            persistent._CloudBackupUUID = str(store.newuuid)
            renpy.show_screen("dp_message","UUID设置成功",Hide("dp_message"))
        except Exception as e:
            mas_submod_utils.submod_log.info("UUID设置失败:" + str(e))
            renpy.show_screen("dp_message","UUID设置失败，请检查log以获取详细信息.",Hide("dp_message"))
        renpy.hide_screen("uuid_save_input")


    ################
    #自动备份
    ################
    try:
        if persistent.submods_dp_CloudBackup:
            try:
                if datetime.datetime.today().day != persistent.CloudBackupLastTime[persistent.CloudBackupUsingSlot].day:
                    mas_submod_utils.submod_log.info("存档开始云端备份: 上次备份 '{}'".format(persistent.CloudBackupLastTime[persistent.CloudBackupUsingSlot]))
                    persistent.CloudBackupUsingSlot = persistent.CloudBackupUsingSlot + 1 if persistent.CloudBackupUsingSlot + 1 <= 3 - 1 else 0
                    mas_submod_utils.submod_log.info("使用槽位: {}".format(persistent.CloudBackupUsingSlot))
                    uploadSave()
                else:
                    mas_submod_utils.submod_log.info("云端存档今日已经备份过，上次备份：'{}' ".format(persistent.CloudBackupLastTime[persistent.CloudBackupUsingSlot]))
            except:
                mas_submod_utils.submod_log.info("云端存档可能从未备份过，进行备份：'{}'".format(datetime.datetime.today()))
                mas_submod_utils.submod_log.info("使用槽位: {}".format(persistent.CloudBackupUsingSlot))
                uploadSave()
    except Exception as e:
        import traceback
        mas_submod_utils.submod_log.error("云端存档自动备份失败：{}".format(traceback.format_exc()))


screen dp_cloudSetting():
    python:
        submods_screen_dp = store.renpy.get_screen("submods", "screens").scope["tooltip"]
        sfilename = getSaveName(encodeBase64(str(persistent._CloudBackupUUID)), "槽位")
        
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
                        text "每天第一次启动时即会进行一次自动备份. 下载的存档文件位于characters文件夹.\n文件在服务器以'[sfilename]'命名\n如果下载时出现问题，可以联系qq1951548620帮助恢复存档\n云端有三个槽位 0/1/2\n注意: 在存档中使用中文名可能导致无法下载存档"
                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        text "\nUUID: [persistent._CloudBackupUUID]\n牢记此id以用于在其他客户端进行使用"

                    hbox:
                        xpos 20
                        spacing 10
                        xmaximum 780
                        textbutton "立刻备份至槽位[persistent.CloudBackupUsingSlot]":
                            action Function(uploadSave)
                        textbutton "下载备份":
                            action Show(screen="save_input", message="请选择要下载的槽位", ok_action=Function(FinishEnterSave))
                        textbutton "设置UUID":
                            action Show(screen="uuid_save_input", message="请输入UUID, 格式为‘00010203-0405-0607-0809-0a0b0c0d0e0f’, 连字符可省略", ok_action=Function(FinishUUIDSet))

            hbox:           
                xalign 0.5
                spacing 100
                textbutton "关闭":
                    action Hide("dp_cloudSetting")

screen save_input(message, ok_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 225
    python:
        saves = getAllCloudFiles()
        savetimes = {}
        showname = {}
        for file in saves:
            savetimes[file] = getCloudSaveTime(file)[1]
            showname[file] = "{}".format(file).replace(encodeBase64(str(persistent._CloudBackupUUID)), "")[1:]
    style_prefix "confirm"

    frame:
        vbox:
            ymaximum 300
            xmaximum 800
            xfill True
            yfill False
            spacing 5

            hbox:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5

            hbox:
                textbutton "如果这里没有存档, 可点击这里查看所有存档列表":
                    action OpenURL(r"http://sp2.0721play.icu/MAS/%E6%89%A9%E5%B1%95%E5%86%85%E5%AE%B9/Dialogue-Packs%20%E5%AD%98%E6%A1%A3%E4%BA%91%E7%AB%AF%E5%A4%87%E4%BB%BD")

            for item in saves:
                hbox:
                    textbutton "{}".format(showname.get(item, item[21:])):
                        action Function(FinishEnterSave, item)
                    label "上传于 " + savetimes.get(item, "未知")

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action Hide("save_input")

screen uuid_save_input(message, ok_action):
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

            input default "[persistent._CloudBackupUUID]" value VariableInputValue("newuuid") length 40

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

init 990 python:
    def CheckNameChanged():
        if nameChanged():
            for i in range(0, 3):
                delSave(i)
            setName()
            uploadSave()
            mas_submod_utils.submod_log.info("检测到名称修改，删除原先所有存档")

    store.mas_submod_utils.registerFunction('ch30_loop', CheckNameChanged)


label monika_changename_dpov:
    call mas_player_name_enter_name_loop ("你想让我怎么称呼你呢?")
    call monika_changename_finish
    return
label monika_changename_finish:
    return
label monika_affection_nickname_dpov:
    call monika_affection_nickname
    
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

