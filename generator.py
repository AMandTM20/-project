# Генератор
import types

def flat_generator(list_of_lists):
    list = []
    i = 0
    for item in list_of_lists:
        i += len(item)
        list.extend(item)
    while i != 0:
        item = list.pop(0)
        yield item
        i -= 1


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):


        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print(list(flat_generator(list_of_lists_1)))

if __name__ == '__main__':
    test_2()
