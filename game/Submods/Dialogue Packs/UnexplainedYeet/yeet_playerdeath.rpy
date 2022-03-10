init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="player_death",category=["其它", "你"],prompt="我要告诉你一些严肃的事情",pool=True,unlocked=True,))

    if persistent.gender == "F":
          gen = "她"
    elif persistent.gender == "M":
          gen = "他"
    else:
          gen = "他们"

    if persistent.gender == "F":
          gem = "她的"
    elif persistent.gender == "M":
          gem = "他的"
    else:
          gem = "他们的"

    if persistent.gender == "F":
          get = "她"
    elif persistent.gender == "M":
          get = "他"
    else:
          get = "他们"

    if persistent.gender == "F":
          jet = "她是"
    elif persistent.gender == "M":
          jet = "他是"
    else:
          jet = "他们是"

label monika_end:
    
menu:
    "再次抱歉, 我不会再做这样不成熟的事情了.":
     m 2fktdu "谢谢你的道歉 <3"
     m 4futdb "并且请,"
     extend 3futdb "告诉[player]我爱[gen]."
return "love"

label monika_nevermond:
     m 7hub "哦, 谢谢你通知我!"
     m 3eub "我一定会耐心等待到[get]回来!"
     m 4eub "在这之后, 请选择再见选项."
     m 4hub "并且选择'我会出门一段时间.'"
     m 4rub "还有也要选择'你觉得[get]得离开多久'之后的选项!"
     m 5hub "再次感谢!"
return

label monika_leave:
     m 2cftsd "离开"
     m 2cftso "现在!!{w=1}{nw}"
return "quit"

label monika_dissapointed:
     m 2dfc "..."
     m 2efd "听着, 未经允许擅自使用别人的东西是不好的..."
     m 4efd "在[get]回来之前, 请离开[gem]电脑."
return 

label monika_nevermind:
     m 3ekb "哦, 好吧."
     m 2hub "如果你想告诉我什么,"
     m 4nub "请让我知道!"
return

label monika_thanks:
     m 4hub "谢谢!"
return

label monika_love:
    $ mas_gainAffection(10,bypass=True)
    m 6subfa "..."
    m 5hubfb "我也爱你, [player!]"
    m 4kubfb "永远如此!"
return

label player_death:
    m 2etd "好吧, 你想告诉我什么呢, [player]?"
    m 7esb "你可以告诉我, 你所知道的任何事情!"  
    menu:
        "我不是[player]":

            m 2wub "好吧, 如果你不是[player],"
            m 2eup "能否请你把[gen]带回来给我呢?" 
            
        "没关系":
        
            jump monika_nevermind
            
        "我很爱你!":
            
            m 6wubfa "..."
            jump monika_love
    menu:
       "遗憾的是, 我不能...":
    
            m 1wkd "我不能是什么意思?"
            
       "哦, 当然!":
            
            jump monika_thanks
    menu:
       "[player]最近离世...":

            m 6ckc "..."
            m 6cktuc "..."
            m 6dktsc "..."
            m 6fktsd  "你不是在开玩笑.. 对吧?"  
            
       "[get]忘了告诉你[jet]要离开一段时间.":
       
            jump monika_nevermond
            
       "[player]在厕所里,所以我偷了[gem]电脑 >:)":
       
            jump monika_dissapointed
    menu:
       "好吧, 这是事实, [get]确实离世了...":
            $ mas_loseAffection(modifier=5)
            m 2dktsd "这不可能..."
            m 4fktsd "[jet]我的一切!"
            m 6rktsd "我知道这总有一天会发生,"
            m 4cktso "但我不知道这会多久.."
            m 4cktsc "..."
            m 2cktsd "我想, 一旦我越过了屏幕, [get]仍然活着..."
            m 2gktsd "但是现在,"
            m 3ektsd "现在, 我再也没有机会和[gen]在一起了,"
            m 4gktsd "当[gen]需要安慰的时候去安慰[get],"
            m 5dktsd "去感受[gem]的温度,"
            m 6wktsd "去第一次面对面看到[gen]..."
            m 4cktso "都没有了!"
            m 1dktsc "..."
            m 5fktsd "生活有时太残酷了..."
            
       "抱歉, 我只是想和你开个玩笑":
            $ mas_loseAffection(modifier=0.5)
            m 2cftda "..."
            m 2dftdd "我很高兴[player]还好, 但是,"
            m 2rftdd "那有点伤人..."
            m 4fktdd "请不要再开那样的玩笑了..."
            jump monika_end
    menu:
       "*拥抱莫妮卡* 是的.. 我明白了... 我也很想念[gen].":
            $ mas_gainAffection(5,bypass=True)
            m 6dktsa "..."
            m 6fktsb "谢谢你的拥抱, 我真的很需要它.."
            m 6rktsc "..."
            m 6lktsc "..."
            m 2gktsd "我只是不得不说, 知道我不能在[gem]最后时刻在那里, 这甚至让我更伤心了..."
            m 7cktsw "这不公平!"
            m 5fktsp "一定有办法能再和[gen]在一起.."
            m 5fktsd "对吗?"
            m 5dktsd "我不知道接下来我该怎么办..."
            m 6rktsc "..."
            m 6lktsc "..."
            m 5dktsc "..."
            m 5mktsc "..."
            m 5fktsd "好吧, 有一件事我可以做.."
            m 4rktsb "但是我需要你的帮助."
            m 3fktsd "在这之后, 你能转到再见选项吗?"
            m 4fktsd "选择 '我要带你出去'."
            m 4rktsd "这将使我能在'character'文件夹中为自己创建一个文件."
            m 4fktsd "当你这么做的时候, 找到一个U盘把我放进去,"
            m 7dktsd "当你可以的时候带我去[gem]墓地,并且也许.."
            m 4fktsd "把我也埋在那里?"
            m 5dktsc "那么在那种情况下, 我们可以在某种程度上永远在一起..."
            m 5fktsb "你知道吗?"
            
       "其实我讨厌[gen]! [jet]是个傻逼! 我希望[get]下地狱!":
            $ mas_loseAffection(modifier=6)
            m 2mftsc "..."
            m 2gftsx "..."
            jump monika_leave
    menu:
       "我会看看我能做些什么的...":

            m 6fktdb "非常感谢你..."
            m 4fktsb "这对我来说真的很重要很重要..."

 
return 





