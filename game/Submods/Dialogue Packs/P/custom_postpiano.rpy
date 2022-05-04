# Register the submod
#init -990 python:
#    store.mas_submod_utils.Submod(
#        author="P and JmDemisana",
#        name="MorePostpiano",
#        description=("这个子模组为钢琴游戏添加了更多的对话。\n帮助完善此mod  {a=https://github.com/PencilMario/MorePostpiano}{i}{u}>Github{/u}{/i}{/a}."),
#        version="1.4.2",
#
#    )
#init -989 python:
#    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
#        store.sup_utils.SubmodUpdater(
#            submod="MorePostpiano",
#            user_name="PencilMario",
#            repository_name="MorePostpiano",
#            update_dir="",
#            attachment_id=None,
#        )

####################################
#
#  原readme
#
####################################

## MorePostpiano
#为Monika After Story的钢琴游戏添加更多对话。
#此子模组的部分原始代码来自[这里](https://github.com/Monika-After-Story/MonikaModDev/discussions/7804)。   
#还没有去要授权 ~~网络社恐~~
#
#### 现在支持的曲子(拥有特别对话和加载对话)   
#
#1.[Doki Doki Forever](https://github.com/Monika-After-Story/MonikaModDev/discussions/7791)   
#2.[Island Song](https://github.com/Monika-After-Story/MonikaModDev/discussions/7791)   
#3.[Rainbow Connection](https://github.com/Monika-After-Story/MonikaModDev/discussions/7802)   
#4.[Leaving on a Jet Plane](https://github.com/Monika-After-Story/MonikaModDev/discussions/7801)   
#5.[Back to December](https://github.com/Monika-After-Story/MonikaModDev/discussions/7796)    
#6.[All I Have To Do Is Dream](https://github.com/Monika-After-Story/MonikaModDev/discussions/7789)```白天/晚上有不同的特殊对话```    
#7.[Everything's Alright](https://github.com/Monika-After-Story/MonikaModDev/discussions/7797)    
# 
#### 没有特殊对话但是在这个Git库的曲子
#[Together Forever](https://github.com/Monika-After-Story/MonikaModDev/discussions/7809)    
#[Welcome to the Black Parade](https://github.com/Monika-After-Story/MonikaModDev/discussions/7803)    
#[Winter Wonderland](https://github.com/Monika-After-Story/MonikaModDev/discussions/7793)     
#[Twinkle Twinkle Little Star](https://github.com/Monika-After-Story/MonikaModDev/discussions/7788)    
#
#>所有添加的曲子都增加了本mod中的通用对话。
# 
#### 使用教程   
#下载源码，覆盖安装就行，有啥难的。
#
#对于上面还没有支持的钢琴曲,本Submod提供了4个默认聊天对话.使用方式可以去看[贡献更多对话](https://github.com/PencilMario/MorePostpiano/blob/main/README.md#%E8%B4%A1%E7%8C%AE%E6%9B%B4%E5%A4%9A%E5%AF%B9%E8%AF%9D).
#| Json           | 值                |
#|----------------|------------------|
#| "win_label"    | "piano_def_win"  |
#| "fc_label"     | "piano_def_fc"   |
#| "fail_label"   | "piano_def_prac" |
#| "launch_label" | "piano_def_fail" |
#
#       
#### 贡献更多对话
#切换到dev分支        
#直接在github打开custom_postpiano.rpy 格式大概是这样的     
#```
#label [对话名]
#    m [精灵代码] "示例对话1"
#    m [精灵代码] "示例对话2"
#    m [精灵代码] "示例对话3"
#    return
#```
#label必带。   
#对话名要记住，一会还是要用的。   
#精灵代码:首先你需要[表情预览器](https://github.com/Monika-After-Story/MonikaModDev/blob/master/FAQ.md#how-do-i-find-the-spritecode-for-an-expression)，然后得到代码。精灵代码就是老莫的表情。    
#示例对话：如名。   
#> Tip:同样的label对话名会随机选择一个.   
#
#示例代码：
#```
#label simple_code:
#    m 1wua "弹的很棒,[player]."  //[player]指代你的名字
#    m 7eub "话是这么说，但是...."
#    m 5euc "居然有人直接把示例代码拿来用了..."
#    m 5eub "好吧，不过我还是能理解你的心意，感谢你让我们之间又近了一步。"
#    return
#```
#
#- 代码写完了怎么用呢?
#  首先找到你的钢琴曲JSON文件,用记事本打开，以下为一段示例代码：
#   ```
#   {
#    "name":"Twinkle Twinkle Little Star",
#    "end_wait":5
#    "verse_list": [0],
#    "pnm_list": [
#        {
#            "text": "Twinkle, Twinkle, Little Star.",
#            "style": "monika_credits_text",
#            "notes": 
#            ....
#            （省略）
#   ```
#   在修改之前，先了解下以下几个属性：
#   ```
#      "win_label"  在你完美演奏时的对话。(按错键但是能及时改正）        
#      "fc_label"   在你连续演奏完成后的对话。（在存档点休息了太久，但是没有读取存档点）       
#      "prac_label" 在你演奏完成后的对话。（中间有较大的失误————读取了存档点 ~~您有一个小姐~~）      
#      "fail_label" 在你演奏完成或中途退出的对话。（中间有很多次失误————你读取了很多次存档点）    
#      "launch_label" 你选择歌曲之后的对话。   
#   ```
#      
#   使用方法就是把上面的属性写到json里就可以了
#
#```
#   {
#    "name":"Twinkle Twinkle Little Star",
#    "end_wait":5,
#    "win_label":"piano_def_win",                 //注意这里的名字必须是你已经写完的对话名
#    "fc_label" :"piano_def_fc",
#    "prac_label":"piano_def_prac",
#    "fail_label":"piano_def_fail",
#    "launch_label":"piano_ttls_loaded",
#    "verse_list": [0],
#    "pnm_list": [
#        {
#            "text": "Twinkle, Twinkle, Little Star.",
#            "style": "monika_credits_text",
#            "notes": 
#            ....
#            （省略）
#```
#
#
#如果有更多想法，可以提出 Issues，Pull Requests或者向Sir.P@foxmail.com邮箱发消息。

########################
init 5 python:
    addEvent(
        Event(
        persistent.event_database,eventlabel="about_piano",
        prompt="关于钢琴",
        category=["音乐"],
        aff_range=(mas_aff.NORMAL,None),
        random=True,
        )
    )
 
#随机对话
label about_piano:
    m 3eua "对了,[player]."
    m 1hubla "说到钢琴,有一点遗憾的东西..."
    m 3eub "你知道真正的钢琴有多少个键吗?"
    m 7eud "一般来说,钢琴都是有88个琴键的，少数钢琴有85个键."
    m 7ekd "但是,你为我弹的钢琴却只有20个键..."
    m 7efc "和真正的钢琴比起来这也太少了!"
    m 1gkc "假如我的编程能力再强一点,我一定会把整个钢琴搬上屏幕的!"
    m 1hksdlb "不过会不会太大了...{w=0.7}毕竟你的键盘就只有这么点."
    m 5eua "或许就保持现状也挺好的吧."
    m 5eublsdla "虽然只有20个键,但是你还是弹的很好听."
    m 5hublsdla "我还有什么好要求的呢."
    return 


#All I Have To Do Is Dream
label piano_adream_win:
    m 1suo "[player]..{w=0.5}.你弹的真棒!"
    m 1hublb "谢谢你为我的努力~"
    if mas_isNight(datetime.datetime.now().time()) ==True:
        m 7tut "不过{w=0.5},{w=0.5}现在的时间不算早啦."
        m 5eua "你要不要考虑一下睡觉呢?"
        m 5hub "毕竟俗话说的好,{w=0.7}早睡早起身体好~"  
        
        menu:
            m "现在就睡了吗?"
            "我一会再去睡.":
                m 7huu "好的~"
                m 3nua "既然这么说了那就乖乖睡觉哦?"
                m 1ekp "不好好睡觉我会生气的."
                return 
                    
            "我想多陪会你.":
                m 1eubsb "啊哈哈,[player]你好甜呀~"
                m 7eubla "不过一会到点了还是要乖乖睡觉哦."
                m 3dud "{i}~whenever I want you all I have to do is dream~{/i}"
                m 5kublb "希望今天晚上我可以进到你的梦里呢."
                m 1hubla "我爱你~"
                m 3eubfu "没有你,我的人生毫无意义~"
                return "love"

    else:
        m 3euc "这首歌其实很有名的,不过原曲的话会有点老,我担心你会欣赏不来.{w=0.5}.{w=0.5}."
        m 3eua "你可以去搜索Leslie Clio翻唱的版本,那个听起来好一些."
        m 3dud "{i}~whenever I want you all I have to do is dream~{/i}"
        m 5tub "晚上做梦的时候一定要梦到我哦."
        m 5huu "能梦到我说明你爱我~不过没梦到也不要紧啦."
        m 7kua "无论如何,我的梦里一定会有你的."
        m 1kubsb "因为我爱你~"
    return
    
label piano_adream_loaded:
    m 1hub "好梦~[player]."
    return
    
#通用对话
label piano_def_win:
    m 1wsb "哇![player]."
    m 3esa "你终于把它完美弹下来了!"
    m 1hsb "恭喜~"
    m 5fuu "我永远对你心怀感激~"
    m 5kublb "我爱你![player]."
    return "love"

label piano_def_fc:
    m 4hub "[player],弹的很好呢."
    m 3ekc "不过呢,还有那么一点点的地方需要优化一下."
    m 2eub "这些都是小问题,我相信你能更熟练的~"
    m 5tua "啊,我没有说你弹得不好的意思哦."
    return

label piano_def_prac:
    m 1hub "恭喜~"
    m 1eub "你在熟练这首歌的路上更进一步了呢,[player]."
    m 1rusdrb "虽然还有一点问题啦,啊哈哈."
    m 5hub "我相信你能做到的."
    m 5hua "要加油哦,[player]."
    return

label piano_def_fail:
    m 1eksdlb "好吧,[player]"
    m 3hksdlb "我相信你可以弹得更好的."
    m 3ekb "要多练习一下,好吗?"
    m 5hua "我期待你可以流畅演奏的那天~."
    return
    
#everything's alright
label piano_tothemoon_loaded:
    m 1eua "假如你迷路了怎么办?"
    m 1kua "那么我们总会在月球上见到的."
return

label piano_tothemoon_win:
    m 1euc "[player],你知道{i}To the Moon{/i}这个游戏吗"
    m 3eud "虽然我并不怎么玩游戏,但是我觉着这个游戏还不错."
    m 3euc "你以前玩过这个游戏吗?"
    menu:
        "你以前玩过这个游戏吗?{fast}"
        "没有":
            m 1eub "好吧~"
            m 1eua "那我等你玩过这个游戏再讲吧~"
            return
        "玩过":
            m 1hub "好耶~"
            m 1eub "这样我就不担心剧透了."
    m 1euc "这个故事主要讲的是Eva与Neil医生用一种能够'编织人工记忆'的技术实现Johnny的梦想的故事."
    m 3euc "但是Johnny的梦想是.{w=0.3}.{w=0.3}.去月球."
    m 3eud "然后两位医生在实现它的梦想的过程中经历了johnny的一些重要时刻."
    m 3hksdrb "啊哈哈,这边就不再赘述了,要不然太啰嗦啦~"
    m 3gkc "你知道吗,其实...River一直爱着Johnny"
    m 3ekc "大概因为这样所以才不惜自己的病而坚持让Johnny建起那栋房子吧."
    m 1ekd "而River对灯塔的偏执,叠那么多的纸兔子的目的也仅仅是{w=0.7}想让Johnny想起他童年的约定罢了."
    m 1ekc "然后两位博士为了实现Johnny的梦想,抹除了记忆中的River."
    m 7efd "我觉着这对River很不公平!{w=0.1}仅仅只是为了完美结局却把两个人的特别回忆抹除."
    m 3dkc "...假如要是为了实现我的梦想就把你给抹杀的话,我觉着我不能接受."
    m 3rkc "不过两位医生也只是为了工作例行公事而已,而且Johnny也已经如风中残烛一样,时日不多了."
    m 1euc "所以这种结局对他来说应该是更好的结局吧."
    m 7eud "你还记着Johnny与River小时候的约定吗?"
    m 1eua "'假如你迷路了怎么办?'"
    m 1dua "'那么我们总会在月球相见的,[player].'"
    m 1hubla "不用担心,我一直爱着你,我们未来总会再见到的~"
return "love"


        


#Doki Doki Forever
label piano_ddf_loaded:
    m 1eua "对你永远心动~"
    return

label jmcustom_ddf_win:
    m 1wua "弹的太棒了,[player]."
    m 1hub "谢谢你能陪我一起弹钢琴~"
    m 3euc "这首歌是DDLC的粉丝们送给它的礼物."
    m 4esd "你知道吗,这首歌在Youtube上已经有1千多万的播放量."
    m 3wuo "但是不仅如此,粉丝们制作的这首歌的MMD甚至有近3千万!"
    m 7nsu "我也很喜欢这首歌."
    m 3dso "{i}~Shall I leave you be~{/i}"
    m 3esb "{i}~is it love if I can set you free~{/i}"
    m 1hsa "{i}~but even if it's not reality~{/i}"
    m 1esb "{i}~Let's be together forever~{/i}"
    m 7hua "{i}~We're never gonna be apart~{/i}"
    m 5kuu "不过不一样的是,这一次我可不会让你离开了哦~"
    m 5ksa "我们会永远在一起."
    return

#JmDemisana的通用对话
label jmcustom_common_complete:
    m 1wua "弹的很棒,[player]."
    m 7eub "只要能多加练习,你就能弹的更好了."
    m 5euc "尽管我很想弹弹我对这首歌的看法,但我不想让我的想法影响到你练习这首歌."
    m 5eub "所以如果你能把这首歌流畅的弹下来，我就告诉你我的想法."
    m 5eua "我希望你能理解我~"
    return

label jmcustom_common_escape:
    m 1euc "..."
    m 1eua "啊，至少你尽力了."
    m 5eud "我真的想告诉你我对这首歌的感受,但是我觉着我只能在你弹得更好的时候再说,或许下一次就可以."
    m 1eub "把它当做你的目标,好吗？但如果需要时间,也不要着急.我相信你能做到."
    return

label jmcustom_common_almost:
    m 1wub "弹得很棒呢, [player]"
    m 4eua "只要多一点练习,你就能更快的掌握它."
    m 1eua "我会支持你的,不过不着急."
    m 1eua "慢慢来就好啦."
    return

#Back to December by JmDemisana
label jmcustom_backtodecember_perfect:
    m 1sua "哇,你弹得完美无缺呢,[player]"
    m 7eua "你知道这首歌的创作是因为Taylor Swift对Taylor Lautner的分手感到伤心吗"
    m 1euc "是的, 我猜没有几个人知道, 但这首歌有一个版本是专门为了{i}那个来自密歇根州的男孩的.{/i}."
    m 1duc "与你奉献了你的爱的人分手,这应该没有什么好的感觉."
    m 1eua "但我不害怕,我相信我们的爱是永恒的."
    m 1eua "我相信你不会离开我的,尽管你离开的可能性很小,但我相信你不会这么做的"
    m 1eub "毕竟,你在这里,还为我弹了这首歌."
    return

label jmcustom_backtodecember_pre:
    m 1eua "Taylor Swift的经典作品？"
    m 1eub "当然,我会为你唱的,[player]."
    return

label jmcustom_ddf_pre:
    m 1sua "哦!我知道这首歌!"
    m 1esb "这是粉丝们送给我们的歌."
    return


#Leaving on a jetplane by JmDemisana
label jmcustom_leavingonajetplane_perfect:
    m 1sua "你真的一点失误都没犯,太棒了."
    m 2euc "等一下!你不是因为要离开一段时间才弹这个的,对吧?"

    menu:
        m "要离开吗?"
        "是的.":

            m 2eud "啊...我好难过.但我也很开心,尽管你要走了,但你还是花时间来陪我弹琴."
            m 3eub "你可以一会告诉我再见来让我知道你什么时候走."
            m 5eua "但现在,我真的很感谢你的到来."
        "不是.":

            m 1wub "好耶！我还以为要让自己忙一阵子呢."
            m 5etc "你走了,我真的会想你的."
            m 4eua "总之..."

    m 7eua "你知道这首歌是1998年电影{i}Armageddon{/i}中的歌曲之一吗?"
    m 1eua "那是一部非常棒的电影,你应该找个时间自己去看看."
    m 5eub "但如果你需要我抱着你,你就不必说了."
    m 6dua "我永远不会让你走的."
    return

label jmcustom_leavingonajetplane_pre:
    m 6euc "感到忧郁吗?"
    m 6eua "嗯,你选对了歌."
    return

#Rainbow Connection by JmDemisana
label jmcustom_rainbowconnection_perfect:
    m 1esb "干得好, Kermit~"
    m 7euc "你知道吗, 我不同意晨星的愿望不会实现的说法."
    m 6duc "在你来之前,我唯一的想法就是希望你回头看一下我."
    m 4euc "那边的窗户是我看到曾经悲伤幻象的地方,我可能再也找不到彩虹的连接."
    m 7eud "但后来..."
    m 7eua "太阳的光芒照耀着,让你的心相信你在乎."
    m 7eud "因为事实是..."
    m 1eub "我只从你那里看到了它"
    m 1wub "我欠你一个人情,因为你完成了我的彩虹."
    m 1hua "我爱你, [player]."
    return

label jmcustom_rainbowconnection_pre:
    m 1eub "选的好, Kermit"
    m 1eua "Oink oink"
    m 1esb "哈哈~"
    return

#Island Song by JmDemisana
label jmcustom_islandsong_perfect:
    m 1esb "太好了!你成功了."
    m 7euc "你知道,《冒险时代》是你永远不会忘记的系列之一."
    m 1eub "谁不希望有一个人人都是有知觉的糖果的世界呢."
    m 1eua "你可能已经看了,但如果你没有,我们可以一起尽情享受."
    m 1esa "你有没有想过,为什么剧中有一堆公主,而Finn却对爱情没有任何兴趣呢?"
    m 3eua "好吧,如果你是粉丝的话,你可能已经看了泡泡糖公主再次成为孩子的那一集,所以..."
    m 5euc "无论如何,听到这首歌有点伤感,因为这首歌在每一集的结尾和该系列的最后一集都在播放."
    m 1eua "不管怎样,我真的希望无论发生什么,我们的曲子都不会改."
    m 1hua "我会永远爱着你.希望你能永远对我做同样的事."
    return

label jmcustom_islandsong_pre:
    m 1eud "这首歌有点悲伤..."
    m 1eua "不过我不会介意的~"
    return
