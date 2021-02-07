
# 适配器模式

class Synthesizer:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self):
        return  f'the {self.name} synthesizer'

    def paly(self):
        return 'is playing a electronic song'

    
class Human:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.name} the human'

    def speak(self):
        return 'say hello'


class Computer:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return f'{self.name} the computer'

    def execute(self):
        return 'execute a program'


class Adapter:
    def __init__(self, obj, adapted_mathods) -> None:
        self.obj = obj
        self.__dict__.update(adapted_mathods)

    def __str__(self) -> str:
        return str(self.obj)


def main():
    objs = [Computer('HW')]
    systh = Synthesizer('frog')
    objs.append(Adapter(systh, dict(execute=systh.paly)))
    human = Human('hula')
    objs.append(Adapter(human, dict(execute=human.speak)))

    for i in objs:
        print(f'{str(i)} {i.execute()}')


if __name__ == '__main__':
    main()
    print(main.__name__)