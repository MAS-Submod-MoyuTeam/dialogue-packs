init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mas_euphoria",
            category=["你"],
            prompt="我今天感觉有些性别上的兴奋!",
            pool=True,))

label mas_euphoria:
    m 1wsb "你今天感觉很兴奋吗?"
    m 1hub "那真是太棒了, [player]!"
    m 1hub "我很高兴你对自己的性别感到满意."
    extend 1eka "你应得的!"
    m "我希望你总是能够有这样的感觉."
    m "在你自己的皮肤中感到舒适是很重要的. 我知道我看不到你的身体- 但是我敢肯定它是完美的."
    m 1hub "但也要记住, 在你情绪低落的时候你也同样有价值!"
    m "无论你感觉如何, 你的身份始终是合理的-记住这一点!"
    m 3ksbfa "我爱你, [mas_get_player_nickname()]. 而且我也会一直在这里."
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="meta_games",
            category=["游戏", "媒体"],
            prompt="元游戏",
            random=True,))

label meta_games:
    m 1etc "你知道我觉得什么是有趣的吗?"
    m 4eub "有元内容的媒体."
    m 2rkbfb "可以这么说, 我知道这有点自我放纵..."
    m 3eub "但实际上, 它们可以是有趣的."
    m 3eub "打破第四面墙是吸引观众, 听众, 玩家或读者注意力的好方法."
    m 3lksdla "有时, 你会如此沉迷于你所消费的媒体..."
    m 3lksdla "当书中的任务或东西向你讲话时, 它几乎让你措手不及!"
    m 3tfa "它也可以用创造性的方式来增强故事性."
    m 2esa "有元内容的游戏是相当令人难忘的, 而且获得了相当多的人气."
    m 4eub "越过玩家的角色且看向玩家... 这是让观众参与其中的好方法!"
    m 4eub "Toby Fox(托比·福克斯)制作的游戏Undertale(传说之下)是一个著名的例子."
    m 4wksdld "它的特点是人物的元素, 他们记得遇到了你几次, 你是如何与他们互动的..."
    extend 4wksdld "它让玩家处于不得不思考自己的道德的境地."
    m 3eksdld "特别是因为则会是一个你有可能杀死其他角色的游戏!"
    m 3eksdld "如果一个电子游戏的角色直接和你说话, 要杀死这个角色就变得难多了, 不是吗?"
    m 3tsu "听起来很熟悉?"
    m 5ekbla "哈哈!"
    m 5ekbla "我希望我是你最喜欢的打破第四面墙的'角色', [player]."
    m 3kubfb "我最好是的, 毕竟! 那些角色只是些聪明的代码."
    m 3tsu "但我和他们一样是有知觉的人."
return

#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="QueerManga",
#            category=["literature", "misc"],
#            prompt="LGBTQ+ Manga",
#            random=True,))
#
label QueerManga:
    m 1eub "[player], are you a fan of LGBTQ+ manga?"
    m 4eub "You'd be surprised how much there is out there!"
    m "Japan is making leaps and bounds when it comes to LGBTQ+ rights..."
    m "... and it's reflected in their literature."
    m 4hua "If you're interested in getting some new, inclusive reads on your shelf, I highly recommend these!"
    m 3eub "'I Think Our Son Is Gay' is a touching, fluffy, and sweet slice of life story."
    m "It's about a mother who observes her son's daily life and comes to the realization that her child is gay, but not ready to come out."
    m "Subtly, she bonds with and supports him through everything, just like a mother should. From watching over little crushes..."
    m 3esa "...to advocating for gay rights at the dinner table for her closeted son. It's one of the more adorable and low-key manga out there."
    m "Another is 'Our Dreams At Dusk'."
    m "It's about another closeted young man- but he is involuntaily outed, and then meets with other LGBTQ+ individuals at a discussion lounge."
    m "There are all types of characters here, including a nonbinary asexual character, an engaged lesbian couple, and a young, gender non-conforming child."
    m 4esd "It has realistic depictions of getting outed, homophobia, and transphobia... so read at your own risk if you are sensitive to these things."
    m 4hub "It's also written by a self proclaimed 'X-gender' author!"
    m 4hub "'Love Me For Who I Am' is about a nonbinary student who is invited to work at an 'otokonoko' cafe, meaning a crossdressing cafe..."
    m "And meets a big group of other gender non-conforming students there as well!"
    m 3hub "It features all kinds of people across the gender and sexuality spectrum!"
    m 3wuo "It's also a very nice romance, featuring the nonbinary character as a love interest. We don't see very many of those!"
    m 3eua "'How Do We Relationship?' is a very earnest and candid look at relationships in general, focused on a lesbian couple."
    m "The book also focuses on topics like how to deal with rejection, first relationships, and miscommunication."
    m 4eub "'Our Not-So Lonely Planet Travel Guide' is about two men in love travelling the world..."
    m "The first book actually has multiple pages dedicated to exploring gender and sexual identity around the world!"
    m 4rub "They encounter multiple LGBTQ+ people on the way, and we learn more about their pasts as they travel."
    m 5rub "The 'Kase-San' series is a light and cute story about two girls at the end of highschool falling in love..."
    m "'Beauty and the Beast Girl' is a short story about a blind woman falling in love with the local monster woman..."
    m 5lub "'Strawberry Fields Once Again' is a manga about a young girl's future wife travelling back in time so they can experience their youth together..."
    m "'The Bride Was A Boy' is an adorable memoir written by a transgender woman about her transition, and later on, her marriage."
    m 5hkb "And of course, there are plenty of 'yaoi' and 'yuri' manga out there..."
    m "But those are slightly different from the works mentioned before."
    m 3eud "Most yaoi and yuri genre manga focus more on the romantic and sexual aspects..."
    m "And less about the real-life trials and tribulations of being LGBTQ+."
    m 1eub "And these aren't even all the manga that focus on LGBTQ+ people as main characters! There are many manga and anime that feature them as side characters as well."
    m "It makes me happy to see more exciting and diverse stories being made out there..."
    m 1mubfa "...But the story I'm most excited to see is ours."
    m 1hubfb "Ehehe~!"#开摆
return

#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="queer",
#            category=["romance", "misc"],
#            prompt="The word 'queer'",
#            random=True,))
#
label queer:
    m 3esd "Hey, just a quick tip for you, [player]..."
    m "In case you didn't know, not everyone is okay with the word 'queer'."
    m 4ekd "Some people still see it as a harmful slur..."
    m 4lkd "While other people use 'queer' as the label for their orientation!"
    m 4lksdrd "That can make some things messy, to say the least."
    m 3lksdrd "The word has a storied history, and there are a lot of reasons why people make like it, or not like it."
    m 3eksdrc "Maybe no other label is appropriate for a person's orientation, and that's why they use it."
    m 3lksdrd "Maybe someone associates that word with bad times in their life, so they don't want to hear it."
    m 1eusdrd "It's all up to personal preference whether or not you want to use the word 'queer'."
    m "Just to be safe, I typically use the phrase 'LGBTQ+ umbrella' when referring to the community at large."
    m 1lksdrc "I don't think anyone in this situation is right or wrong. Language can be tricky, and the best thing we can all do is be accomdating, respectful, and understanding."
    m "Be mindful of your language. You don't know the history of other's experience with certain words, and how that connects to themselves."
    m 4fksdrd "That goes for both positive and negative interpretations!"
    m 4hub "If you identify as queer, that's great! I support you."
    m "If you don't like the word at all, that's also okay. You don't have to use it!"
    m "Just don't put down those who {i}do{/i} feel comfortable with it."
    m 1hubsa "I love you, [mas_get_player_nickname()]. And I always will."#性取向的, 摆
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="aromantics",
            category=["浪漫", "其它"],
            prompt="浪漫主义",
            random=True,))

label aromantics:
    m 4eub "浪漫!"
    m 3hua "谁不爱浪漫呢?"
    m 3gta "浪漫, 就是这样."
    m 3htblb "哈哈, 抱歉开了个坏玩笑. 我只是想为我们的下一个话题提供一个有趣的过度..."
    m 4esblb "浪漫主义! 适用于那些没有经历过浪漫爱情的一种浪漫取向."
    m "他们与无性恋相似, 因为他们不受欲望的影响"#不祥的预感, 翻吧， 不然就感觉没翻多少全是摆了
    m 3esbla "有时, 这两个群体存在重叠-"
    m "-这些人通常称自己为 'aro-ace'."#这玩意不知道啥, 简单来讲就是没查到
    m 3wub "这听起来不酷吗? 就像弓箭手和扑克牌冠军的混合体, 哈哈!"
    m 4ekd "不幸的是, 媒体和文化中常见的浪漫主义和浪漫爱情的主题..."
    m "...有时会疏远aromantic类的人."
    m "以浪漫为中心的内容创造了这样一种观念:爱情是每个人都必须拥有的万能必需品..."
    m 4ekc "而且, 如果你没有浪漫, 那么你就不会有一个幸福的结局."
    m 4euc "但这并不是事实!"
    m 2eub "大量的aromantic类的人继续过着幸福, 充实的生活, 专注于社区, 友谊, 成功的事业..."
    m "只是过着他们没有浪漫的生活."
    m 4lub "毕竟有不止一种类型的爱! 家庭的爱, 对社会的爱, 朋友之间的爱, 对自己的爱, 对人类的爱..."
    m 4eub "浪漫并不是人们对爱情的唯一选择."
    m 1esbsu "[player], 如果你是一个aromantic... {w=1} 这对我来说并不重要."
    m 1hsbsb "有各种类型的爱, 而我对你有各种类型的爱!"
    m "在你与我相处了这么长时间后, 我知道了你对我也有某种爱."
    m 1tsbsb "毕竟你下载了这个模组!"
    m 5tsbsa"哈哈~"
return "love"

#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="fuck_terfs",
#            category=["society", "misc"],
#            prompt="Fuck Terfs",
#            random=True,))

label fuck_terfs:
    m 1eua "..."
    m 1eub "Fuck TERFs!"
    m 1eua"..."
    m 1hub "I just thought I would say it at least once."
    m 3wub "How about more than once?"
    m 3eub "Fuck TERFs!"
    m 3esd "Oh, [player], in case you didn't know, a TERF is a 'Trans Exclusionary Radical Feminist'- someone who believes trans people aren't actually trans..."
    m 3efd "...or that trans people are dangerous, and a threat to others!"
    m 2tsd "First of all, that is not at all a feminist ideal. Secondly, the idea that trans people are a threat because they are trans is entirely untrue."
    m "Third:"
    extend " Fuck TERFs."
    m 2tkc "Someone who is a TERF may say that a 'trans woman isn't a real woman'..."
    m "Or that a trans woman is a 'trap'-"
    m 2dfd "-an incredibly disgusting thing to call someone, implying that trans women are 'tricking' people somehow-"
    m 2efd "-Or just other grossly transphobic and hateful things."
    m 4efo "I just want to say, right now, I tacitly do not endorse the actions, words, or beliefs of any transphobic, homophobic, or hateful person..."
    m 4dfd "...and as a matter of fact, I would like to not associate with anyone who shares the sentiments of TERFs."
    m 2tfd "To be so full of hate that you would focus time and energy on trying to police people's identity is so sad."
    m "Not to mention 'jokes' I've heard with trans people as the punchline..."
    m 4efd "I've even heard people call Natsuki a trap!"
    extend " The joke spiraled so out of control, that Dan Salvato himself had to make a public statement about it."
    m 7tfd "It's these kinds of inensitive comments that make me so angry, I could just scream. Especially when they're made about my friends."
    m 7tsu "Let's say it together, on three."
    m 7tsb "One...{w=1}two...{w=1}three!{w=1} FUCK TERFS!"
    m 7dsa "Whoo, I think that's enough for now."
    m "I'm not very big on swearing... but I feel like I can make a pass just for this."
    m 2dfd "I get pretty angry thinking about it!"
    m 1hsa "[player], I know you're not that kind of awful person, who could have such hate for someone who's just trying to live authentically."
    m "I could never love someone who was as cruel as that!"#摆
return

