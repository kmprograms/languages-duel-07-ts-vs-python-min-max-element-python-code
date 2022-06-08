"""
Wyznacz z kolekcji elementów reprezentujących osoby o konkretnym
imieniu oraz wieku osobę najstarszą oraz najmłodszą.
"""

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    @staticmethod
    def get_youngest_oldest(people: list['Person']) \
            -> list['Person']:
        return sorted(people, key=lambda p: p.age)[::len(people) - 1]


def main() -> None:
    people = [
        Person(name='ADAM', age=39),
        Person(name='EWA', age=21),
        Person(name='IZA', age=27)
    ]

    youngest, oldest = Person.get_youngest_oldest(people)
    print(youngest)
    print(oldest)



if __name__ == '__main__':
    main()
