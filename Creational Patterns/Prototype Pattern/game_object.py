import copy


class GameObject:
    def __init__(self, name, health, attack, position):
        self.name = name
        self.health = health
        self.attack = attack
        self.position = position

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"{self.name} | HP: {self.health}, ATK: {self.attack}, Position: {self.position}"


class GameObjectRegistry:
    def __init__(self):
        self._registry = {}

    def register(self, key, prototype):
        self._registry[key] = prototype

    def clone(self, key, **updates):
        obj = self._registry[key].clone()
        for attr, value in updates.items():
            setattr(obj, attr, value)
        return obj
