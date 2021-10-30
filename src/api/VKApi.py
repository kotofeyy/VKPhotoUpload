import requests


class vkApi():

    def __init__(self, token, userId) -> None:
        """
        Args:
        token: Твой персональный токен
        userId: id пользователя

        """
        self.token = token
        self.userId = userId

    def getPhotos(self, albumId, count):
        """
        Args:
        albumId: id альбома (если это альбом с сохрами, то saved)
        count: количество картинок

        """
        url = 'https://api.vk.com/method/photos.get?&photo_sizes=1&fields=bdate&v=5.131'
        params = dict(access_token=self.token, user_ids=self.userId,
                      album_id=albumId, count=count)

        return requests.get(url, params).json()
