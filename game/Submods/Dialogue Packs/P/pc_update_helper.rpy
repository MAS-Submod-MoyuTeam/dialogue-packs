init python:
    todoDir = [
    "game/Submods",
    "game/python-packages",
    "game/mod_assets/location",
    "game/mod_assets/monika/a",
    "game/mod_assets/monika/b",
    "game/mod_assets/monika/c",
    "game/mod_assets/monika/cg",
    "game/mod_assets/monika/f",
    "game/mod_assets/monika/h",
    "game/mod_assets/monika/j",
    "game/mod_assets/monika/t",
    "game/mod_assets/thumbs",
    "game/mod_assets/font",
    "piano_songs",
    "lib",
    "log",
    "custom_bgm"]
    import os
    import shutil
    subUBasedir = renpy.config.basedir + "/characters/OldVersionFiles"
    def createFileBaseDir():
        #创建基础文件夹
        if os.path.exists(subUBasedir):
            os.makedirs(subUBasedir)
    def createFileDir(dir):
        #建立对应的文件夹
        cDir = subUBasedir + "/" +dir
        if os.path.exists(cDir):
            os.makedirs(cDir)
    def copyOldDir(dir):
        #复制文件
        cDir = renpy.config.basedir + "/" + dir
        tDir = subUBasedir + "/" + dir
        if os.path.exists(cDir):
            shutil.copytree(cDir,tDir)
        return
    def zipFiles():
        import zipfile
        dir_name = renpy.config.basedir + "/characters/OldVersionFiles"
        zip_file = renpy.config.basedir + "/characters/OldVersionFiles.zip"
        zip = zipfile.ZipFile(zip_file, 'w') 
        zip.write(dir_name,compress_type = zipfile.ZIP_DEFLATED)
        zip.close()


init 5 python:
    addEvent(
            Event(
                persistent.event_database,          
                eventlabel="sub_update_helper",        
                category=["模组"],                   
                prompt="准备一下更新吧",
                conditional="not renpy.android",
                action=EV_ACT_UNLOCK,
                pool=True
            )
        )

label sub_update_helper:
    m 1eua "好的"
    m 3eka "如果未响应, 这是正常情况, 因为在干活要稍微等一下..."
    #m "你想让我为你打包一下文件吗?{nw}"
    $ create_zip = False
    call copyfile
    m 4eub "搞定了. {w=0.3}文件都在character/OldVersionFiles文件夹里, 复制到新版本就好了."
    m 3eua "不要复制到新版本的character了, 要去合并新版本game文件夹."
return

label copyfile:
    python:
        import os
        import shutil
        if os.path.exists(renpy.config.basedir + "/characters/OldVersionFiles"):
            renpy.say(m,"你要先删除原来的OldVersionFiles文件夹才能继续, [player]...")
            renpy.jump("spemptylabel")
        renpy.pause(0.1)
        createFileBaseDir()
        for lista in todoDir:
            renpy.say(m,"[todoDir.index(lista)+1]/[len(todoDir)] | 正在复制文件夹:"+lista+"{fast}{nw}")
            copyOldDir(lista)
        if create_zip:
            renpy.say(m,"正在压缩文件{fast}{nw}")
            zipFiles()
            renpy.say(m,"正在删除临时文件{fast}{nw}")
            shutil.rmtree(renpy.config.basedir + "/characters/OldVersionFiles")
    return

label spemptylabel:
    pass
    return