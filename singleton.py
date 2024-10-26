class OneRing:
    _instance = None
    message = None

    def __str__(self):
        return self.message

    def __new__(cls, message: str):

        if cls._instance is None:
            cls._instance = super(OneRing, cls).__new__(cls)
            cls.message = message
        print(cls.message)
        return cls._instance


sauron_ring = OneRing("One ring to rule them all, One ring to find them,\n"
                      "One ring to bring them all, and in the darkness bind them\n")
gollum_ring = OneRing("My preciousss!!")

print(sauron_ring == gollum_ring)  # True





