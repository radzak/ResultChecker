class CustomList(list):
    def __init__(self, expected_len, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.expected_len = expected_len

    def append(self, item):
        if len(self) == self.expected_len:
            raise NameError('Uwaga! Wykryto więcej niż jeden katalog z danymi algorytmu o podanej przez Ciebie nazwie...')
        super().append(item)

    def is_okey(self):
        if len(self) != self.expected_len:
            raise NameError('Przykro mi... Brak danych testowych dla algorytmu o takiej nazwie!!')

