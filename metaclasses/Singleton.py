class SingletonMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMetaClass, cls).\
                __call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        del SingletonMetaClass._instances[cls]