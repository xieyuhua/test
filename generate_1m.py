import json
import random

random.seed(42)

TARGET = 1_000_000
BATCH_SIZE = 50000

people = ["我", "你", "他", "她", "我们", "你们", "他们", "小明", "小红", "小李", "小张", "小刘", "老师", "妈妈", "爸爸", "朋友", "同学", "班长", "舍友", "闺蜜", "兄弟", "邻居", "同桌"]
relatives = ["爸妈", "家人", "朋友", "同学", "同事", "室友", "邻居", "亲戚", "发小", "队友"]
foods = ["火锅", "烧烤", "奶茶", "炸鸡", "麻辣烫", "寿司", "披萨", "拉面", "饺子", "酸菜鱼", "小龙虾", "烤肉", "煲仔饭", "螺蛳粉", "烤鸭", "串串", "米线", "凉皮", "肉夹馍", "肠粉", "煎饼果子", "小笼包", "馄饨", "热干面", "冒菜", "烤鱼", "手抓饼", "章鱼烧", "部队锅", "韩式炸鸡"]
drinks = ["可乐", "奶茶", "咖啡", "果汁", "柠檬茶", "牛奶", "酸奶", "气泡水", "冰美式", "杨枝甘露", "蜜桃乌龙", "抹茶拿铁", "椰汁"]
places = ["学校", "图书馆", "操场", "食堂", "教室", "宿舍", "公园", "超市", "电影院", "体育馆", "商场", "咖啡馆", "海边", "山里", "游乐园", "博物馆", "科技馆", "动物园", "植物园", "健身房", "游泳馆", "篮球场", "足球场", "书店", "奶茶店", "KTV", "烧烤摊", "小吃街"]
sports = ["篮球", "足球", "羽毛球", "乒乓球", "跑步", "游泳", "瑜伽", "跳绳", "滑板", "骑行", "网球", "排球", "棒球", "滑雪", "攀岩", "拳击", "跳舞"]
subjects = ["数学", "语文", "英语", "物理", "化学", "历史", "地理", "生物", "政治", "高数", "大物", "线代", "经济学", "心理学", "哲学", "艺术概论"]
music_genres = ["流行", "摇滚", "说唱", "民谣", "古典", "电子", "R&B", "爵士", "嘻哈", "古风"]
animals = ["猫", "狗", "兔子", "仓鼠", "金鱼", "乌龟", "鸟", "龙猫", "刺猬", "宠物猪", "鹦鹉", "松鼠"]
weathers = ["晴天", "阴天", "下雨", "下雪", "刮风", "多云", "大雾", "雷雨", "暴雪", "沙尘"]
times = ["今天", "昨天", "明天", "周末", "下周", "放假", "晚上", "早上", "下午", "这周日", "下周一", "周三", "周五", "周六", "下周末", "寒假", "暑假", "中秋节", "国庆节", "元旦", "春节"]
feelings = ["开心", "难过", "紧张", "兴奋", "无聊", "疲惫", "期待", "焦虑", "放松", "感动", "烦躁", "郁闷", "激动", "失落", "温暖", "幸福", "委屈", "惊喜"]
adjectives = ["好看", "好吃", "好玩", "好听", "舒服", "方便", "划算", "实用", "有意思", "不错", "超棒", "无敌", "绝了", "很赞", "惊艳", "感人", "精彩", "过瘾", "良心"]
neg_adj = ["难吃", "难看", "无聊", "不方便", "一般般", "没意思", "浪费时间", "踩雷", "后悔", "不值"]
movies = ["《流浪地球》", "《哪吒》", "《长津湖》", "《你好李焕英》", "《独行月球》", "《满江红》", "《唐人街探案》", "《飞驰人生》", "《封神》", "《八角笼中》", "《消失的她》", "《孤注一掷》", "《热辣滚烫》", "《飞驰人生2》", "《第二十条》"]
games = ["王者荣耀", "原神", "和平精英", "英雄联盟", "吃鸡", "蛋仔派对", "金铲铲之战", "星穹铁道", "绝区零", "永劫无间", "第五人格", "光遇", "我的世界"]
courses = ["选修课", "专业课", "体育课", "音乐课", "美术课", "实验课", "公开课", "通识课"]
stores = ["文具店", "零食店", "服装店", "书店", "花店", "甜品店", "便利店", "杂货铺", "潮玩店", "古着店"]
apps = ["微信", "抖音", "B站", "微博", "小红书", "知乎", "QQ", "网易云", "美团", "饿了么", "淘宝", "京东", "闲鱼"]
interjections_pre = ["嗯", "其实", "说实话", "感觉", "我觉得", "话说回来", "对了", "那个", "讲真", "不是我说", "有一说一", "客观来说", "老实讲"]
interjections_suf = ["你说是不是？", "你觉得呢？", "对吧。", "真的。", "就这样。", "哈哈。", "唉。", "懂的都懂。", "懂的扣1。", "谁懂啊。", "无语了。", "笑死。"]

def p(): return random.choice(people)
def f(): return random.choice(foods)
def d(): return random.choice(drinks)
def pl(): return random.choice(places)
def sp(): return random.choice(sports)
def su(): return random.choice(subjects)
def a(): return random.choice(animals)
def w(): return random.choice(weathers)
def t(): return random.choice(times)
def fe(): return random.choice(feelings)
def ad(): return random.choice(adjectives)
def na(): return random.choice(neg_adj)
def m(): return random.choice(movies)
def g(): return random.choice(games)
def st(): return random.choice(stores)
def ap(): return random.choice(apps)

def render():
    tid = random.randint(0, 40)

    if tid == 0:
        s = f"我觉得在{pl()}吃{f()}真的很{ad()}。"
    elif tid == 1:
        s = f"我觉得{su()}好{ad()}啊。"
    elif tid == 2:
        s = f"我觉得{sp()}挺{ad()}的。"
    elif tid == 3:
        s = f"我觉得{m()}拍得挺{ad()}的。"
    elif tid == 4:
        s = f"说实话，{g()}{na()}。"
    elif tid == 5:
        s = f"要我说，{su()}还是得好好学。"
    elif tid == 6:
        s = f"{t()}有空吗？一起去{pl()}逛逛？"
    elif tid == 7:
        s = f"你知道{pl()}怎么走吗？"
    elif tid == 8:
        s = f"{t()}要不要一起去{sp()}？"
    elif tid == 9:
        s = f"你最近有没有看{m()}？好看吗？"
    elif tid == 10:
        s = f"你玩{g()}不？加个好友一起玩啊。"
    elif tid == 11:
        s = f"{t()}有什么安排吗，一起出来玩啊。"
    elif tid == 12:
        s = f"你能帮我{random.choice(['拿个快递', '带份午饭', '看下这道题', '占个座', '打个饭', '带杯' + d()])}吗？"
    elif tid == 13:
        s = f"你觉得{random.choice(['这个方案', '这个安排', '这种方式', '这个说法'])}怎么样？"
    elif tid == 14:
        s = f"{t()}天气真好，适合出去走走。"
    elif tid == 15:
        s = f"我今天心情{fe()}。"
    elif tid == 16:
        s = f"我养了一只{a()}，特别{random.choice(['调皮', '可爱', '粘人', '聪明', '懒'])}。"
    elif tid == 17:
        s = f"{t()}我们去{pl()}玩吧。"
    elif tid == 18:
        s = f"我最近在学{random.choice(['做饭', '弹吉他', '画画', '摄影', '编程', '跳舞', '剪辑', '瑜伽'])}，还挺有意思的。"
    elif tid == 19:
        s = f"昨天看了一部{m()}，{ad()}。"
    elif tid == 20:
        s = f"我家附近新开了一家{st()}，东西还不错。"
    elif tid == 21:
        s = f"我下周要考{su()}了，有点{fe()}。"
    elif tid == 22:
        s = f"我在{ap()}上刷到一个{ad()}的视频。"
    elif tid == 23:
        s = f"我推荐你去吃{pl()}的{f()}，真的{ad()}。"
    elif tid == 24:
        s = f"要不我们{t()}去{pl()}吧？"
    elif tid == 25:
        s = f"强烈推荐{pl()}的{f()}！"
    elif tid == 26:
        s = f"今天{w()}，出门好不方便。"
    elif tid == 27:
        s = f"{su()}太难了吧，完全学不会。"
    elif tid == 28:
        s = f"今天的作业也太多了吧。"
    elif tid == 29:
        s = f"好饿啊，等会去吃{random.choice(['食堂', '外卖', f()])}吧。"
    elif tid == 30:
        s = f"你吃饭了吗？一起去食堂？"
    elif tid == 31:
        s = f"帮我带一份{pl()}的{f()}呗。"
    elif tid == 32:
        s = f"下课一起去{pl()}啊。"
    elif tid == 33:
        s = f"你作业写完了吗？借我参考一下呗。"
    elif tid == 34:
        s = f"你今天穿得好好看啊，在哪买的？"
    elif tid == 35:
        s = f"加油，我相信你一定可以的！"
    elif tid == 36:
        s = f"没事的，下次再努力就好了。"
    elif tid == 37:
        s = f"我给你推荐一首{random.choice(['《起风了》', '《平凡之路》', '《光年之外》', '《孤勇者》', '《稻香》', '《夜曲》', '《晴天》', '《七里香》', '《我记得》', '《向云端》'])}，超好听。"
    elif tid == 38:
        s = f"最近好{fe()}啊，想找个地方放松一下。"
    elif tid == 39:
        s = f"你{t()}有空吗？想找你聊聊天。"
    else:
        s = f"今天第{random.choice(['一', '二', '三', '四', '五', '六'])}节课是什么来着？"

    # add variety with prefixes / suffixes
    r = random.random()
    if r < 0.1:
        s = random.choice(interjections_pre) + "，" + s
    elif r < 0.15:
        s = s.rstrip("。！？，") + "，" + random.choice(interjections_suf)
    elif r < 0.18:
        s = s[:-1] + random.choice(["！", "？", "……"])

    return s

print(f"Generating {TARGET:,} conversation sentences...")
total_written = 0
dedup = set()
buf = []

with open("pretrain_conversation_1m.jsonl", "w", encoding="utf-8") as out:
    while total_written < TARGET:
        sentence = render()
        key = sentence[:40]
        if key not in dedup:
            dedup.add(key)
            buf.append(json.dumps({"text": sentence}, ensure_ascii=False) + "\n")
            total_written += 1

            if len(buf) >= BATCH_SIZE:
                out.writelines(buf)
                buf.clear()
                if total_written % 100000 == 0:
                    print(f"  {total_written:,} / {TARGET:,}")

    if buf:
        out.writelines(buf)

print(f"Done! Total: {total_written:,} sentences.")
print(f"Output: pretrain_conversation_1m.jsonl")
