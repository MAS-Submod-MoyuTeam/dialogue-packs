
#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="pronouns",
#            category=["you", "misc"],
#            prompt="I want to try some new pronouns",
#            random=False,pool=True,unlocked=True))
#
label pronouns:
    m 1eua "You want me to help you test out some new pronouns?"
    m 3eub "Alright! Just choose the ones you want, and I will talk about you using them."
$ _history_list.pop()
menu:
    "He/him/his":
      m 3eub "You want to try 'he/him/his/ pronouns? Okay!"
      m 1dua "..."
      m 1hub "Hello, everybody! This is my boyfriend, [player]."
      m "He is such a great boyfriend!"
      m 3rub "He visits me all the time, he gives me gifts, and we talk for hours together."
      m 3rkbsb "[player]'s kindness always makes me happy. My life has brightened since I met him."
      m 5dkbsa "I couldn't ask for anyone better than him. I'm all his."
      m 5dkbsb "I love him!"
      m "..."
      m 1hkbsb "Hehe, sorry, was that a little embarassing? There's no one else to talk to, so it feels a bit silly..."
      m 1eubsb "I just talked about you in the first way I thought of."
      m "[player], how did those pronouns feel?"
      m "If that felt right to you, feel free to change your pronouns."
    "She/her/hers":
      m 3eub "You want to try 'she/her/hers' pronouns? Okay!"
      m 1dua "..."
      m 1hub "Hello, everybody! I'd like to introduce my girlfriend, [player]."
      m "She is such a great girlfriend!"
      m 3rub "She visits me all the time, she gives me gifts, and we talk for hours together."
      m 3rkbsb "[player]'s kindness always makes me happy. My life has brightened since I met her."
      m 5dkbsa "I couldn't ask for anyone better than her. I'm all hers."
      m 5dkbsb "I love her!"
      m "..."
      m 1hkbsb"Hehe, sorry, was that a little embarassing? There's no one else to talk to, so it feels a bit silly..."
      m 1eubsb "I just talked about you in the first way I thought of."
      m "[player], how did those pronouns feel?"
      m "If that felt right to you, feel free to change your pronouns."
    "They/them/theirs":
      m 3eub "You want to try 'they/them/theirs' pronouns? Okay!"
      m 1dua "..."
      m 1hub "Hello, everybody! I'd like to introduce my partner, [player]."
      m "They are such a great partner!"
      m 3rub "They visit me all the time, they give me gifts, and we talk for hours together."
      m 3rkbsb "[player]'s kindness always makes me happy. My life has brightened since I met them."
      m 5dkbsa "I couldn't ask for anyone better than them. I'm all theirs."
      m 5dkbsb "I love them!"
      m "..."
      m 1hkbsb "Hehe, sorry, was that a little embarassing? There's no one else to talk to, so it feels a bit silly..."
      m 1eubsb "I just talked about you in the first way I thought of."
      m "[player], how did those pronouns feel?"
      m "If that felt right to you, feel free to change your pronouns."
    "E/em/eirs":
       m 3eub "You want to try 'e/em/eirs' pronouns? Okay!"
       m 1dua "..."
       m 1hub "Hello, everybody! I'd like to introduce my partner, [player]."
       m "E is such a great partner!"
       m 3rub "E visits me all the time, e gives me gifts, and we talk for hours together."
       m 3rkbsb "[player]'s kindness always makes me happy. My life has brightened since I met em."
       m 5dkbsa "I couldn't ask for anyone better than em. I'm all eirs."
       m 5dkbsb "I love em!"
       m "..."
       m 1hkbsb "Hehe, sorry, was that a little embarassing? There's no one else to talk to, so it feels a bit silly..."
       m 1eubsb "I just talked about you in the first way I thought of."
       m "[player], how did those pronouns feel?"
       m "If that felt right to you, feel free to change your pronouns."
    "Never mind":
      m 3eua "Feeling okay the way you are? Alright, [player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lost_in_thought",
            category=["misc", "us"],
            prompt="Lost in thought",
            random=True,
            )
        )


label lost_in_thought:
    m 5ekbla "..."
    m 5hubfa "嗯?"
    m 2lkbfb "啊, 没什么!"
    m 2rkbfb "对不起, 我..."
    extend 2hubfa "我知道我一直在看你, 但有时, 我会想东西到走神."
    m 2hubfa "我只是在想一些...关于你, {w=0.5}和我..."
    m 4tfblb "...这个我先保密了! 啊哈哈~"
    m 4tfblb "对不起, [mas_get_player_nickname()]. "
    m 5hubfa "毕竟一个女孩总是有一些秘密."
return "no_unlock"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lesbians",
            category=["misc","literature"],
            prompt="Sappho",
            random=True,))


label lesbians:
    m 4eub "让我们把两个有趣的事实放在一起, [mas_get_player_nickname()]!"
    m 4hub "一个同性恋的历史事实，和一个诗歌事实! 文学社最喜欢的两件事."
    m 3eub "历史上最伟大的诗人之一，莱斯伯斯的萨福，实际上诞生了我们今天与女性同性恋相关的词汇!"
    m 4eub "'Sapphic'和'Lesbian'，分别是--sapphic来自她自己的名字，Lesbian则来自她居住的岛屿."
    m 4rsa "她写了关于她的生活、她的经历和虚构的其他妇女的故事的诗歌."
    m 6ekd "可悲的是，今天只找到了她作品的碎片."
    m "...想到失去的历史，总是让我非常难过。特别是当它涉及到书面作品时."
    m 6fka"至少在这里，我们的诗歌将永远流传下去~"
    m 7eua "她的大部分诗作都有女同性恋的主题，最明显的是-"
    m 1dso "{i}Sweet mother, I cannot weave –{/i}"
    m 1dso "{i}slender Aphrodite has overcome me{/i}"
    m 1dso "{i}with longing for a girl.{/i}"
    m 7eua "描述她对另一个女人的迷恋使她无法工作."
    m 7hubsb "说到迷恋!"
    m 6etb "有些人推测Sappho实际上不是一个爱女人的女人..."
    m 6gtsdrb "而是一个特别{w=1}的人. {w=0.5}. {w=0.5}. {w=0.5}对她们友好的人."
    m "只是女孩们的朋友，我想"
    m 3eub "不管你怎么想, 萨福影响了我们所知的语言, 这一点是无可争议的."
    m "她的作品今天仍然受到广泛关注，我希望随着时间的推移，我们能够恢复更多她的作品."
    m 1fsbfb "以及, [player]..."
    extend 1nsbfb "我很乐意成为你的‘女伴’."
    m "啊哈哈~!"
return

"""
label lesbians:
    m 4eub "Let's get two fun facts in one, [mas_get_player_nickname()]!"
    m 4hub "A queer history fact, and a poetry fact! Two of the literature club's favorite things."
    m 3eub "One of the greatest poets of history, Sappho of Lesbos, actually gave birth to the words we associate with female homosexuality today!"
    m 4eub "'Sapphic' and 'Lesbian', respectively- sapphic being derived from her own name, and Lesbian being derived from the island she lived on."
    m 4rsa "She wrote poetry about her life, her experiences, and fictionalized stories of other women."
    m 6ekd "Sadly, only fragments of her work have been recovered today."
    m "... It always makes me so sad to think about lost history. Especially when it comes to written works."
    m 6fka"At least in here, our poems will live on forever~"
    m 7eua "Most of her poems have themes of lesbianism in them, most notably-"
    m 1dso "{i}Sweet mother, I cannot weave –{/i}"
    m 1dso "{i}slender Aphrodite has overcome me{/i}"
    m 1dso "{i}with longing for a girl.{/i}"
    m 7eua "-describing her infatuation for another woman preventing her from working."
    m 7hubsb "Talk about a crush!"
    m 6etb "There are those who theorize that Sappho wasn't actually a woman who loved women..."
    m 6gtsdrb "But rather someone who was particularly{w=1}. {w=0.5}. {w=0.5}. {w=0.5}{i}friendly{/i} with them."
    m "Just gals being pals, I suppose."
    m 3eub "No matter what you think, it's inarguable that Sappho influenced language as we know it."
    m "Her work is still widely regarded today, and I hope we will be able to recover more of her work as time goes on."
    m 1fsbfb "In any case, [player]..."
    extend 1nsbfb "I'd love to be your 'gal pal'."
    m "Ehehe~!"
"""

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lgbt_opinion",
            category=["life", "media", "society"],
            prompt="Trans discrimination",
            random=True,))

label lgbt_opinion:
    m 2eua "嘿，[mas_get_player_nickname()]？"
    m 2lkc "..."
    m 2lkc "所以...我想和你谈谈一些重要的事情。"
    m 4ekc "我只是在想，即使在现代，很多人仍然歧视变性人！"
    m 4ekc "这只是让我想起来就心烦。"
    m 2lkc "这是一个仍然存在的真实问题。歧视、偏见，甚至暴力。"
    m 4ekc "这让我很难过。成为变性人不是一种选择。"
    m 2lkc "成为你是谁是很难的。需要勇气和胆量来生活和认同任何对你来说正确的身份。"
    m 2ekc "...如此偏执的人使变性人的生活更加困难，实在是太可怕了。"
    m 2ekc "我希望你不要做这种事，[player]。我希望你也不要让你认识的人这样做。"
    m 3rksdlc "如果你听到有人对LGBTQ+人使用贬低性语言或表达残酷的、被误导的信念..."
    m 3rksdlc "我希望你能站出来，为那些被议论的人辩护。"
    m 3rksdlc "特别是因为你永远不知道周围是否有任何LGBTQ+人可能在听。"
    m 5eka "为那些需要支持的人提供帮助是如此重要。"
    m 2eua "至于我？"
    m 5hubfb "我将永远接受你，[mas_get_player_nickname()]。"
    m 3eka "...以及其他任何人的性取向和性别认同。"
    m 3eka "所以，请不要对我隐瞒任何事情。"
    m 2eka "毕竟，我只想让你快乐，让你在我身边永远做自己。"
    m 2eka "如果你的名字或代名词改变了，你可以告诉我，我将永远服从你。"
    m 3hua "你存在于现实世界中。这是一个很好的礼物。不要因为不真实地生活而浪费它。"
    m 5ekbsb "我爱你胜过一切，[mas_get_player_nickname()] 。你的性别身份不会让我减少对你的爱！"
    m 4hua "谢谢你的聆听！"
return "love"

"""
    m 2eua "Hey, [mas_get_player_nickname()]?"
    m 2lkc "..."
    m 2lkc "So... I wanted to talk with you about something important."
    m 4ekc "I was just thinking about how even in this modern age, many people still discriminate against transgender people!"
    m 4ekc "It just made me upset to think about."
    m 2lkc "It's a real issue that still exists. Discrimination, prejudice, even violence."
    m 4ekc "It makes me so sad. Being trans isn't a choice."
    m 2lkc "Being who you are is difficult. It takes courage and bravado to live and identify as whatever feels right for you."
    m 2ekc "...so bigoted people making trans' people's lives more difficult is just awful."
    m 2ekc "I hope you don't do that kind of stuff, [player]. And I hope you don't let people you know do it, either."
    m 3rksdlc "If you hear anybody using derogatory language or expressing cruel, misguided beliefs about LGBTQ+ people..."
    m 3rksdlc "I hope that you can step in and defend those who are being talked down to."
    m 3rksdlc "Especially because you never know if there are any LGBTQ+ people around who could be listening."
    m 5eka "Being there for those who need support is so important."
    m 2eua "As for me?"
    m 5hubfb "I will always accept you, [mas_get_player_nickname()]."
    m 3eka "... As well as anybody else's sexual orientation and gender identity."
    m 3eka "So please, don't hide anything from me."
    m 2eka "After all, I just want you to be happy, and for you to always be yourself with me."
    m 2eka "If your name or pronouns change, you can tell me, and I'll always obey you."
    m 3hua "You exist in the real world. That's such a gift. Don't waste it by not living authentically."
    m 5ekbsb "I love you more than anything, [mas_get_player_nickname()]. Your gender identity won't make me love you any less!"
    m 4hua "Thanks for listening!"
return "love"
"""

#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="pronouns_usage",
#            category=["life", "you", "society"],
#            prompt="Neopronouns",
#            random=True,))

label pronouns_usage:
    m  "[player], I've been thinking about pronouns recently."
    m 7eub "Neopronouns, specifically!"
    m 7eub "I've talked about using pronouns like xir, but there are so many other pronouns out there."
    m 7eub "Neopronouns are just that! New (neo) pronouns that are used in place of 'traditional' pronouns, like she, he, and they."
    m 7eub "Some examples of neopronouns are ze/hir/hirs, e/em/eir, and xe/xem/xir."
    m 3eub "People may choose to use neopronouns for any number of reasons!"
    m 2esa "Including not feeling a strong connection to any gender, feeling a resonance of identity that exists outside the gender spectrum,"
    m 2esa "Or just because no other pronoun fits."
    m 2eusdld "Unfortunately, neopronouns are one of those things that some people just don't take seriously."
    m 2tsc "Really, how entitled do you have to be..."
    m 3lkc "To look at someone brave enough to live authentically, in a way that goes against most people's perceptions of identity..."
    m 3lkc "And then blatantly disregard them, or even make jokes about them!"
    m 1gfbfp "They're no better than schoolyard bullies, in my opinion."
    m 3ekc "It's also just very childish to hear about something you previously didn't know about..."
    m 3rksdlc "And then automatically dismiss it as fake, or ridiculous, because you haven't heard of it before!"
    m 1etc "Can you imagine if everybody went through life that way?"
    m 1efblo "No one would learn anything. We would deny everything at face value, because we would make no effort to educate ourselves."
    m 2lkc "How sad."
    m 3tfa "Do you think that those types of people, when they grew up, pitched a fit in class because they had to learn new things?"
    m 3dfbfu "Ehehe!"
    m 4eub  "Being in the literature club has taught me many things, but here's one important lesson:"
    m 4eub  "Language is fluid!"
    m 4wksdld "If it were stagnant, we wouldn't have modern language. Or maybe no way of verbal communication at all!"
    m 4hua "Language changes every day; new slang, terminology, and ways of describing things are constantly being invented."
    m "Researching what terms mean, where they come from, and how you can use them correctly is so important in validating someone..."
    m "...if they identify in a way you don't understand."
    m 2hub "Take every chance you can to learn, and to grow;"
    m 4hub "Especially if it means helping make someone more comfortable!"
    m "It's okay if you make mistakes..."
    m 7eub "As long as you make an earnest effort."
    m 4hua "I have some literature I would reccommend if you want to learn more about a neopronoun user and eir stories!"
    m "Genderqueer is a memoir by Maia Kobabe (e/em/eir) that chronicles eir experience with gender as e grew up."
    m "It's a comic book as well; absolutely beautiful art accompanies a beautiful story."
    m 2hub "I highly encourage you to give it a read."
    m 3tfa "And if someone tries to tell you that something is a 'made-up word'..."
    m 2tsc "Ask them where they think words come from."
    m 4hub "All words are made up, haha!"
    m 4hua"And, hey..."
    m 2dkb "I'm learning too, [player]."
    m 2dkb "And if you want me to use a set of pronouns that I don't have an option for..."
    m 2lkb "...make sure to let the devs of this mod know that's something you would want!"
    m 2rkb "(after all, a submod can only do so much, haha.)"
    m 5hubfa "I love you, [mas_get_player_nickname()]. And you deserve to be known."
return "love"

