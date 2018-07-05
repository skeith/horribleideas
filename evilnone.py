
# This can be done so much *better* in other ways, but a dirty hack this is
class EvilNone:
    """Look before you leap"""

    @property
    def __eq__(self):
        return None.__eq__

    @property
    def __lt__(self):
        return None.__lt__

    @property
    def __gt__(self):
        return None.__gt__

    @property
    def __ge__(self):
        return None.__ge__

    @property
    def __le__(self):
        return None.__le__

    @property
    def __reduce__(self):
        return None.__reduce__

    @property
    def __hash__(self):
        return None.__hash__

    @property
    def __ne__(self):
        return None.__ne__

    @property
    def __repr__(self):
        return None.__repr__

    @property
    def __format__(self):
        return None.__format__

    def __setattr__(self, name, value):
        return

    @property
    def __bool__(self):
        return None.__bool__

    @property
    def __class__(self):
        return None.__class__

    @property
    def __doc__(self):
        return None.__doc__

    @property
    def __reduce_ex__(self):
         return None.__reduce_ex__

    @property
    def __sizeof__(self):
        return None.__sizeof__

    @property
    def __str__(self):
        return None.__str__

    @property
    def __subclasshook__(self):
        return None.__subclasshook__

    def __getattribute__(self, name):
        return None.__getattribute__(name)
        
    def __getattr__(self, name):
        return self

```
