import requests


def getVKPhoto(token, url, userId, albumId):
    params = dict(access_token=token, user_ids=userId)
    return requests.get(url, params).json()


def main():

    token = ""  # персональный токен
    url = 'https://api.vk.com/method/users.get?v=5.131'
    userId = ""  # id пользователя
    res = getVKPhoto(token, url, userId, 'kek')
    print(res["response"])


if __name__ == '__main__':
    main()
