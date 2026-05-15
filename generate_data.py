import json
import random
import uuid

random.seed(42)

conversations = []

people = ["我", "你", "他", "她", "我们", "你们", "他们", "小明", "小红", "小李", "老师", "妈妈", "爸爸", "朋友", "同学"]
relatives = ["爸妈", "家人", "朋友", "同学", "同事", "室友", "邻居", "亲戚"]
foods = ["火锅", "烧烤", "奶茶", "炸鸡", "麻辣烫", "寿司", "披萨", "拉面", "饺子", "酸菜鱼", "小龙虾", "烤肉", "煲仔饭", "螺蛳粉", "烤鸭"]
drinks = ["可乐", "奶茶", "咖啡", "果汁", "柠檬茶", "牛奶", "酸奶", "气泡水"]
places = ["学校", "图书馆", "操场", "食堂", "教室", "宿舍", "公园", "超市", "电影院", "体育馆", "商场", "咖啡馆", "海边", "山里", "游乐园"]
sports = ["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳", "瑜伽", "跳绳", "滑板", "骑行"]
subjects = ["数学", "语文", "英语", "物理", "化学", "历史", "地理", "生物", "政治"]
music_genres = ["流行", "摇滚", "说唱", "民谣", "古典", "电子", "R&B"]
animals = ["猫", "狗", "兔子", "仓鼠", "金鱼", "乌龟", "鸟", "龙猫"]
weathers = ["晴天", "阴天", "下雨", "下雪", "刮风", "多云", "大雾"]
times = ["今天", "昨天", "明天", "周末", "下周", "放假", "晚上", "早上", "下午", "这周日", "下周一"]
feelings = ["开心", "难过", "紧张", "兴奋", "无聊", "疲惫", "期待", "焦虑", "放松", "感动"]
adjectives = ["好看", "好吃", "好玩", "好听", "舒服", "方便", "划算", "实用", "有意思", "不错"]
neg_adj = ["难吃", "难看", "无聊", "不方便", "一般般", "没意思", "浪费时间"]
movies = ["《流浪地球》", "《哪吒》", "《长津湖》", "《你好李焕英》", "《独行月球》", "《满江红》", "《唐人街探案》", "《飞驰人生》"]
games = ["王者荣耀", "原神", "和平精英", "英雄联盟", "吃鸡", "蛋仔派对", "金铲铲之战"]
courses = ["选修课", "专业课", "体育课", "音乐课", "美术课", "实验课"]
stores = ["文具店", "零食店", "服装店", "书店", "花店", "甜品店", "便利店"]
apps = ["微信", "抖音", "B站", "微博", "小红书", "知乎", "QQ"]
quantifiers = ["一点", "很多", "一些", "几个", "不少", "一大堆", "好多"]
time_phrases = ["有空的时候", "最近", "平时", "有空", "周末的时候", "放假的时候", "下课以后", "放学以后", "吃完饭以后"]

interjections = ["啊", "吧", "呢", "吗", "嘛", "哦", "呀", "哈"]

length_levels = ["short", "medium", "long"]

character_map = str.maketrans("", "", "！？，。、；：""''（）【】《》")

# ---------- template groups ----------

templates_group_opinion = [
    "我觉得{place}的{food}真的{adj}。",
    "我觉得{place}的{food}{neg_adj}。",
    "我觉得{subject}{adj}。",
    "我觉得{sport}{adj}。",
    "我觉得{movie}{adj}。",
    "我觉得{game}{adj}。",
    "我觉得{adj_thing}挺{adj}的。",
    "我个人觉得{opinion_topic}还是{adj2}一些。",
    "说实话，{opinion_topic}{neg_adj}。",
    "要我说，{opinion_topic}真的{adj}。",
    "讲真的，{opinion_topic}还不错。",
    "以我的经验来看，{opinion_topic}{adj2}一点比较好。",
]

templates_group_question = [
    "{time}你有空吗？一起去{place}走走？",
    "你知道{place}怎么走吗？",
    "你{time}去{place}吗？一起啊。",
    "{time}要不要一起去{sport}？",
    "你最近有没有看{movie}？好看吗？",
    "你玩{game}吗？加个好友呗。",
    "你{time}有什么安排吗？",
    "你知不知道{fact_question}？",
    "你能帮我{verb_action}吗？",
    "你对{opinion_topic}怎么看？",
    "你觉得{choice_a}好还是{choice_b}好？",
    "有没有人{time}想一起去{place}？",
    "你{time}有空吗？想找你聊聊天。",
]

templates_group_statement = [
    "{time}天气真好，适合出去走走。",
    "我今天心情{feeling}。",
    "我养了一只{animal}，特别调皮。",
    "{time}我们去{place}玩吧。",
    "我最近在学{skill}，还挺有意思的。",
    "我昨天看了一部电影叫{movie}，{adj}。",
    "我家附近新开了{store}，东西还不错。",
    "我{time}要考试了，有点{feeling}。",
    "我朋友送了我一个{object}，我很喜欢。",
    "我已经{quantity}天没{sport}了。",
    "{time}社团有活动，我得去参加。",
    "我在{app}上看到一个{adj}的视频。",
    "这个周末终于能好好休息了。",
    "我打算{time}去{place}旅行。",
    "我们班{person}特别{adj}。",
    "{time}的{subject}作业好多啊。",
    "我今天{adv_verb}{quantity}。",
]

templates_group_suggestion = [
    "我推荐你去尝尝{place}的{food}，{adj}。",
    "要不我们{time}去{place}吧？",
    "我建议你试试{activity}。",
    "你可以去{app}上搜一下{search_topic}。",
    "要不要试试{store}新出的{product}？",
    "你下次可以试试{method}，效果不错。",
    "我建议你{time}再去{place}，人会少一点。",
]

templates_group_complaint = [
    "今天{weather}，出门太不方便了。",
    "{subject}太难了，我完全学不会。",
    "今天的作业也太多了吧。",
    "我手机又没电了，好烦。",
    "这家{store}的{product}{neg_adj}。",
    "我在{app}上刷了半天，啥也没看到。",
    "最近太累了，每天都睡不够。",
    "这个{thing_name}{neg_adj}，后悔买了。",
]

templates_group_daily = [
    "早上好，今天吃早饭了吗？",
    "我到{place}了，你在哪？",
    "好饿啊，等会吃什么？",
    "我先走了，明天见。",
    "晚安，早点休息。",
    "你吃饭了吗？一起去食堂？",
    "今天第几节课最累？",
    "帮我带一份{place}的{food}呗。",
    "下课一起去{place}吧。",
    "你作业写完了吗？借我抄抄呗。",
    "等我一下，马上就好。",
    "你今天穿得好好看啊。",
    "你的新{object}好{adj}！",
    "刚刚那个{event}也太搞笑了吧。",
    "你不要紧张，肯定没问题的。",
    "加油，我相信你可以的！",
    "没事的，下次再努力就好。",
]

templates_group_recommend = [
    "我给你推荐一首歌叫{song_name}，{adj}。",
    "推荐一部电影{movie}，{adj}。",
    "强烈推荐{place}的{food}！",
    "你一定要试试这款{product}，真的很好用。",
    "最近发现了一家宝藏{store}，分享给你。",
]

# Word banks for slots

topics_opinion = ["这件事", "这个方案", "这种说法", "这个观点", "这种方式", "这个安排"]
adj2_list = ["靠谱", "合理", "实际", "简单", "明确", "灵活"]
adj_thing_list = ["这家店", "这个电影", "这个游戏", "这个地方", "这本书", "这个课"]
fact_questions = ["图书馆今天开不开门", "食堂几点关门", "明天要不要上课", "这次考试难不难", "学校周末有没有活动"]
verb_actions = ["拿一下快递", "带份午饭", "看看这道题", "帮我占个座", "帮我打印一下文件"]
choices_a = ["出去吃", "看电影", "打游戏", "去图书馆", "逛街"]
choices_b = ["点外卖", "逛公园", "看书", "去运动", "在家休息"]
skills = ["做饭", "弹吉他", "画画", "摄影", "编程", "跳舞", "写作", "剪辑"]
objects = ["书包", "手环", "水杯", "充电宝", "耳机", "笔记本", "台灯", "键盘"]
quantity_list = ["好几天", "一周", "半个月", "一个月", "两个月", "几周"]
adv_verb_phrases = ["吃了好多", "走了一万步", "学了三个小时", "打了半天球", "睡了一整天"]
activity_list = ["早起跑步", "晚上冥想", "每天读书半小时", "少喝奶茶", "多喝水"]
search_topics = ["好吃的火锅店", "好看的电影", "好听的歌", "旅游攻略", "学习方法"]
products = ["奶茶", "面包", "咖啡", "甜点", "套餐", "新品"]
methods = ["提前预约", "错峰出行", "用学生证买票", "网上订餐"]
thing_names = ["这个充电宝", "这个手机壳", "这双鞋", "这件衣服", "这个耳机"]
events = ["那个笑话", "刚才的事", "那段视频", "那个场面"]
song_names = ["《起风了》", "《平凡之路》", "《光年之外》", "《孤勇者》", "《稻香》", "《夜曲》", "《晴天》", "《七里香》"]
product_recos = ["耳机", "键盘", "鼠标", "台灯", "水杯", "充电宝", "手机支架"]

all_templates = (
    templates_group_opinion +
    templates_group_question +
    templates_group_statement +
    templates_group_suggestion +
    templates_group_complaint +
    templates_group_daily +
    templates_group_recommend
)

def render(tpl):
    kwargs = {}
    kwargs["person"] = random.choice(people)
    kwargs["food"] = random.choice(foods)
    kwargs["drink"] = random.choice(drinks)
    kwargs["place"] = random.choice(places)
    kwargs["sport"] = random.choice(sports)
    kwargs["subject"] = random.choice(subjects)
    kwargs["music"] = random.choice(music_genres)
    kwargs["animal"] = random.choice(animals)
    kwargs["weather"] = random.choice(weathers)
    kwargs["time"] = random.choice(times)
    kwargs["feeling"] = random.choice(feelings)
    kwargs["adj"] = random.choice(adjectives)
    kwargs["neg_adj"] = random.choice(neg_adj)
    kwargs["movie"] = random.choice(movies)
    kwargs["game"] = random.choice(games)
    kwargs["store"] = random.choice(stores)
    kwargs["app"] = random.choice(apps)
    kwargs["relative"] = random.choice(relatives)
    kwargs["course"] = random.choice(courses)
    kwargs["adj2"] = random.choice(adj2_list)
    kwargs["adj_thing"] = random.choice(adj_thing_list)
    kwargs["opinion_topic"] = random.choice(topics_opinion)
    kwargs["fact_question"] = random.choice(fact_questions)
    kwargs["verb_action"] = random.choice(verb_actions)
    kwargs["choice_a"] = random.choice(choices_a)
    kwargs["choice_b"] = random.choice(choices_b)
    kwargs["skill"] = random.choice(skills)
    kwargs["object"] = random.choice(objects)
    kwargs["quantity"] = random.choice(quantity_list)
    kwargs["adv_verb"] = random.choice(adv_verb_phrases)
    kwargs["activity"] = random.choice(activity_list)
    kwargs["search_topic"] = random.choice(search_topics)
    kwargs["product"] = random.choice(products)
    kwargs["method"] = random.choice(methods)
    kwargs["thing_name"] = random.choice(thing_names)
    kwargs["event"] = random.choice(events)
    kwargs["song_name"] = random.choice(song_names)
    kwargs["product_reco"] = random.choice(product_recos)

    result = tpl.format(**kwargs)

    if random.random() < 0.15:
        if random.random() < 0.5:
            result = result[:-1] + random.choice(["！", "？", "……"])
        else:
            punct = random.choice(["啊", "吧", "呢", "嘛", "呀"])
            result = result[:-1] + punct + result[-1]

    if random.random() < 0.1:
        prefix = random.choice(["嗯，", "其实，", "说实话，", "感觉", "我觉得", "话说回来，", "对了，", "那个，"])
        result = prefix + result[0].lower() + result[1:]

    if random.random() < 0.08:
        suffix = random.choice(["你说是不是？", "你觉得呢？", "对吧。", "真的。", "就这样。", "哈哈。", "唉。"])
        result = result.rstrip("。！？，") + "，" + suffix

    return result

target = 100000
existing = set()

while len(conversations) < target:
    tpl = random.choice(all_templates)
    sentence = render(tpl)

    dedup_key = sentence[:30]
    if dedup_key not in existing:
        existing.add(dedup_key)
        conversations.append({"text": sentence})

    if len(conversations) % 10000 == 0 and len(conversations) > 0:
        print(f"Generated {len(conversations)} / {target}")

random.shuffle(conversations)

with open("pretrain_conversation_data.jsonl", "w", encoding="utf-8") as f:
    for item in conversations:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Done! Generated {len(conversations)} sentences.")
