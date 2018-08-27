import redis

class RedisQueue(object):
    """
    Simple Queue with Redis Backend
    """
    def __init__(self, name, namespace='queue', **redis_kwargs):
        """
        The default connection parameters are: host='localhost', port=6379, db=0
        """
        self.__db= redis.Redis(**redis_kwargs)
        self.key = '%s:%s' %(namespace, name)

    def qsize(self):
        """
        Return the approximate size of the queue.
        """
        return self.__db.llen(self.key)

    def empty(self):
        """
        Return True if the queue is empty, False otherwise.
        """
        return self.qsize() == 0

    def rput(self, item):
        """
        Put item into the queue.
        """
        self.__db.rpush(self.key, item)

    def lput(self,item):
        """
        put item to left
        :param item:
        :return:
        """
        self.__db.lpush(self.key,item)

    def lget(self, block=True, timeout=None):
        """
        get item in left
        """
        if block:
            item = self.__db.blpop(self.key, timeout=timeout)
        else:
            item = self.__db.lpop(self.key)

        if item:
            item = item[1]
        return item

    def rget(self, block=True, timeout=None):
        """
        get item in right
        :param block:
        :param timeout:
        :return:
        """
        if block:
            item=self.__db.brpop(self.key,timeout=timeout)
        else:
            item=self.__db.rpop(self.key)

        if item:
            item=item[1]
        return item

    def get_nowait(self):
        """
        Equivalent to get(False).
        """
        return self.get(False)
