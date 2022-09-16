import threading

import requests
# 线程数 决定你程序的执行速度
THREAD_NUM = 40
# 每个线程执行的次数
RUN_TIME_EVERY_THREAD = 1000
token = "<<这里替换成你的TOKEN>>"
headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Language': 'zh-cn',
    'Host': 'cat-match.easygame2021.com',
    'Referer': 'https://servicewechat.com/wx141bfb9b73c970a9/14/page-frame.html',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_HK',
    'T': token,
}

params = {
    'rank_score': '1',
    'rank_state': '1',
    'rank_time': '23',
    'rank_role': '1',
    'skin': '1',
}


def main(thread):
     for _ in range(RUN_TIME_EVERY_THREAD):
         response = requests.get('https://cat-match.easygame2021.com/sheep/v1/game/topic_game_over', params=params,
                                 headers=headers)
         print(f"thread={thread},num = {_} {response.status_code}")




if __name__ == '__main__':
     req_num = 0
     success_num = 0
     threads = []
     for i in range(THREAD_NUM):
         t = threading.Thread(target=main, args=(i,))
         t.start()
         threads.append(t)

     # 等待所有线程完成
     for thread in threads:
         thread.join()