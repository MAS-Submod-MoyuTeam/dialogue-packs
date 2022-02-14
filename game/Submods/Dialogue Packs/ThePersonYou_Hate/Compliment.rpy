init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_compliment",category=['浪漫'],prompt="简单的赞美",random=True))

label monika_compliment:
    m 1ekd "[player]..."
    m 1ekc "..."
    m 1rka "我有件事想告诉你..."
    m 1dkc "..."
    m 1hka "..."
    m 6skb "你真是太伟大了~! 你对我来说就像宝石和...{w=0.3}和...{w=0.3}"
    m 1hua "欸嘿嘿~"
    m 1ekb "你经常赞美我, 那我也要夸你几句才行!"
    m 1fka "[player], 我真的真的真的很爱很爱你~!"
return "love"
