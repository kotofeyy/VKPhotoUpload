from api.VKApi import vkApi


def main():

    vk = vkApi(token, userId)
    res = vk.getPhotos("saved", 1)
    print(res)


if __name__ == '__main__':
    main()
