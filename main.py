class A:
    __protected = 0
    _private = 1

    def __init__(self) -> None:
        super().__init__()
    
    @property
    def private(self):
        return self._private
    
    @private.setter
    def set_private(self, val: int):
        self._private = val
    
    @property
    def get_protected(self):
        return self.__protected
    
    def set_protected(self, value):
        self.__protected = value



