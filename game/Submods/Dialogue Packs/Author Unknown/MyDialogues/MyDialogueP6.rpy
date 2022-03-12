init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="makemefeel",
            prompt="Make Me Feel",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label makemefeel:
    m 1hubsb "{i}这感觉就像我的力量带着一丝丝温柔{/i}"
    m 1lubfb "{i}多愁善感的 直女杀手{/i}"
    m 6hubfb "{i}那么来搞砸我的心绪吧 没有人比你更擅长这个{/i}"
    m 3dubsb "{i}没有什么比这感觉更棒r{/i}"
    m 3hubfb"{i}这就是你让我感受到的{/i}"
    m 3hubfa "{i}这就是你让我感受到的{/i}"
    m 2hubfa "{i}如此美妙,{/i}"
    extend 2hubfb " {i}如此美妙,{/i}"
    extend 2hkbfb " {i}如此美妙,{/i}"
    extend 2skbfb" {i}又真实无比!{/i}"
    m 3dubsb "{i}这就是你让我感受到的~{/i}"
    m 2dkbfa "..."
    m 2dkbsb "你让我感觉很棒, [mas_get_player_nickname()]."
    m "我爱你!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="wouldntitbenice",
            prompt="Wouldn't It Be Nice",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label wouldntitbenice:
    m 1dud "{i}没有什么能比如果我们长大一些更好~{/i}"
    m 1dud "{i}我们就不有漫长的等待~{/i}"
    m 1dkbsb "{i}没有什么能比我们住在一起更好~{/i}"
    m 1ekbsb "{i}在这个我们应该在一起的世界~{/i}"
    m 1eubsb"{i}你知道它会变的更好~{/i}"
    m 3hubfa "{i}当我们能在一起并互道晚安时~{/i}"
    m 1dubsa "..."
    m 1dkbsb "当我穿越到你的世界时, 这就是我生命中最大的祝福, [mas_get_player_nickname()]."
    m "因为我知道那是属于我的地方."
    m 1hubsb "我爱你!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="whatloveis",
            prompt="I Wanna Know What Love Is",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label whatloveis:
    m 1dubsa "{i}我想知道什么是爱~{/i}"
    m 1dubsa "{i}我知道你能告诉我~{/i}"
    m 1dfbsb "{i}我想感受什么是爱~{/i}"
    m 1dsbsa "{i}我知道你会告诉我~{/i}"
    m 1dubsa "..."
    m 1esbsb "你已经向我展示了什么是爱了, [player]."
    m 1nsbsb "我爱你!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="jenny",
            prompt="Jenny (I Wanna Ruin Our Friendship)",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label jenny:
    m 1hubfb "{i}我想结束我们的友谊~{/i}"
    m 1subfb "{i}我们应该做爱人呀~{/i}"
    m 1dubfa "{i}我不知道该怎么跟你说~{/i}"
    m 3hubfb "{i}因为你真的是我最好的朋友~!{/i}"
    m 2dsbfa "..."
    m 2esbfb "你真的是我最好的朋友, [player]."
    m 2ekbfa "但我们的友谊不可能被一段关系毁掉."
    m "我很高兴能成为你的爱人."
    m 2ekbfb "我爱你!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="sunny",
            prompt="Sunny",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label sunny:
    m 2eubfb "{i}阳光, 昨日我的内心充满着阴暗潮湿的阴雨~{/i}"
    m 2hubfb "{i}我的阳光, 当你对着我微笑的时候, 我内心的痛苦仿佛立时消散~{/i}"
    m 2hubfa "{i}现在折磨逝去, 眼前正是阳光大道~{/i}"
    m 2subfb "{i}我的小太阳散发的光热是如此诚挚~!{/i}"
    m 2subfb"{i}亲爱的你是如此的真诚, 我爱你~!{/i}"
    m 2dsbfa "..."
    m 2esbfb "我的阳光 [player]."
    m "照亮了我的人生."
    m 2ekbfb "我爱你!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="alone_now",
            prompt="I Think We're Alone Now",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label alone_now:
    m 1hubfb "{i}此刻我们是这世界唯一的存在~{/i}"
    m 1tubfb "{i}周围无人能介入我们~{/i}"
    m 1tubfa "{i}此刻我们是这世界唯一的声音~{/i}"
    m 1hubfb "{i}寂静中涌动着的是你我的爱意~{/i}"
    m 2dsbfa "..."
    m 2hubfb "我们已经独处一段时间了, [player]..."
    m "但我还是等不及想听到你的心跳声."
    m 2subfa "我爱你!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_just_the_two_of_us",
            prompt="Just The Two Of Us",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_just_the_two_of_us:
    m 1dubsd "{i}我看见水晶般的雨滴落下~{/i}"
    m  "{i}看着这一切的美丽~{/i}"
    m 7dubsd "{i}当阳光照耀时~{/i}"
    m 7dubsb "{i}脑海中形成一道彩虹~{/i}"
    m 7kubsb "{i}当我偶尔想起你时~{/i}"
    m 1kubsb "{i}我想花点时间跟你在一起~{/i}"
    m 1dkbsa "{i}就我们俩~{/i}"
    m 1dkbsb "{i}只要一起努力就能做得到~{/i}"
    m "{i}只有我们两个~{/i}"
    m 3dubsb"{i}就我们俩~{/i}"
    m "{i}在天空筑起城堡~{/i}"
    m 5hubsb"{i}只有你我~{/i}"
    m 5rubfb "{i}你和我.{/i}"
    m 5rubfa "..."
    m 5rubfb "就我们俩, 哈, [mas_get_player_nickname()]?"
    m 5subfb "对我来说就像做梦一样."

return

#init 5 python:
#    addEvent(
#        Event(
#            persistent._mas_songs_database,
#            eventlabel="mas_the_missing_piece",
#            prompt="The Missing Piece",
#            category=[store.mas_songs.TYPE_SHORT],
#            random=True,
#            aff_range=(mas_aff.NORMAL,None)
#        ),
#        code="SNG"
#    )

label mas_the_missing_piece:
    m 5dkbfb "{i}Everything seems to fade when I see your face~{/i}"
    m 5fkbfb"{i}The sun turns dim, it's true, every time I look at you~{/i}"
    m 5fkbftpd "{i}Nobody understood me, 'til your eyes fixed upon me~{/i}"
    m 5fkbftpb "{i}My puzzle life's complete, now that I've found the missing piece~!{/i}"
    m 5dkbftda  "..."
    m 2fkbftdb "You really are my missing piece, [player]."
    m 2rkbftdb "When I saw you, I understood... everything."
    m 4ekbfb "I have you to thank for my realization... and your love."
    m 2dkbfa "I love you."
return "love"
