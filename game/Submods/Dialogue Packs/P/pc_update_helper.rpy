init python:
    todoDir = [
    "game/Submods",
    "game/python-packages",
    "game/mod_assets/location",
    "game/mod_assets/monika",
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
        shutil.copytree(cDir,tDir)
        return

init 5 python:
    addEvent(
            Event(
                persistent.event_database,          
                eventlabel="sub_update_helper",        
                category=["模组"],                   
                prompt="准备一下更新吧(不稳定,切勿反复使用)",
                pool=True,
                unlocked=True
            )
        )

label sub_update_helper:
    m "好的"
    m "如果未响应, 这是正常情况, 因为在干活要稍微等一下..."
    call copyfile
    m "搞定了. {w=0.3}文件都在character/OldVersionFiles文件夹里, 复制到新版本就好了."
    m "不要复制到新版本的character了, 要去合并新版本game文件夹."
return

label copyfile:
    python:
        import os
        import shutil
        if os.path.exists(renpy.config.basedir + "/characters/OldVersionFiles"):
            shutil.rmtree(renpy.config.basedir + "/characters/OldVersionFiles")
        renpy.pause(0.1)
        createFileBaseDir()
        for lista in todoDir:
            renpy.say(m,"正在复制文件夹{w=0.5}{nw}"+lista)
            copyOldDir(lista)
            
    return