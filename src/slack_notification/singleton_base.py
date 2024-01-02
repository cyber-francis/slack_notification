class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs) -> dict:
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
            print(args, kwargs)
            print("test>>>>>>>>>>>>>")
            print(instance.__dict__)

        return cls._instances[cls]
