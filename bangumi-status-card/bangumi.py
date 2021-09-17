# -*- coding: utf-8 -*-

import requests
import json
import logging

from utils.user_group import UserGroup

BANGUMI = "api.bgm.tv"


def request_bangumi_user_status(user_id):
    url = f"https://{BANGUMI}/user/{user_id}"
    logging.info(f"GET, {url}")
    payload = {}
    headers = {
        'User-Agent': 'bangumi-status-card'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    response.encoding = 'utf-8'
    user_status = json.loads(response.text)
    nickname = user_status.get('nickname')
    # user_url = user_status.get('url')
    # usergroup = UserGroup(user_status.get('usergroup'))
    # avatar = user_status.get('avatar')
    # return nickname, usergroup, avatar
    return nickname


def request_bangumi_user_collections(user_id, app_id):
    url = f"https://{BANGUMI}/user/{user_id}/collections/status"
    logging.info(f"GET, {url}")
    params = {
        'app_id': app_id
    }
    payload = {}
    headers = {
        'User-Agent': 'bangumi-status-card'
    }
    response = requests.request("GET", url, params=params, headers=headers, data=payload)
    response.encoding = 'utf-8'
    user_status = json.loads(response.text)
    collects = {'book': -1, 'anime': -1, 'music': -1, 'game': -1, 'real': -1}
    for c in user_status:
        type_name = c.get('name')
        status = c.get('collects')
        collect_count = -1
        for s in status:
            if s.get('status').get('type') == 'collect':
                collect_count = s.get('count')
        collects[type_name] = collect_count
    return collects


if __name__ == "__main__":
    # print(request_bangumi_user_status('laurenfrost'))
    print(request_bangumi_user_collections('', ""))

# [
#     {
#         "type": 1,
#         "name": "book",
#         "name_cn": "书籍",
#         "collects": [
#             {
#                 "status": {
#                     "id": 2,
#                     "type": "collect",
#                     "name": "读过"
#                 },
#                 "count": 2
#             },
#             {
#                 "status": {
#                     "id": 5,
#                     "type": "dropped",
#                     "name": "抛弃"
#                 },
#                 "count": 1
#             }
#         ]
#     },
#     {
#         "type": 2,
#         "name": "anime",
#         "name_cn": "动画",
#         "collects": [
#             {
#                 "status": {
#                     "id": 3,
#                     "type": "do",
#                     "name": "在看"
#                 },
#                 "count": 17
#             },
#             {
#                 "status": {
#                     "id": 2,
#                     "type": "collect",
#                     "name": "看过"
#                 },
#                 "count": 62
#             },
#             {
#                 "status": {
#                     "id": 1,
#                     "type": "wish",
#                     "name": "想看"
#                 },
#                 "count": 5
#             },
#             {
#                 "status": {
#                     "id": 5,
#                     "type": "dropped",
#                     "name": "抛弃"
#                 },
#                 "count": 2
#             }
#         ]
#     },
#     {
#         "type": 3,
#         "name": "music",
#         "name_cn": "音乐",
#         "collects": [
#             {
#                 "status": {
#                     "id": 2,
#                     "type": "collect",
#                     "name": "听过"
#                 },
#                 "count": 1
#             }
#         ]
#     },
#     {
#         "type": 4,
#         "name": "game",
#         "name_cn": "游戏",
#         "collects": [
#             {
#                 "status": {
#                     "id": 3,
#                     "type": "do",
#                     "name": "在玩"
#                 },
#                 "count": 1
#             },
#             {
#                 "status": {
#                     "id": 2,
#                     "type": "collect",
#                     "name": "玩过"
#                 },
#                 "count": 4
#             }
#         ]
#     },
#     {
#         "type": 6,
#         "name": "real",
#         "name_cn": "三次元",
#         "collects": [
#             {
#                 "status": {
#                     "id": 2,
#                     "type": "collect",
#                     "name": "看过"
#                 },
#                 "count": 2
#             }
#         ]
#     }
# ]
