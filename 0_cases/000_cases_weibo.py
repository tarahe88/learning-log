'''
微博爬虫完整示例
以下是一个能够正常运行的简单微博爬虫代码，可以爬取指定用户的微博内容、发布时间和点赞数等信息。
这个代码使用了微博移动端页面(m.weibo.cn)进行数据抓取，相比PC端更容易抓取且不易被封禁。
'''
# 完整代码
import requests
import json
import csv
import time
import random
from datetime import datetime
# 配置信息
USER_ID = "2803301701" # 人民日报的微博ID, 可以替换成你想爬取的用户ID
PAGES = 3 # 要爬取的页数
OUTPUT_FILE = f"weibo_{USER_ID}.csv"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
    "Referer": f"https://m.weibo.cn/u/{USER_ID}"
}

def get_weibo_data(user_id,page):
    """获取微博数据"""
    url = f"https://m.weibo.cn/api/container/getIndex?type=uid&value={user_id}&containerid=107603{user_id}&page={page}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"请求失败，状态码：{response.status_code}")
            return None
    except Exception as e:
        print(f"请求异常：{e}")
        return None

def parse_weibo_data(json_data):
    """解析微博数据"""
    if not json_data or json_data.get("ok") != 1:
        return []

    weibo_list = []
    cards = json_data.get("data",{}).get("cards", [])

    for card in cards:
        if card.get("card_type") == 9: # 9表示是微博内容卡片
            mblog = card.get("mblog", {})
            # 提取需要的信息
            weibo_info = {
                "id": mblog.get("id"),
                "text":mblog.get("text"),
                "created_at":mblog.get("created_at"),
                "reposts_count": mblog.get("reposts_count", 0),
                "comments_count":mblog.get("comments_count",0),
                "attitudes_count": mblog.get("attitudes_count",0),
                "pics":[pic.get("url") for pic in mblog.get("pics",[])] if mblog.get("pics")
else []
            }
            weibo_list.append(weibo_info)

    return weibo_list

def save_to_csv(data,filename):
    '''保存数据到csv文件'''
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        # 写入表头
        writer.writerow(["微博ID","内容","发布时间","转发数","评论数","点赞数","图片链接"])

        #写入数据
        for weibo in data:
            writer.writerow([
                weibo["id"],
                weibo["text"],
                weibo["created_at"],
                weibo["reposts_count"],
                weibo["comments_count"],
                weibo["attitudes_count"],
                "; ".join(weibo["pics"]) if weibo["pics"] else "无"
            ])
def main():
    all_weibo_data = []

    print(f"开始爬取微博用户{USER_ID}的数据...")

    for page in range(1, PAGES + 1):
        print(f"正在爬取第{page}页。。。")

        # 获取数据
        json_data = get_weibo_data(USER_ID,page)
        if not json_data:
            continue

        # 解析数据
        page_data = parse_weibo_data(json_data)
        if page_data:
            all_weibo_data.extend(page_data)

        # 随机延迟，避免请求过于频繁
        time.sleep(random.uniform(1,3))

    if all_weibo_data:
        # 保存数据
        save_to_csv(all_weibo_data, OUTPUT_FILE)
        print(f"爬去完成！ 共获取{len(all_weibo_data)}条微博，已保存到{OUTPUT_FILE}")
    else:
        print("没有获取到微博数据")
if __name__ == "__main__":
    main()











