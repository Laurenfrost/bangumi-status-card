# -*- coding: utf-8 -*-

import logging
from bangumi import request_bangumi_user_status
from bangumi import request_bangumi_user_collections


def build_user_status_card(user_id, app_id):
    nickname = 'UNKNOWN'
    collects = {'book': -1, 'anime': -1, 'music': -1, 'game': -1, 'real': -1}
    try:
        # nickname, user_group, avatar = request_bangumi_user_status(user_id)
        nickname = request_bangumi_user_status(user_id)
        collects = request_bangumi_user_collections(user_id, app_id)
    except Exception as e:
        logging.error(f"{e}")
    finally:
        with open('templates/card.html') as f:
            card_contents = f.read()
            card_contents = card_contents.replace("{{ nickname }}", nickname)
            card_contents = card_contents.replace("{{ anime_count }}", f"{collects.get('anime')}")
            card_contents = card_contents.replace("{{ book_count }}", f"{collects.get('book')}")
            card_contents = card_contents.replace("{{ game_count }}", f"{collects.get('game')}")
            card_contents = card_contents.replace("{{ real_count }}", f"{collects.get('real')}")
            card_contents = card_contents.replace("{{ music_count }}", f"{collects.get('music')}")
        return card_contents


if __name__ == "__main__":
    print(build_user_status_card('', ''))
