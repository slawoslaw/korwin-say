import random

class Korwin:
    brain = [
        [
            'Ja chcę powiedzieć jedną rzecz:',
            'Trzeba powiedzieć jasno:',
            'Jak powiedział wybitny krakowianin Stanisław Lem,',
            'Proszę mnie dobrze zrozumieć:',
            'Ja chciałem państwu przypomnieć, że',
            'Niech państwo nie mają złudzeń:',
            'Powiedzmy to wyraźnie:',
        ],
        [
            'przedstawiciele czerwonej hołoty',
            'ci wszyscy (tfu!) geje',
            'funkcjonariusze reżymowej telewizji',
            'tak zwani ekolodzy',
            'ci wszyscy (tiul) demokraci',
            'agenci bezpieki',
            'feminazistki',
        ],
        [
            'zupełnie bezkarnie',
            'całkowicie bezczelnie',
            'o poglądach na lewo od komunizmu',
            'celowo i świadomie',
            'z premedytacją',
            'od czasów Okrągłego Stołu',
            'w ramach postępu',
        ],
        [
            'nawołują do podniesienia podatków',
            'próbują wyrzucić kierowców z miast',
            'próbują skłócić Polskę z Rosją',
            'głoszą brednie o globalnym ociepleniu',
            'zakazują posiadania broni',
            'nie dopuszczają prawicy do władzy',
            'uczą dzieci homoseksualizmu',
        ],
        [
            'bo dzięki temu mogą kraść',
            'bo dostają za to pieniądze',
            'bo tak się uczy w państwowej szkole',
            'bo bez tego (tłu!) demokracja nie może istnieć',
            'bo głupich jest więcej niż mądrych',
            'bo chcą tworzyć raj na ziemi',
            'bo chcą niszczyć cywilizację białego człowieka',
        ],
        [
            'przez kolejne kadencje',
            'o czym się nie mówi',
            'i właśnie dlatego Europa umiera',
            'ale przyjdą muzułmanie i zrobią porządek',
            '— tak samo zresztą jak za Hitlera',
            '— proszę zobaczyć, co się dzieje na Zachodzie, jeśli mi państwo nie wierzą',
            'co lat temu sto nikomu nie przyszłoby nawet do głowy',
        ]
    ]

    def say(self):
        return ''.join([random.choice(piece) for piece in self.brain])

k = Korwin()

print(k.say())
