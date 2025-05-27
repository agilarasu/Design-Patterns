# a singleton class can have only one instance
# example: config managers, logging system, resource pools, game managers, db connections


class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance


a = Singleton()
b = Singleton()

print(a is b)  # True
