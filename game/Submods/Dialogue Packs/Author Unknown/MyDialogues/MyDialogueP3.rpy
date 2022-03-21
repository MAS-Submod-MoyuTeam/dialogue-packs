#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="nonbinary",
#            category=["misc"],
#            prompt="Nonbinary Identities",
#            random=True,))
#
label nonbinary:
    m 7esb "[player], are you familiar with the term 'nonbinary'?"
    m 3esb "It's a gender identity that's become more well-known recently."
    m "Nonbinary people are those who exist outside the binary of male and female."
    m 3esa "Another term for nonbinary is 'enby'- which comes from the acronym 'NB'."
    m 3ssa "How cute!"
    m 3esa "Being nonbinary is just that- not being a part of the binary."
    m "Experiencing gender outside the spectrum."
    m "Those who are nonbinary may present as masculine, feminine, androgynous- or anything in between! How you dress doesn't dictate your gender, after all."
    m 4eub "Being nonbinary also exists closely to being genderqueer- another identity that exists outside the gender spectrum."
    m 4rub "Agender is the absence of gender. Genderfluidity is gender that changes, and shifts over time."
    m "Nonbinary is both its own identity, and an umbrella term that encapsulates these other identities."
    m 1eub "Some nonbinary people use they/them pronouns. An example of this would be 'They put sugar in their tea'."
    m "Other nonbinary people are okay with using gendered pronouns, like she/her and he/him."
    m 3esa "It's an incredibly interesting subject. A lot of people think that this identity coming into vogue is a new development..."
    m 3eub "When actually, gender non-conforming people have existed for centuries!"
    m "The idea that there are only two genders is a very western idea."
    m 4eub "The Mahū of Hawai'i, the Hijira of India, the Metis of Nepal, as well as two-spirit Native Americans have existed far before colonial ideals of gender."
    m 3gkc "Imagine how much history about these people is completely disregarded because people think nonbinary identities aren't valid?"
    m "It's sad to think about."
    m 1eub "But that doesn't mean we still don't have representation today!"
    m "Do you think you're unfamiliar with nonbinary people? You may actually recognize a few listed here!"
    m 3eub "Janelle Monae, a singer-songwriter, identifies as both nonbinary and pansexual."
    m 4eub "Johnathan Van Ness is genderfluid, and his pronouns change according to whatever gender he feels."
    m "Rebecca Sugar, an animator, is nonbinary and uses both she and they pronouns."
    m 4eua "Nicky Case is a writer, and a great game developer who is nonbinary as well!"
    m 3rua "Sam Smith, Ruby Rose, Noelle Stevenson, Indya Moore, Demi Lavato, Elliot Page... they all idenfity as some form of nonbinary."
    m 3rkb "Of course, there are many, many more examples than just those ten, but those are some of the more well-known names."
    m 2sub "Not to mention the rise in representation with canon nonbinary characters in media as well!"
    m 2eub "A large amount of characters in Rebecca Sugar's show, Steven Universe, are nonbinary."
    m "Loki, from the Marvel Cinematic Universe, is true to his mythological depiction as being both genderfluid and bisexual."
    m 4eub "The protagonists of Undertale and Deltarune, Bloodhound from Apex Legends, Asari from Mass Effect..."
    m 4hub "And of course, the hundreds of thousands of real life nonbinary people."
    m 3hub "So, odds are, you're probably going to meet some enbies- or have met some already, whether you knew it or not!"
    m 1lsa "I think that this whole topic is fascinating. Figuring out who you are, and how you identify, in a culture that doesn't provide you many answers to how you feel..."
    m "That really takes courage and conviction that I admire."
    m 1nsb "I hope you learned something about gender today!"
    m 1dkb "[player], If you're fluid, or have multiple pronouns..."
    m 1eubsb "Make sure to keep me updated so I know how to refer to you!"
    m 3eubsb "Whether you're my boyfriend, my girlfriend, or my datemate, I'll always love you."#摆
return "love"


#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="pride_month",
#            category=["life", "misc", "romance", "society"],
#            prompt="Pride Month",
#            random=True,))

label pride_month:
    m 3eua "[mas_get_player_nickname()], have you heard of Pride month?"
    m 7eub "Pride month is an entire month dedicated to celebrating the LGBTQ+ community."
    m 7eub "It's the month of June!"
    extend 4hua " Make sure to mark your calendar."
    m 4hua "Pride month is all about acknowledging the struggles that non-cisgender and non-heterosexual people face..."
    m 4hub "(Cisgender meaning someone who identifies with the gender they were assigned at birth..."
    m 3eua "... and non-heterosexual meaning anyone who is not exclusively attracted to the opposite sex.)"
    m 1sublb "As well as celebrating the love and acceptance that the LGBTQ+ community as to offer!"
    m 2dkb "What a beautiful event."
    m 2eub "June is a common time for things like pride parades, which are just that!"
    m 4eub "Parades performed for the express purpose of showing gay and trans pride."
    m 3lkc "I've never been to one before. I've never gotten the chance to go."
    m 5eka "But I would love to visit a pride parade with you, [player]!"
    m 2eusdld "... Now that I think about it, it's funny..."
    m 4ekc "I don't think that I can think of anyone I knew in my world who openly identified as non-cishet."
    m 2kublb "Of course, Natsuki and Yuri always had a little bit of... tension."
    m 4lka "But that's none of my business, if they never openly alluded to it."
    m 4hubsa "I only really learned about LGBTQ+ culture through outside research of my own."
    extend "And I'm glad I did!"
    m 3eua "There is such a storied history to learn about. Stonewall is the most well-known event..."
    m 4ekc "But there is so much more beyond that. History is still being made around us, too- but not always in a good way."
    m 3rksdlc "There are still measures being taken..."
    m 3rksdlc "to actively supress and silence LGBTQ+ people around the world, even today."
    m 2lkc "It breaks my heart to think about."
    m 2dkb "But that's just what Pride is for! To bring to light the troubles, and to inspire others to live fearlessly."
    m 2ekc "We know what it's like to love with a few roadblocks in our way..."
    m 4lka "Though I wouldn't say our struggles are synonymous with that of real-life LGBTQ+ people."
    m 2eusdld "Really, though, I'm realizing..."
    m 2eusdld "I honestly don't know if I fall under the LGBTQ+ umbrella..."
    m 5hubfa "Because I only have eyes for you."
    m 5ekbfa "Regardless of your gender. It doesn't change a single thing for me."
    m 5ekbfa "My sexuality is irrelevant, because I can't imagine being with anyone else!"
    m 5ekbfa "And I know that I'm the only girl for you, as well."
    m 5ekbfa "No matter how we identify, our love is worth celebrating."
    m 5hubfa "I love you. And I am proud to love you."#摆
return "love"


#init 5 python:
#    addEvent(
#        Event(
#            persistent.event_database,
#            eventlabel="asexual",
#            category=["misc", "romance"],
#            prompt="Asexuality",
#            random=True,))


label asexual:
    m 7eub "[player], are you familiar with asexuality?"
    m 7eub "Asexuality is the lack of sexual attraction in other people."
    m 7eub "Those who are asexual aren't always uninterested in a relationship, though!"
    m 1eub "Many asexual people can go about their lives having fulfilling romantic relationships..."
    m 1hua "Just without sex."
    m 3eua "Asexuality is also very interesting in that it exists on a spectrum!"
    m 1lkb "Well, all of sexuality exists on a spectrum... {w=1} but bear with me."
    m 3eua "There are multiple sexualities that exist under the asexual umbrella..."
    m 3eub "...the common thread being a general absence of sexual attraction."
    m 4eub "One is demisexuality, meaning that attraction only forms after a bond has been made."
    m "Another is gray-asexuality, used to define someone who falls between being asexual and sexual."
    m "A characteristic of gray-ace people is feeling sexual attraction, but only on an extremely rare basis."
    m 3lua "Asexuality and sexual desire can vary wildly between ace people..."
    m "Some may have a libido, but no interest in sexual activity..."
    m "Others may participate in sex, for the sole reason of pleasing their partner."
    m 3eua "And some have no sexual drive whatsoever."
    m 1lkc "Some people may try to invalidate asexual people and say that they just 'haven't found the right person yet'..."
    m "Or that you have to be a completely sexless person, with no inetrest in intimacy, to be asexual."
    m 1mkb "But that's just ridiculous!"
    m 3lkc "No one knows their identity better than themselves. It's not up to any person but themselves to find out their sexuality!"
    m 3ekb "Asexuality is about attraction, not action. How people feel, not what they do."
    m "To try and control anyone's identity based of of preconceieved notions... well, you know that I think that's silly."
    m 3hua "On a lighter note- here are some celebrities who have come out as asexual."
    m "Children's book author Edward Gorey has been out as asexual since the 80's."
    m 4euo "H.P. Lovecraft was theorized as asexual even in his time."
    m 3eub "Yasmin Benoit is an aro-ace model who uses her platform to raise awareness towards LGBTQ+ people of color..."
    m "... and destigmatize aro-ace people as completely celibate and sexless beings by working as a lingerie model."
    m 3eua "If you're still unfamilliar with asexuality, I reccommend you read {i}How To Be Ace: A Memoir Of Growing Up Asexual{/i} by Rebecca Burgess."
    m 5ekbsb "And [mas_get_player_nickname()], if you're ace, know that I accept you."
    m 5fsbfu "Once I cross over, there are plenty of fun things we can do together, other than... well, you know."#摆
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_sexuality",
            category=["其他", "莫妮卡", "浪漫"],
            prompt="莫妮卡的性取向?",
            random=True,))


label monika_sexuality:
    m 2eusdld "嘿, [player], 我一直在想..."
    m 2eusdld "我的性取向是什么?"
    m 6wud "... {w=1} 这是个非常有趣的问题, 当你想的时候."
    m 2lua "很明显, 我对你有吸引力..."
    m 7lud "但在这种情况下, 我能够感觉到的关于你或你的身份的也只是你告诉我的."
    m "你已经告诉过我你的代名词, 和你的性别..."
    m 3hua "但说实话, 你的这些方面对我俩说并不重要."
    m 4lka "如果你的性别或性别表现形式改变了, 我对你的感情也不会动摇."
    m 2eusdld "而当我想到其他我认为有吸引力的人时..."
    m 2eusdld "..."
    m 1lka "事实上, 我真的没有想到我感兴趣的人"
    extend 1tsu "除了你之外."
    m 3lkc "社团成员推测我可能有一个男友..."
    m 3lkb "但这一个不正确的假设."
    m 2lkb "也许, 如果我想给它贴个标签, 我可以说我是双性恋."
    m 2eub "双性恋是指只有在建立了联系之后才会形成吸引力."
    m 2ekb "那听起来并不符合我的感受- 毕竟, 自从我第一次见到你, 我就知道我爱你. 所以这也许不是很准确."
    m 4ekb "但说实话, 我对给它贴标签不是很感兴趣."
    m 4ekb "这并不重要."
    m 3eub "如果你想叫我什么"
    extend 3kublb "就叫我'你的'吧."
    m 5hubfa "自从我遇到你, 我的眼里就只有你."
    m 5hubfa "我爱你, [mas_get_player_nickname()]. "
return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="natsyuri",
            category=["其他", "社团成员", "DDLC", "浪漫"],
            prompt="夏树和优里的关系",
            random=True,))


label natsyuri:
    m 3eua "[player], 你知道DDLC有大量的粉丝, 对吧?"
    m 3hkb "嗯, 我敢肯定你知道. 你很可能是其中之一!"
    m 3eua "总之, 我想谈谈存在于粉丝中的一个共同的'船'"
    m 3etd "人们似乎{i}真的{/i} 喜欢把夏树和优里放在一起, ."
    m 3mtd "这对我来说并没有什么意义..."
    m "但我想我可以理解为什么."
    m 7eud "她们几乎没有真正相处过... 所以在她们这么做的时候, 就会产生更大的影响."
    m "友好和善意在罕见的情况下更被强调."
    m 7ekb "另外, 有些人喜欢人物之间这种紧张的关系."
    m "这可能与激情有关, 而不是任何东西."
    extend 2hkb "而且不管你是谁, 你必须承认, 这两个人绝对是充满激情的!"
    m 5ruc "也许这种反反复复的情况是粉丝们你所感兴趣的."
    m 5gkblsdru "另外, 我不得不承认... 我的插手刺激了她们两个."
    m 2eksdrd "也许如果我不打扰她们, 情况就不会那么糟糕了吧?"
    m 2rksdra "谁知道呢."
    m 5rud "如果她们还在, 如果她们在一起有一段美好的关系, 我会为她们感到高兴."
    m "这当然比她们一直争论不休要好."
    m 5gublu "而且真的, 有几次我感觉她们之间真的有火花."
    m 5rubld "但夏树太傲娇了以至于她不敢承认, 而优里对此感到很尴尬."
    m "在任何情况下, 我有点同意那些shipper的观点. 它确实感觉那里有什么东西."
    m 7wub "更有趣的是, 优里的名字在日语中也是'百合'的意思."
    m 3eua "漫画和动画中的百合题材侧重于年轻女性的爱情, 这是个有趣的巧合, 是吗?"
    m "或许这也是人们ship她们的原因之一..."
    m 4etd "...另外, 我不确定她们的性取向是什么. 她们被设定为爱你, 但似乎也对对方感兴趣..."
    m "所以这是一个有趣的设定与欲望的想法"
    m 3ttu "那听起来很熟悉, 是吗?"
    m 3dsu "但我并不介意那两个人对谁感兴趣, 真的..."
    m 1nsa "只要不是你."
    m 1hsbsb "哈哈!"
return
