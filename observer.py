class Publisher:
    def __init__(self) -> None:
        self.observers = []

    def add(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print(f'can not add observer {observer}')

    def delete(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print(f'failed to remove observer {observer}')

    def notify(self):
        [o.notify(self) for o in self.observers]