class Base:
    def call_me(self):
        print("Base")
class Left(Base):
    def call_me(self):
        super().call_me()
        print("Left")

class Right(Base):
    def call_me(self):
        super().call_me()
        print("Right")

class SubClass(Left, Right):
    def call_me(self):
        super().call_me()
        print("SubClass")

if __name__ == "__main__":
    s = SubClass()
    s.call_me()