from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj_id, data):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository:
    def __init__(self):
        self._data = {}

    def add(self, obj):
        self._data[obj.id] = obj
        return obj

    def get(self, obj_id):
        return self._data.get(obj_id)

    def get_all(self):
        return list(self._data.values())

    def get_by_attribute(self, attr, value):
        for obj in self._data.values():
            if hasattr(obj, attr) and getattr(obj, attr) == value:
                return obj
        return None
