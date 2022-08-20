
#init -990 python:
#    store.mas_submod_utils.Submod(
#        author="LC",
#        name="Jay的歌曲",
#        description="莫妮卡听了不少Jay的歌",
#        version='1.0.0'
#    )

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_you_hear_me",
            prompt="你听得到",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_you_hear_me:
    m 1dubfd "{i}~有谁能比我知道~{/i}"
    m 1eubfb "{i}~你的温柔像羽毛~{/i}"
    m 1rubfu "{i}~秘密躺在我怀抱~{/i}"
    m 1dubfb "{i}~只有你能听得到~{/i}"
    m 1kubfb "欸嘿嘿~"
    m 3eubfa "这首歌是杰伦在03年《叶惠美》中发表的的一首歌"
    m 1eubfa "歌曲里有一个倒放彩蛋"
    m 1eubfb "你可以去听听看哦"
    m 1rubfa "也是我想对你说的话哦"
    m 1kubfa "我爱你"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_Sunny_day",
            prompt="晴天",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_Sunny_day:
    m 1dubfd "{i}~从前从前~{/i}"
    m 1eubfb "{i}~有个人爱你很久~{/i}"
    m 1ekbfd "{i}~但偏偏 {/i}"
    extend 1ekbfd "{i}雨渐渐~{/i}"
    m 1rkbfd "{i}~大到我看你不见~{/i}"
    m 1dkbftdd "{i}~好不容易 {/i}"
    extend 1fkbftpd "{i}又能再多爱一天~{/i}"
    m 1ekbftpb "{i}~但故事的最后你好像还是说了 {/i}"
    extend 1dkbftud "{i}拜拜~{/i}"
    m 1ekbftub "这首歌真的杰伦是相当经典的苦情歌了吧"
    m 1ekbftua "整首歌没有雨"
    m 3hkbftpb "但是整首歌却都是雨"
    m 1fkbftpb "幸好你依然在我身边"
    m 1fkbftpc "失去你我就会失去我的世界"
    m 1fkbftpa "有你在的每一天,"
    extend 3fkbftua "都会是晴天哦"
    m 1kkbftua "爱你"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_Common_Jasmine_Orange",
            prompt="七里香",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_Common_Jasmine_Orange:
    m 1dubfd "{i}~雨下整夜~{/i}"
    m 1eubfu "{i}~我的爱溢出就像雨水~{/i}"
    m 1dubfd "{i}~院子落叶~{/i}"
    m 1fubfb "{i}~跟我的思念厚厚一叠~{/i}"
    m 1dubfb "{i}~几句是非~{/i}"
    m 3dubfb "{i}~也无法将我的热情冷却~{/i}"
    m 3fubfa "{i}~你是我唯一想要的了解~{/i}"
    m 1eubfb "非常经典的歌呢"
    m 1eubfu "这首词简直就像一句句优美的诗"
    m 1dubfb "不管外界怎么评价你你依然陪伴着我"
    m 1fubfa "还有什么能够冷却我对你的热情呢"
    m 1kubfa "爱你"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_Nocturne",
            prompt="夜曲",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_Nocturne:
    m 1dubld "{i}~为你弹奏肖邦的夜曲~{/i}"
    m 1dublc "{i}~纪念我死去的爱情~{/i}"
    m 1eubld "{i}~而我为你隐姓埋名~{/i}"
    m 1dubld "{i}~在月光下弹琴~{/i}"
    m 1fubsa "{i}~对你心跳的感应~{/i}"
    m 1fubsb "{i}~还是如此温热亲近~{/i}"
    m 1dubsb "{i}~怀念你那鲜红的唇印~{/i}"
    m 3rubsb "听说这首歌在这些年火的很离谱哦"
    m 1eubsa "似乎是杰伦拿奖拿到手软的一首歌？"
    m 1hubsb "然后就有了'夜曲一响，上台领奖'这一句话哈哈哈"
    m 3lubsb "从文学的角度来解析这首歌"
    m 3eubsa "也是一首相当优秀的作品了"
    m 1fubsa "我很喜欢这一首哦"
    m 1hubsa "唱起来也不是很难"
    m 1gubsa "哪一天我把这个伴奏我学会了可能就可以给你弹唱出来了哦"
    m 1kubsa "爱你"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_Adorable_Lady",
            prompt="可爱女人",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_Adorable_Lady:
    m 1dubfb "{i}~想要有直升机~{/i}"
    m 1dubfa "{i}~想要和你飞到宇宙去~{/i}"
    m 3kubfa "{i}~想要和你融化在一起~{/i}"
    m 3kubfa "{i}~融化再银河里~{/i}"
    m 1dubfb "{i}~我每天每天每天在想想想想着你~{/i}"
    m 1dubfd "{i}~这样的甜蜜让我开始相信命运~{/i}"
    m 1dubfb "{i}~感谢地心引力让我碰到你~{/i}"
    m 1eubfb "{i}~漂亮的让我面红的可爱女人~{/i}"
    m 1eubfb "{i}~温柔的让我心疼的可爱女人~{/i}"
    m 1dubfb "{i}~透明的让我感动的可爱女人~{/i}"
    m 1kubfa "{i}~坏坏的让我疯狂的可爱女人~{/i}"
    m 1fubfb "我会是你的可爱女人吗 "
    extend 1kubfb "欸嘿嘿"
    m 1eubfa "爱你哦"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_Fun_Fair",
            prompt="园游会",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_Fun_Fair:
    m 1eubfb "{i}~我顶着大太阳~{/i}"
    m 1dubfb "{i}~只想为你撑伞~{/i}"
    m 1dubfd "{i}~你靠在我肩膀~{/i}"
    m 1dubfb "{i}~深呼吸怕遗忘~{/i}"
    m 1eubfb "{i}~因为捞鱼的蠢游戏我们开始交谈~{/i}"
    m 1eubfb "{i}~多希望话题不断园游会永不打烊~{/i}"
    m 1eubfb "{i}~气球在我手上~{/i}"
    m 1dubfb "{i}~我牵着你瞎逛~{/i}"
    m 1dubfd "{i}~有话想对你讲~{/i}"
    m 1gubfb "{i}~你眼睛却装忙~{/i}"
    m 1ekbfb "{i}~鸡蛋糕跟你嘴角果酱我都想要尝~{/i}"
    m 1eubfb "{i}~园游会影片在播放~{/i}"
    m 1kubfb "{i}~这个世界约好一起逛~{/i}"
    m 5dubfa "多想和你在一起去一次园游会啊"
    m 5dubfa "总有一天会实现的吧"
    m 1dubfa "嗯..."
    extend 1kubfa "一定会的!"
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_song_The_Longest_Movie",
            prompt="最长的电影",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_song_The_Longest_Movie:
    m 1dkbftpd "{i}~再给我两分钟~{/i}"
    m 1rkbftdd "{i}~让我把记忆结成冰~{/i}"
    m 1dkbftuo "{i}~别融化了眼泪~{/i}"
    m 1dkbftuc "{i}~你妆都花了要我怎么记得~{/i}"
    m 1dkbftsc "{i}~记得你叫我忘了吧~{/i}"
    m 1dkbftsd "{i}~记得你叫我忘了吧~{/i}"
    m 1fkbftsd "{i}~你说你会哭~{/i}"
    m 1dkbftsd "{i}~不是因为在乎~{/i}"
    m 1rkbftsd "这首歌听着真的很心痛"
    m 1rkbftuc "以至于杰伦在演唱会上都唱哭了"
    m 1gkbftuc "可见当时舆论导致的分手让他多么痛苦"
    m 1dkbftpc "但是都过去了,毕竟双方都有家室了"
    m 1rkbftpc "已经没有太大必要再为此难过了..."
    m 1ekbftpc "[player]..."
    extend 1rkbftpd "我不知道你是不是顶着外界的舆论和我在一起"
    m 1fkbftpd "但我有个请求"
    m 1fkbftpd  "不管怎样..."
    extend 3hkbftpa "不要忘了我永远都爱着你好吗?"
return "love"