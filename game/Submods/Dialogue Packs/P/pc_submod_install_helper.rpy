init python:
    import os
    import gzip
    import tarfile
    import shutil
    
    submod_locat = renpy.config.basedir + "/characters"
    
    def check_zip():
        dirs = os.listdir(submod_locat)
        for file_name in dirs:
            if file_name.find('zip') != -1:
                file_name = submod_locat + "/" + file_name
                try:
                    un_zip(file_name)
                except:
                    move_files(file_name,False)
                    raise Exception("Error when decompressing zip file. \n解压zip文件时出现错误.")
                if not copy_dir_m(file_name):#尝试处理文件夹 返回F时抛出异常
                    move_files(file_name,False)
                    raise Exception("The zip file is incorrect, this may mean that the zip file isnot compressed according to the game file directory, please unzip it manually to the specified location.\nzip文件不正确，这可能意味着这个zip文件并没有根据游戏文件目录来压缩，请手动解压至正确位置.")
                move_files(file_name,True)

    def move_files(file_name,result = True):
        """
        结束后的文件处理
        vars:
            file_name - 删除的文件夹
            result - 执行结果
        """
        if result:
            dir = submod_locat + "/Install Success"
        else:
            dir = submod_locat + "/Install Fail"
        if not os.path.exists(dir):
            os.mkdir(dir)
        shutil.rmtree(file_name + "_files")
        shutil.move(file_name ,dir )

    def un_zip(file_name):
        """
        解压文件
        """
        import zipfile
        zip_file = zipfile.ZipFile(file_name)
        if os.path.isdir(file_name + "_files"):
            pass
        else:
            os.mkdir(file_name + "_files")
        for names in zip_file.namelist():
            zip_file.extract(names,file_name + "_files/")
        zip_file.close()

    def copy_dir_m(file_name,inseconddir = False):
        """
        处理文件夹
        vars:
            file_name - 处理的文件夹
            inseconddir - 是否进入了子文件夹
        """
        bak_file_name = None
        if inseconddir == False:
            file_name = file_name + "_files"
            bak_file_name = file_name
        files = os.listdir(file_name)
        for dirs in files:
            if dirs == 'game':
                copy_dir(file_name + "/game" ,renpy.config.basedir + "/game")
                if os.path.exists(file_name + "/game" + "/mod_assets"):
                    #如果存在mod_assets 检查json
                    check_json(file_name + "/game" + "/mod_assets",bak_file_name)
            elif dirs == 'lib':
                copy_dir(file_name + "/lib" ,renpy.config.basedir + "/lib")
            elif dirs == 'log':
                copy_dir(file_name + "/log" ,renpy.config.basedir + "/log")
            elif dirs == 'piano_songs':
                copy_dir(file_name + "/piano_songs" ,renpy.config.basedir + "/piano_songs")
            elif dirs == 'custom_bgm':
                copy_dir(file_name + "/custom_bgm" ,renpy.config.basedir + "/custom_bgm")
            elif dirs == 'characters':
                continue#什么都不做, 我不希望做一个一键解锁精灵包的东西--至少要手动移动文件.
            #game下文件夹
            elif dirs == 'Submods':
                copy_dir(file_name + "/Submods",renpy.config.basedir + "/game/Submods")
            elif dirs == 'mod_assets':
                check_json(file_name + "/mod_assets",bak_file_name)
                copy_dir(file_name + "/mod_assets",renpy.config.basedir + "/game/mod_assets")
            elif dirs == 'python-packages':
                copy_dir(file_name + "/python-packages",renpy.config.basedir + "/game/python-packages")
            elif dirs == 'gui':
                copy_dir(file_name + "/gui",renpy.config.basedir + "/game/gui")
            else:
                if os.path.isfile(file_name + '/' + dirs):
                    continue#这是个文件，直接continue
                if inseconddir:
                    #在子文件夹直接返回F
                    return False
                inseconddir = True
                if not copy_dir_m(file_name + '/' + dirs,inseconddir = True):#说明子文件夹内也没有符合条件文件夹
                    return False
        return True

    def copy_dir(src_path, target_path):
        """
        复制文件 网上找的代码:))))))
        """
        if os.path.isdir(src_path) and os.path.isdir(target_path):        
            filelist_src = os.listdir(src_path)                            
            for file in filelist_src:
                path = os.path.join(os.path.abspath(src_path), file)    
                if os.path.isdir(path):
                    path1 = os.path.join(os.path.abspath(target_path), file)    
                    if not os.path.exists(path1):                        
                        os.mkdir(path1)
                    copy_dir(path,path1)            
                else:                                
                    with open(path, 'rb') as read_stream:
                        contents = read_stream.read()
                        path1 = os.path.join(target_path, file)
                        with open(path1, 'wb') as write_stream:
                            write_stream.write(contents)
            return True    
        else:
            return False 

    def check_json(filename,movedir):
        import json
        """
        用于检查json并生成gift文件
        vars:
            filename - mod_assets文件夹
            movedir - 失败后删除的文件夹
        """
        if not os.path.exists(filename + "/monika/j"):
            return
        filename = filename + "/monika/j"
        files = os.listdir(filename)
        for jsonfile in files:
            if jsonfile.find('json') != -1:
                try:
                    json_file = filename + "/" + jsonfile
                    json_data = open(json_file).read()
                    output_json = json.loads(json_data)
                except:
                    move_files(movedir,False)
                    raise Exception("JSON ERROR:" + json_file + "\n这个json文件存在问题")
                try:
                    giftname = output_json['giftname']
                    if not os.path.exists(renpy.config.basedir + '/AvailableGift'):
                        os.mkdir(renpy.config.basedir + '/AvailableGift')
                    giftfile = open(renpy.config.basedir + '/AvailableGift/' + giftname + '.gift','w')
                    giftfile.close()
                except:
                    continue

    check_zip()
