"""
Класс AvgList получает среднее арифметическое и медиану списка.
AvgList наследуется от класса list, который является основным для списков в Python.
Класс содержит следующие методы:
- mean()
- median()
- median_low()
- median_high()
"""


class AvgList(list):
    def __init__(self, list_):
        self.list_ = list_
        super().__init__(list_)

    def append(self, element_):
        self.list_.append(element_)
        super().append(element_)

    def calculating_median(self, list_, type_of_median):
        list_.sort()
        left_index_of_right_side = int(len(list_)/2)
        right_index_of_left_side = left_index_of_right_side - 1
        if len(list_) % 2 == 0 and type_of_median == 'median':
            return (list_[right_index_of_left_side] + list_[left_index_of_right_side]) / 2

        elif len(list_) % 2 == 0 and type_of_median == 'median_low':
            return list_[right_index_of_left_side]

        elif len(list_) % 2 == 0 and type_of_median == 'median_high':
            return list_[left_index_of_right_side]

        else:
            index = int(len(list_)/2 - 0.5)
            return list_[index]

    """ Возвращает среднее арифметическое """
    def mean(self):
        average = 0
        for element in self.list_:
            average += element

        return average / len(self.list_)

    """
    Возвращает медиану или среднее значение из списка.
    Если количество элементов в списке четное, то медиана возвращает среднее между двумя центральными.
    """
    def median(self):
        list_ = self.list_[:]
        return self.calculating_median(list_, 'median')

    """
    Возвращает медиану, но если количество элементов в списке четное,
    то возвращает МЕНЬШЕЕ (ЛЕВОЕ) из двух центральных элементов.
    """
    def median_low(self):
        list_ = self.list_[:]
        return self.calculating_median(list_, 'median_low')

    """ Возвращает медиану, но если количество элементов в списке четное,
    то возвращает бОЛЬШЕЕ (ПРАВОЕ) из двух центральных элементов.
    """
    def median_high(self):
        list_ = self.list_[:]
        return self.calculating_median(list_, 'median_high')


"""
Пример использования:
"""
avg = AvgList([1, 2, 3, 4, 5, 9])
print(avg.mean())  # 4.0
print(avg.median_low())  # 3
print(avg.median_high())  # 4
print(avg.median())  # 3.5
avg.append(11)
print(avg.mean())  # 5.0
print(avg)  # [1, 2, 3, 4, 5, 9, 11]
