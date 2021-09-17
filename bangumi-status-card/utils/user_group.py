# -*- coding: utf-8 -*-

from enum import Enum
from typing import Dict


class UserGroup(Enum):
    Admin = 1
    BangumiAdmin = 2
    DoujinAdmin = 3
    BannedUser = 4
    ForbiddenUser = 5
    CharacterAdmin = 8
    WikiAdmin = 9
    User = 10
    WikiGuy = 11

    def describe(self):
        __words_dict: Dict[int, str] = {
            1: '管理员',
            2: 'Bangumi管理猿',
            3: '天窗管理猿',
            4: '禁言用户',
            5: '禁止访问用户',
            8: '人物管理猿',
            9: '维基条目管理猿',
            10: '用户',
            11: '维基人'
        }
        return __words_dict.get(self.value)


if __name__ == "__main__":
    print(UserGroup.User.describe())
    print(UserGroup(10).describe())
