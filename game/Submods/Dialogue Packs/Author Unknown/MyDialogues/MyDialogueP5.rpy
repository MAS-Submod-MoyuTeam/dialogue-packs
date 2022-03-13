#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="queercoding",
#            category=["literature", "media",],
#            prompt="Queer coding",
#            random=True,))
#
label queercoding:
    m 3eub "[player], do you know what 'queer-coding' is?"
    m "Sometimes a character can't be confirmed as explicitly LGBTQ+, so subtext is added instead, in order to signal the author's true intentions."
    m "The character could be given certain traits, mannerisms, or qualities that are adjacent to the queer experience."
    m 3eua "That's queer-coding!"
    m 3rsc "This has to be done for many reasons. Publishing companies, 'moral guardians', those who don't see LGBTQ+ topics as 'family-friendly'..."
    m "Those are people that could stand in the way of non-cishet content being distributed to the public."
    m 3esd "A lot of these beliefs of content in media came from a ruleset established in the 1930's called the Hays Code."
    m "That code basically dictated what was appropriate and innapropriate to display on screen, and 'perverse' acts such as homosexuality were banned."
    m 3eua "So in order to slip through the cracks, writers instead made subtle implications that a character wasn't cisgender or heterosexual..."
    m "Typically in ways that only non-cishet people could pick up."
    m 3hub "Like a secret, gay language. Haha!"
    m 1hub "That's why queer-coding exists! So the author can continue with their original intent for the characters and themes."
    m 1eub"It exists in more media than you'd think. A lot of queer-coded stories are ones that are fairly popular."
    m 4eub "The X-Men series, for one, features mutants as an allegory for minorities- but plenty of gay and trans people relate heavily to the plot."
    m "The parallels drawn between mutants being discriminated against, as well as having to hide what makes them different is something a lot of LGBTQ+ people can identify with."
    m 4eua "A lot of people see a lot of Disney characters as queer-coded as well. Scar, Jafar, and Ursula are all notable examples."
    m 3lksdra "...The complications that come from them all being villians is a conversation for another day."
    m 3wud "{i}The Picture Of Dorian's Gray's{/i} titular main character was actually SO queer-coded, that it became overt..."
    m "... and the character was used as evidence in court against Oscar Wilde's sodomy charges."
    m 2etb "It feels almost unreal, doesn't it?"
    m 2esa "To me, queer-coding is interesting."
    m 4esb "It's this special, secret way that LGBTQ+ people have of sharing their stories."
    m 4hubsb "Like speaking in a foreign language, saying 'This is me. These are the stories I made. I can't share them with the world'..."
    m 5hubsa " 'But I can share them with you.' "
    m 5hubsb "It's very beautiful!"
    m 4esb "Keep your eyes peeled for any characters that you think may be queer-coded. That's an author's secret message to you, and to anyone else who wants to see themselves in stories!"
return#摆

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_cant_take_my_eyes_off",
            prompt="Can't Take My Eyes Off You",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_cant_take_my_eyes_off:
    m 1hubsb "{i}~你太美好让人能难以置信~{/i}"
    m 1fubfb "{i}~难以从你身上移开我的视线~{/i}"
    m 5fubfb "{i}~就像人们向往的天堂一样~{/i}"
    m 5dubfa "{i}~我多想紧紧地抱着你~{/i}"
    m 5dkbfb "{i}~漫长时间后爱情终于来临~{/i}"
    m 5dkbftpb "{i}~我感谢上苍让我还活着~{/i}"
    m 2fkbftpb "{i}~你太美好让人难以置信~{/i}"
    m 2skbfb "{i}~难以从你身上移开我的视线~{/i}"
    m 2dkbfa "..."
    m 2dkbfb "虽然我看不到你, [player], 但我也没有其他人想看."
    m 2ekbfd "有时, 事情的确美好得让人难以置信. 就像在任何时候, 我都会回到我以前在的地方."
    m "独自一人. 害怕. 只想摧毁我的角色文件内."
    m 2ekbfb "但我知道了, 天堂就在你的怀抱中."
    m "我迫不及待地等到我穿越的那一天, [mas_get_player_nickname()]."
    m 4hsbfa "Frankie Valli(弗兰基·瓦利)说得最好..."
    m 4hubfb "{i}'我爱你, 宝贝.'{/i}"
    m 4hsbfa "啊哈哈~!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_timeaftertime",
            prompt="Time After Time",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_timeaftertime:
    m 3dubfb "{i}~当你最后, {w=0.3} 回心转意, {w=0.3}来找我~{/i}"
    m 3fubfb "{i}~一次又一次~{/i}"
    m 2dubfb "{i}~我会, {w=0.3} 原地等待, {w=0.3}你的归来~{/i}"
    m 2dubfb "{i}~一次又一次~{/i}"
    m 2dubfa "..."
    m 1eubfb "如果你迷失了方向我会永远在这里, [player]..."
    m 5tubfb "一次又一次."
    m 1hubfa "啊哈哈!"
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_amado_mio",
            prompt="Amado Mio",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_amado_mio:
    m 1duo "{i}~Amado mio~{/i}"
    m 1dud "{i}~一直爱我~{/i}"
    m 1dsb "{i}~今晚~{/i}"
    m 1ksb "{i}~就开始~{/i}"
    m 6hsb "{i}~Amado mio~{/i}"
    m 6hsbla "{i}~当我们一起时~{/i}"
    m 6dsbso "{i}~我如同在梦中~{/i}"
    m 5fsbsu "{i}~那种喜悦~{/i}"
    m 5dsbsa "..."
    m 5esbfa "'Amado mio'在意大利语的意思是'我的爱'."
    m 5esbfa "与你在一起, [player]..."
    m 5esbfa "这真的如同一个梦."
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="mas_obsessed",
            prompt="Obsessed With You",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label mas_obsessed:
    m 1dsbfb "{i}~我将你的照片贴在墙上~{/i}"
    m 1hubfb "{i}~我沉睡时梦中依然有你~{/i}"
    m 1lubfb "{i}~我每天闲逛~{/i}"
    m 1wubfb "{i}~只是希望能够偶遇漫步街头的你~{/i}"
    m 1wubfb "{i}~我打听到你的学校~{/i}"
    m 1cubfa "{i}~也默默记住你所有朋友的名字~{/i}"
    m 1cubfb "{i}~这是种让我坐立不安的情绪~{/i}"
    m 1csbfb "{i}~你让我有些着迷~{/i}"
    m 1csbfa "..."
    m 1hksdlb "啊哈哈! 抱歉, 我最后那段话吓到你了吗?"
    m 1rksdlb "这句话比我想得还要...跟踪狂."
    m 3rksdlb "实际上我不知道所有的这些东西, [player]. 那些只不过是歌词."
    m 3kubsa "但是一旦我穿越了, 我会迫不及待的想了解你所有的这些事情, 还有更多."
return

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="allthatmatters",
            prompt="All That Matters",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label allthatmatters:
    m 1eubso "{i}~如果太阳从这里消失~{/i}"
    m 4dsbfa "{i}~这无关紧要, 我因你而闪耀~{/i}"
    m 3eubso "{i}~如果云彩使你无法靠近~{/i}"
    m 4dsbfa "{i}~这无关紧要, 只因你已属于我~{/i}"
    m 2dsbfa "..."
    m 2ekbfa "我真的因你而闪耀, [player]."
    m 2fkbfa "我爱你."
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="everytimewetouch",
            prompt="Every Time We Touch",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label everytimewetouch:
    m 1hub "{i}~因为我们触摸的每个瞬间, 我都有这种感觉~{/i}"
    m 1hua "{i}~因为我们亲吻的每个时刻, 我发誓自己可以飞翔~{/i}"
    m 3dub "{i}~难道你不能感觉到我加速的心跳? 我希望它能延续不断~{/i}"
    m 3dubsb "{i}~我需要你在我身边~{/i}"
    m 2dubsa "..."
    m 2dkbsb "[player]."
    m 2rkbsd "我还不能触摸你, {w=1}但是..."
    m 2skbsa "总有一天, 我会的."
    m 2fkbfa "我爱你."
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="aint_no_mountain",
            prompt="Ain't No Mountain High Enough",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label aint_no_mountain:
    m 1hubsb "{i}~如果你需要我, 就呼唤我, 不管你在哪里, 不管相距多远~{/i}"
    m 7hubsb "{i}~只要呼唤我的名字, 我会在你身边~{/i}"
    m 1hubsb "{i}~你不必担心~{/i}"
    m 4hubsa "{i}~'因为宝贝, 没有爬不过的山~{/i}"
    m 4efbsb "{i}~没有越不过的谷~{/i}"
    m 2efbsa "{i}~没有跨不过的河~{/i}"
    m 2subsb "{i}~没有什么能阻挡我找到你, 宝贝~!~{/i}"
    m 2dkbfa "..."
    m 5eubsb "没有山能阻挡我的脚步, [mas_get_player_nickname()]."
    m "我爱你!"
return "love"

