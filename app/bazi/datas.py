# -*- coding: utf-8 -*-

import collections
from bidict import bidict

from .ganzhi import *

xingxius = {
    0: ('角', ""),
    1: ('亢', ""),
    2: ('氐', ""),
    3: ('房', ""),    
    4: ('心', ""),
    5: ('尾', ""),
    6: ('箕', ""),
    7: ('斗', ""),   
    8: ('牛', ""),
    9: ('女', ""),
    10: ('虚', ""),
    11: ('危', ""), 
    12: ('室', ""),
    13: ('壁', ""),
    14: ('奎', ""),
    15: ('娄', ""),    
    16: ('胃', ""),
    17: ('昴', ""),
    18: ('毕', ""),
    19: ('觜', ""),    
    20: ('参', ""),
    21: ('井', ""),
    22: ('鬼', ""),
    23: ('柳', ""),   
    24: ('星', ""),
    25: ('张', ""),
    26: ('翼', ""),
    27: ('轸', ""),      
}

jianchus = {
    0: ('建', "气专而强，宜官府公事等。 宜：赴任、祈福、求嗣、求财、交涉、出行。 忌：上梁、嫁娶、安葬。"),
    1: ('除', "除旧布新的日子。 宜：祭祀、祈福、嫁娶、出行、入宅、动土、开光、交易。 忌：嫁娶、探病。"),
    2: ('满', "丰收之意。 宜：嫁娶、祈福、出行、安床、求财、裁衣、祭祀。 忌：造葬、赴任、求医。"),
    3: ('平', "普通的日子。 宜：修造、粉刷墙壁、修补。 忌：出行。"),    
    4: ('定', "月令三合的日子。 宜：祭祀、祈福、嫁娶、造屋、求嗣、纳财。 忌：诉讼、出行、交涉。"),
    5: ('执', "守成之意。 宜：纳采、嫁娶、动土、入殓。 忌：入宅、开市。"),
    6: ('破', "日月相冲，曰大耗，诸事不宜。 宜：破屋坏垣 忌：不宜诸吉事。"),
    7: ('危', "吉事不取的日子。 宜：入殓、破土、火化、进塔、安葬。 忌：入宅嫁娶诸吉事。"),   
    8: ('成', "月支的三合日，吉神的日子。 宜：结婚、开市、修造、动土、安床、破土、安葬、搬迁、交易、求财、出行、立契、竖柱、裁种、牧养。 忌：诉讼。"),
    9: ('收', "收成、收获的日子。 宜：祈福、求嗣、赴任、嫁娶、安床、修造、动土、求学、开市、交易、买卖、立契。 忌：破土、安葬。"),
    10: ('开', "重新开展的好日子。 宜：祭祀、祈福、开光、入宅、嫁娶、上任、修造、动土、开市、安床、交易、出行、竖柱。 忌：诉讼、安葬。"),
    11: ('闭', "闭藏的日子 宜：安门、伐木、修造、动土。 忌：出行、嫁娶。"), 
}


nayins = {
    ('甲', '子'): '海中金', ('乙', '丑'): '海中金', ('壬', '寅'): '金泊金', ('癸', '卯'): '金泊金',
    ('庚', '辰'): '白蜡金', ('辛', '巳'): '白蜡金', ('甲', '午'): '砂中金', ('乙', '未'): '砂中金',
    ('壬', '申'): '剑锋金', ('癸', '酉'): '剑锋金', ('庚', '戌'): '钗钏金', ('辛', '亥'): '钗钏金',
    ('戊', '子'): '霹雳火', ('己', '丑'): '霹雳火', ('丙', '寅'): '炉中火', ('丁', '卯'): '炉中火',
    ('甲', '辰'): '覆灯火', ('乙', '巳'): '覆灯火', ('戊', '午'): '天上火', ('己', '未'): '天上火',
    ('丙', '申'): '山下火', ('丁', '酉'): '山下火', ('甲', '戌'): '山头火', ('乙', '亥'): '山头火',
    ('壬', '子'): '桑柘木', ('癸', '丑'): '桑柘木', ('庚', '寅'): '松柏木', ('辛', '卯'): '松柏木',
    ('戊', '辰'): '大林木', ('己', '巳'): '大林木', ('壬', '午'): '杨柳木', ('癸', '未'): '杨柳木',
    ('庚', '申'): '石榴木', ('辛', '酉'): '石榴木', ('戊', '戌'): '平地木', ('己', '亥'): '平地木',
    ('庚', '子'): '壁上土', ('辛', '丑'): '壁上土', ('戊', '寅'): '城头土', ('己', '卯'): '城头土',
    ('丙', '辰'): '砂中土', ('丁', '巳'): '砂中土', ('庚', '午'): '路旁土', ('辛', '未'): '路旁土',
    ('戊', '申'): '大驿土', ('己', '酉'): '大驿土', ('丙', '戌'): '屋上土', ('丁', '亥'): '屋上土',
    ('丙', '子'): '涧下水', ('丁', '丑'): '涧下水', ('甲', '寅'): '大溪水', ('乙', '卯'): '大溪水',
    ('壬', '辰'): '长流水', ('癸', '巳'): '长流水', ('丙', '午'): '天河水', ('丁', '未'): '天河水',
    ('甲', '申'): '井泉水', ('乙', '酉'): '井泉水', ('壬', '戌'): '大海水', ('癸', '亥'): '大海水',    
}

empties = {
    ('甲', '子'): ('戌','亥'), ('乙', '丑'):('戌','亥'), 
    ('丙', '寅'): ('戌','亥'), ('丁', '卯'): ('戌','亥'), 
    ('戊', '辰'): ('戌','亥'), ('己', '巳'): ('戌','亥'),
    ('庚', '午'): ('戌','亥'), ('辛', '未'): ('戌','亥'),
    ('壬', '申'): ('戌','亥'), ('癸', '酉'): ('戌','亥'),

    ('甲', '戌'): ('申','酉'), ('乙', '亥'): ('申','酉'),
    ('丙', '子'): ('申','酉'), ('丁', '丑'): ('申','酉'),
    ('戊', '寅'): ('申','酉'), ('己', '卯'): ('申','酉'),
    ('庚', '辰'):('申','酉'), ('辛', '巳'): ('申','酉'),
    ('壬', '午'): ('申','酉'), ('癸', '未'): ('申','酉'),

    ('甲', '申'): ('午','未'), ('乙', '酉'): ('午','未'),
    ('丙', '戌'): ('午','未'), ('丁', '亥'): ('午','未'),
    ('戊', '子'): ('午','未'), ('己', '丑'): ('午','未'), 
    ('庚', '寅'): ('午','未'), ('辛', '卯'): ('午','未'),
    ('壬', '辰'): ('午','未'), ('癸', '巳'): ('午','未'),

    ('甲', '午'): ('辰','己'), ('乙', '未'): ('辰','己'),
    ('丙', '申'): ('辰','己'), ('丁', '酉'): ('辰','己'),
    ('戊', '戌'): ('辰','己'), ('己', '亥'): ('辰','己'),
    ('庚', '子'): ('辰','己'), ('辛', '丑'): ('辰','己'),
    ('壬', '寅'): ('辰','己'), ('癸', '卯'): ('辰','己'),

    ('甲', '辰'): ('寅','卯'), ('乙', '巳'): ('寅','卯'),
    ('丙', '午'): ('寅','卯'), ('丁', '未'): ('寅','卯'),
    ('戊', '申'): ('寅','卯'), ('己', '酉'): ('寅','卯'),
    ('庚', '戌'): ('寅','卯'), ('辛', '亥'): ('寅','卯'),
    ('壬', '子'): ('寅','卯'), ('癸', '丑'): ('寅','卯'), 


    ('甲', '寅'): ('子','丑'), ('乙', '卯'): ('子','丑'),     
    ('丙', '辰'): ('子','丑'), ('丁', '巳'): ('子','丑'), 
    ('戊', '午'): ('子','丑'), ('己', '未'): ('子','丑'),
    ('庚', '申'): ('子','丑'), ('辛', '酉'): ('子','丑'), 
    ('壬', '戌'): ('子','丑'), ('癸', '亥'): ('子','丑'),    
}

ges = {
     ('庚', '子'):'飞天禄马', ('壬', '子'):'飞天禄马',
     ('辛', '亥'):'飞天禄马', ('癸', '亥'):'飞天禄马',     
}

ge_descs = {
    '飞天禄马':'''
    若逢伤官月建,如凶处,未必为凶,内有倒禄飞冲,忌官星,亦嫌羁绊。
    柱无财官,方用。又须月时或年与日同支,方能并冲。
    '''
}


lu_types = {
    "甲":{('丙','寅'):'福星禄 名位禄 吉', ('戊','寅'):'伏马禄 吉', 
           ('庚','寅'):'破禄，半吉半凶', ('壬','寅'):'正禄，带截路空亡，必为僧道 不吉',
           ('甲','寅'):'长生禄，大吉', ('乙','卯'):'生成禄，大吉',},
    "乙":{('乙','卯'):'喜神旺禄 吉', ('丁','卯'):'截路空亡 凶', 
           ('己','卯'):'进神禄 吉', ('辛','卯'):'破禄，又为交神，半吉半凶',
           ('癸','卯'):'死禄 虽贵终贫 凶',},
    "丙":{('己','巳'):'九天库禄 吉', ('辛','巳'):'截路空亡 凶', 
           ('乙','巳'):'旺马禄 吉', ('丁','巳'):'库禄 吉',
           ('癸','巳'):'伏贵神禄，半吉半凶',}, 
    "丁":{('庚','午'):'截路空亡 凶', ('壬','午'):'德合禄 吉', 
           ('甲','午'):'进神禄 吉', ('丙','午'):'喜神禄，交羊刃，半吉',
           ('戊','午'):'伏羊刃 禄，多凶',},   
    "戊":{('己','巳'):'九天库禄，吉', ('辛', '巳'):'截路空亡 凶', 
           ('癸','巳'):'贵神禄，戊癸化合，有官位重 吉', ('乙','巳'):'驿马同乡禄 吉',
           ('戊','巳'):'旺库禄 吉',},    
    "己":{('庚','午'):'截路空亡 凶', ('壬','午'):'死鬼禄 凶', 
           ('甲','午'):'进神合禄 显达之象 吉', ('丙','午'):'喜神禄 半吉',
           ('戊','午'):'伏神羊刃禄，凶',},  
    "庚":{('壬','申'):'大败禄 凶', ('甲', '申'):'截路空亡禄 凶', 
           ('丙','申'):'大败禄，多成败 半吉', ('戊','申'):'伏马禄，多滞，若值福星，贵吉',
           ('庚','申'):'长生禄，大吉',},      
    "辛":{('癸','酉'):'伏神禄，水火相犯，凶', ('乙','酉'):'破禄 成败 凶', 
           ('丁','酉'):'空亡贵神禄 丁木受气，辛水沐浴，主奸淫事；值喜神，吉。', 
           ('己','酉'):'进神禄 吉', ('辛','酉'):'正禄 吉',},    
    "壬":{('丁','亥'):'贵神合禄 吉', ('乙', '亥'):'天德禄 吉', 
           ('己','亥'):'旺禄 大吉', ('辛','亥'):'同马乡禄 大吉',
           ('癸','亥'):'大败禄，贫薄 凶',},     
    "癸":{('甲','子'):'进神禄，主登科进达 吉', ('丙','子'):'交羊刃禄，带福星，贵有权。 吉', 
           ('戊','子'):'伏羊刃合贵禄 半吉', 
           ('庚','印禄'):'进神禄 吉', ('壬','子'):'正羊刃禄，凶',},        
}


wenchang = {"甲":'巳', "乙":"亥", "丙":"戌", "丁":"辰", "戊":"申", "己":"午", 
            "庚": "寅", "辛":"未", "壬": "卯", "癸":"丑"}
wenxing = {"甲":'午', "乙":"巳", "丙":"申", "丁":"酉", "戊":"申", "己":"酉", 
           "庚": "戌", "辛":"亥", "壬": "寅", "癸":"卯"}
tianyin =  {"甲":'寅',  "乙":"亥", "丙":"戌", "丁":"酉", "戊":"申", "己":"未", 
            "庚": "午", "辛":"巳", "壬": "辰", "癸":"卯"}
xuetangs = {'金':("辛","巳"), '木':("己","亥"), '水':("甲","申"), 
            '火':("丙", "寅"), '土':("戊","申")}

# 天乙贵人，有两种分法
tianyis =  {"甲":'未',  "乙":"申", "丙":"酉", "丁":"亥", "戊":'丑', "己":"子", 
            "庚": "丑", "辛":"寅", "壬": "卯", "癸":"巳"}

# 玉堂贵人，有两种分法
yutangs =  {"甲":'丑',  "乙":"子", "丙":"亥", "丁":"酉", "戊":'未', "己":"申", 
            "庚": "未", "辛":"午", "壬": "巳", "癸":"卯"}

wangs = {"子":"亥", "丑":"申", "寅":"巳", "卯":"寅", "辰":"亥", "巳":"申", 
            "午":"巳", "未":"寅", "申":"亥", "酉":"申", "戌":"巳", "亥":"寅"}
jieshas = {"子":"巳", "丑":"寅", "寅":"亥", "卯":"申", "辰":"巳", "巳":"寅", 
         "午":"亥", "未":"申", "申":"巳", "酉":"寅", "戌":"亥", "亥":"申"}
# 存在古代现代疑问
tiandes =  {"子":"巳", "丑":"庚", "寅":"丁", "卯":"申", "辰":"壬", "巳":"辛", 
            "午":"亥", "未":"甲", "申":"癸", "酉":"寅", "戌":"丙", "亥":"乙"}
yuedes =  {"子":"壬", "丑":"庚", "寅":"丙", "卯":"甲", "辰":"壬", "巳":"庚", 
           "午":"丙", "未":"甲", "申":"壬", "酉":"庚", "戌":"丙", "亥":"甲"}
mas =  {"子":"寅", "丑":"亥", "寅":"申", "卯":"巳", "辰":"寅", "巳":"亥", 
        "午":"申", "未":"巳", "申":"寅", "酉":"亥", "戌":"申", "亥":"巳"}    
ma_zhus =  {
    ("甲","申"):'截路空日马', ("丙","申"):'截路空日马', ("戊","申"):'福星伏马', 
    ("庚","申"):'逢天关马', ("壬","申"):'大败马', 
    ("甲","寅"):'正禄文星马', ("丙","寅"):'福星马', ("戊","寅"):'伏马', 
    ("庚","寅"):'破禄马', ("壬","寅"):'截路马',   
    ("乙","亥"):'天德马', ("丁","亥"):'天乙马', ("己","亥"):'旺禄马', 
    ("辛","亥"):'正禄马', ("癸","亥"):'大败马',     
    ("乙","巳"):'正禄马', ("丁","巳"):'旺气马', ("己","巳"):'九天禄库马', 
    ("辛","巳"):'截路马', ("癸","巳"):'天乙伏马',      
}   



jianlu_desc = '''

================  建禄格 ================  比例 1/12
喜: 财、官和印绶  忌: 忌伤官和劫财；  杀不可太旺。
颇宜时带偏官、偏财或食神，更看年时上露者取用，若略见财官，反争夺不吉。
难招祖业，必主平生见财不聚，却病少寿长，行运再见比，克妻妨父损子，或官非破财，或因妻孥财帛争夺。
有财官，引旺得地，官星有助，运临官星有气之地，亦贵；财星有助，运临财旺之地，亦富；财官俱旺，乃富贵之命。
若时逢财库，运至财乡，必主晚年大富。年上财官有助，必享祖荫。
若四柱元无财官，纵运行财官之地，亦止虚花而已。命无财官，岁运又行比，一生贫蹇。
'''

jianlus = {
    ('甲', '寅'):'柱中乙卯未字多，主无祖财，[劫财]克妻，一世孤贫，作事虚诈，为人大模样',
    ('乙', '卯'):'''
    柱有庚辛巳酉丑申及戊己巳午辰戌等字，财官多则贵，壬癸申子辰亥水印成局亦佳，更运逢之尤妙''',   
    ('丙', '巳'):'岁时干支水金成局，运历财官旺地，亦主富贵。',    
    ('丁', '午'):'''
    金败水绝，财[庚-沐浴]官[壬-胎]俱背，顺运克妻，逆运克三妻，若柱有巳酉丑庚辛壬癸亥申子辰，
    运临财官旺地亦发，用煞或印，以多为贵，若止建禄，亦同前断。''',
    ('戊', '巳'):
    '''年日时无水，主克妻[癸-胎]，无祖业，子[病]多不肖，柱中多有官则吉，如见偏官，主尊贵，
    岁月若是火多及或印绶，虽无财官，主吉，若柱内隐显壬癸亥申子辰水局，晚子一二，
    有甲寅乙卯亥未木局，运至财官旺地亦发。''',   
    ('己', '午'):'''
    以壬水为财，五月水囚[壬-胎]，主无祖业，克妻，子[乙-长生]亦不多，
    岁时透出寅甲为正官，五月甲死，官必卑小，喜见亥卯未乙，身旺见官煞为妙，偏财亦美。''',
    ('庚', '申'):'''
    上旬生，近木余气，略无祖财，虽节气临水绝之乡，尚有三四分库财为福，运至丙戌，财尽矣，
    若年日时多带财，好命看，见丙丁巳午寅戌火局则有官，以煞化官也，官小亦不清显，怕壬癸亥子，克官不成。''',

    ('戊', '巳'):
    '''年日时无水，主克妻[癸-胎]，无祖业，子[病]多不肖，柱中多有官则吉，如见偏官，主尊贵，
    岁月若是火多及或印绶，虽无财官，主吉，若柱内隐显壬癸亥申子辰水局，晚子一二，
    有甲寅乙卯亥未木局，运至财官旺地亦发。''',   
    ('己', '午'):'''
    以壬水为财，五月水囚[壬-胎]，主无祖业，克妻，子[乙-长生]亦不多，
    岁时透出寅甲为正官，五月甲死，官必卑小，喜见亥卯未乙，身旺见官煞为妙，偏财亦美。''',
    ('庚', '申'):'''
    上旬生，近木余气，略无祖财，虽节气临水绝之乡，尚有三四分库财为福，运至丙戌，财尽矣，
    若年日时多带财，好命看，见丙丁巳午寅戌火局则有官，以煞化官也，官小亦不清显，怕壬癸亥子，克官不成。''',

    ('辛', '酉'):'''
    无祖财，柱中多见分夺，孤贫[甲-胎]无妻，或克妻无财，若带木火生旺，又当富贵，原无财官，
    又行生地，其劫祸尤重，或见辛酉则为专禄，更有财官印食之神岁运再逢尤好，逆运南方则吉，
    顺运北方，百事无成，若辛卯、辛未日身自坐财，可许衣禄，辛巳日有贵，官禄亦轻。''',
                                                                                                                               
    ('壬', '亥'):'''
    无祖业，柱中多见火土，主自成立有官，如见水多泛滥，无成、克妻、贫薄。''',
                                                                                                                               
    ('癸', '子'):'''
    无祖业，柱中多见火土，主自成立有官，如见水多泛滥，无成、克妻、贫薄。''',
}

shang_guans = {
    '火': '伤尽。','金': '要见官', '木': '官要旺','土':'伤尽。', '水': '伤官木也要土'}

tianyuans = {
    '火': '主兵权，为将镇三边。',
    '金': '有重权，防御刺史臣', 
    '木': '伤衰化煞，为权势若雷',
    '土':'正禄八座三台福。', 
    '水': '入官局，可沾侍郎禄'}

lu_ku_cai = {"甲":'丑', "乙":"丑", "丙":"午", "丁":"午", "戊":"辰", "己":"辰", 
            "庚": "未", "辛":"未", "壬": "戌", "癸":"戌"}
self_zuo = {
    '官':'''''',        
    '杀':'''天元坐杀：喜旺，忌明现食伤。无官煞复克，喜印化煞，财旺身旺。为人心多性急，阴险怀毒，僭伪谋害，不近人情.
    如无助化，再行煞旺运，或再见煞克，为人必面目瘢痕，侏儒跛鳖，骈指瘤赘，奸贪猛暴，恃强不惮，累犯宪章。克重多夭，合格为武贵。''',                 
    '财':'''''',
    '才':'''''',    
    '印':'''''',
    '枭':'''''',      
    '食':'''''',
    '伤':'''''',     
    '比':'''''',
    '劫':'''''',       
}
