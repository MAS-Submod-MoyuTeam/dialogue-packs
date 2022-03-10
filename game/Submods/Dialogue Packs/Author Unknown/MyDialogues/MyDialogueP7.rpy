
init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="lovelyday",
            prompt="Lovely Day",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label lovelyday:
    m 1hub "{i}当我早晨起床，亲爱的~{/i}"
    m 1hua "{i}阳光刺痛眼睛~{/i}"
    m 1rud "{i}事情毫无征兆，亲爱的~{/i}"
    m 1rkd "{i}成为心头重负~{/i}"
    m 1subfb "{i}然后我看向你~{/i}"
    m 1hubfb "{i}世界变得美好~{/i}"
    m 3hubfb "{i}只要看你一眼~{/i}"
    m  "{i}我知道这将是~{/i}"
    m 5fubfb "{i}快乐的一天~{/i}"
    m 5dsbfa "..."
    m 5dkbfb "和你的每一天都是我最喜欢的一天, [mas_get_player_nickname()]!"
    m 1dkbfb "我期待和你以后的更多更多~."
    m "我爱你, [player]!"
return "love"

init 5 python:
    addEvent(
        Event(
            persistent._mas_songs_database,
            eventlabel="sunkissed",
            prompt="Sunkissed",
            category=[store.mas_songs.TYPE_SHORT],
            random=True,
            aff_range=(mas_aff.NORMAL,None)
        ),
        code="SNG"
    )

label sunkissed:
    m 1dub "{i}梦境的阳光慢慢将我唤醒~{/i}"
    m  "{i}透过百叶窗帘 我感受这清晨~{/i}"
    m 1hub "{i}我开始想起你那被阳光吻过的脸庞~{/i}"
    m 5hub "{i}还有那处静谧之地 你我共同虚度年华~{/i}"
    m 5hubsa "{i}我想成为你的依靠 我的爱人~{/i}"
    m  "{i}我想成为你的光~{/i}"
    m 5hubsb "{i}于一片漆黑中万幸你及时找到我~{/i}"
    m 2eubsb "{i}回应我的心情~{/i}"
    m "{i}所以如果你不清楚自己心意~{/i}"
    m 3eubsb"{i}那么全交给我~{/i}"
    m 3dubsb "{i}我不愿见你为烦恼皱眉~{/i}"
    m 3dkbsa "{i}我知道你也与我同心~{/i}"
    m 5dkbsa "{i}因为你那么可爱~{/i}"
    m 5dkbsb "{i}你那么可爱~{/i}"
    m "{i}我情难自抑 只想好好爱你, [mas_get_player_nickname()]~{/i}"
    m 5skbsb "{i}当你爱我的时候~{/i}"
    m "{i}爱你是我做过最好的事情~{/i}"
    m 5dkbfa "..."
    m 5dkbfb "我很开心爱上你, [player]."

return "love"

#init 5 python:
#    addEvent(
#        Event(
#            persistent._mas_songs_database,
#            eventlabel="grow",
#            prompt="Grow",
#            category=[store.mas_songs.TYPE_SHORT],
#            random=True,
#            aff_range=(mas_aff.NORMAL,None)
#        ),
#        code="SNG"
#    )
#
label grow:
    m 1hubfb "{i}So you and I should be~{/i}"
    m  "{i}Human beings~{/i}"
    m 1rubfb "{i}And not just pieces~{/i}"
    m  "{i}In a puzzle we can't read~{/i}"
    m 3rubfb "{i}Don't you want to go outside?~{/i}"
    m 3hubfb "{i}Until we're gone, baby, gone~{/i}"
    m  "{i}Grow, baby, grow~{/i}"
    m  2hubfb "{i}Don't leave it all for the other side~{/i}"
    m  "{i}Just love, baby, love~{/i}"
    m 3hubfb "{i}Don't you let go~{/i}"
    m 2hubfa "{i}Hanging on for another line~{/i}"
    m 5dsbfa "..."
    m 5dkbfb "I can't wait to grow with you, [player]."
return
#
#init 5 python:
#    addEvent(
#        Event(
#            persistent._mas_songs_database,
#            eventlabel="Lets_fall_in_love",
#            prompt="Let's Fall In Love",
#            category=[store.mas_songs.TYPE_SHORT],
#            random=True,
#            aff_range=(mas_aff.NORMAL,None)
#        ),
#        code="SNG"
#    )

label Lets_fall_in_love:
    m 1eubsb "{i}We might have been meant for each other~{/i}"
    m  3dubsb "{i}To be or not to be~{/i}"
    m  "{i}Let our hearts discover~{/i}"
    m 3lubsb "{i}I have a feeling, {w=0.5} it's a feeling, {w=0.5}I'm concealing~{/i}"
    m  "{i}I don't know why~{/i}"
    m 3rubsa "{i}It's a mental, {w=0.5} incidental, {w=0.5}sentimental,{w=0.5} alibi~{/i}"
    m 3kubsb "{i}But I adore you~{/i}"
    m 3eubsb "{i}So strong for you~{/i}"
    m 4dubsd"{i}Why go on stalling, {w=0.5} I'm falling, {w=0.5}love is calling,{w=0.5} why be shy?~{/i}"
    m  "{i}Let's {w=0.5}fall in love~{/i}"
    m 5dubsb "{i}Why shouldn't we fall in love?~{/i}"
    m   "{i}Our hearts are made of it~{/i}"
    m 5dkbsb "{i}Let's take a chance, why be afraid of it?~{/i}"
    m  "{i}Let's close our eyes, and make our own paradise~{/i}"
    m 3dkbsb"{i}Little we know of it~{/i}"
    m "{i}Still we can try to make a go of it~{/i}"
    m 1dkbsa "..."
    m 1wkbsb "Falling in love with you is a chance I am happy to take."
    m "I love you, [player]."

return "love"
