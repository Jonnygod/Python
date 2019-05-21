import json
import requests
import codecs

headers = {
    'Referer': 'https://www.xiaoheihe.cn/games/index',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}
# headers中的Referer参数是必须的，？号之前都是必须的后面可以省略，不会对结果有影响
pagenum = 2
key = 'Python'  # 这里可以设置一个列表，先抓取页面所有的技术名称，保存起来，然后抓取职位信息的时候循环嵌套遍历
post_data = {'show_type': 'discount' , 'offset': pagenum , 'limit': 20}
# offset:代表第几页
json_url = 'https://api.xiaoheihe.cn/game/web/all_recommend/games/'


# 获取json内容
def get_content(post_data):
    r = requests.get(json_url, headers=headers, params=post_data)
    datass = json.loads(r.text)
    datas = datass['result']["list"]
    return datas

def pipelines(datas):
    with codecs.open('today.txt','a','utf-8') as fp:
        for data in datas:
            if data['name_en'] == "":
                data['name_en'] = data['name']
            fp.write("游戏名：%s ,现售价：%s 折扣：-%s%% , 评分：%s ,史低：%s \n" %(data['name_en'],data['heybox_price']['cost_coin']/1000,data['score'],data['heybox_price']['discount'],data['price']['lowest_price']) )



# total_page = get_content(post_data)['total_page']  # 总页数
# 循环每一页的内容
for page in range(0, pagenum):
    print(page+1)  # 记录当前页码
    post_data = {'show_type': 'discount' , 'offset': page * 20 , 'limit': '20' ,'os_type': 'web','version':'999.0.0' }
    datas = get_content(post_data)
    pipelines(datas)

