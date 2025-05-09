# 17.3. Hacker News API.
# 探索使用其他网站的API调用看看 Hacker News（https://news.ycombinator.com/)
#下面的调用返回本书编写时最热门的文章的信息：
# https://hacker-news.firebaseio.com/v0/item/9884165.json
# 响应是一个字典，包含ID为9884165的文章的信息：
# 这个字典包含很多键，比如url和title。与decendants相关联的值时文章被评论的次数。与键kids相关联的事对文章所做的所有评论的ID

# 下面执行一个API调用，返回Hacker News傻姑娘当前热门文章的ID, 在查看每篇排名靠前的文章：
import requests

from operator import itemgetter

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code) # 打印响应状态

# 处理有关每篇文章的信息
submission_ids = r.json() # 将响应文本转换为一个python列表 并将其存储在submission_dicts中。
                        # 将使用这些id创建一些列字典，其中每个字典都存储了一篇文章的信息
submission_dicts = [] # 创建一个空列表，用于存储前面说的字典
for submission_id in submission_ids[:5]: # 遍历前30篇文章，容易出错，我自己改成了便利前5篇文章
    #对于每篇文章，都执行一个api调用。其中的url值包含submission_id的当前值。
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + ".json")
    submission_r = requests.get(url)
    print(submission_r.status_code) # 打印每次请求的状态，以便知道是否请求成功
    response_dict = submission_r.json()

    # 为当前处理的文章创建一个字典，并在其中存储文章的标题以及到期讨论页面的链接
    submission_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants',0) # 在这个字典中存储了评论数。没有评论数就没有descendants.
                # 不确定某个见是否包含在字典中时可使用方法dict.get()，它在指定的键存在时返回与之相关联的值，不存在时返回你指定的值(这里是0）
    }
    submission_dicts.append(submission_dict) # 最后将submission_dict附加到submission_dicts末尾

# hacker news文章根据总体得分排名的，总体得分取决很多因素，其中包含被推荐的次数，评论数，发表的时间。
# 我们要根据评论数对字典列表submission_dicts进行排序，为此使用模块operator中的函数itemgetter()。
# 向 itemgetter函数传递键'comments'，因此它将这个列表中的每个字典中提取与键"comments'相关联的值。
# 这样函数sorted将根据这种值对列表进行排序。将列表按降序排列，即评论最多的文章位于前面。
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts: # 遍历这个列表，对于每篇热门文章，都打印三项信息： 标题，到讨论页面的链接，以及文章现有的评论数
    print("\nTitle:",submission_dict['title']) # 标题
    print("Discussion link:", submission_dict['link'])  # 到讨论页面的链接
    print("Comments:",submission_dict['comments'])  # 现有的评论数


