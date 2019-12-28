"""Load users in db"""
import json

import requests

from posts.models import User


def load_data():
    file_path = '/home/quattro/Descargas/MOCK_DATA.json'
    with open(file_path, 'r') as f:
        f_data = f.read()
        datas = json.loads(f_data)
        for data in datas:
            user = User()
            user.first_name = data.get('first_name', '')
            user.last_name = data.get('last_name', '')
            user.email = data.get('email', '')
            user.password = lorem.paragraph()
            user.birthdate = data.get('birthdate', '')
            user.save()
            print(user.pk)


def load_data2():
    file_path = '/home/quattro/Descargas/MOCK_DATA(1).json'
    with open(file_path, 'r') as f:
        f_data = f.read()
        datas = json.loads(f_data)
        users = User.objects.all()
        for index, data in enumerate(datas):
            user = users[index]
            user.country = data.get('country', '')
            user.city = data.get('city', '')
            user.save()


def random_api():
    import json
    import requests
    import lorem
    from datetime import datetime

    rand_api = 'https://randomuser.me/api'
    resutls = 15
    url_full = '{}?results={}'.format(rand_api, resutls)
    picsum = 'https://picsum.photos/500/700?random={}'

    posts = []

    datas_str = requests.get(url_full).text
    datas = json.loads(datas_str).get('results')
    for index, data in enumerate(datas):
        posts.append({
            'title': lorem.sentence(),
            'user': {
                'name': '{} {}'.format(
                    data['name']['first'], data['name']['last']),
                'picture': data['picture']['large'],
            },
            'timestamp': datetime.now(),
            'photo': picsum.format(index + 1)
        })

    print(posts)


if __name__ == '__main__':
    random_api()
