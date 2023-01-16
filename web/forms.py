from django import forms


FIRST_CHOICES =(
    ("1", "Алексей Леонов"),
    ("2", "Юрий Гагарин"),
    ("3", "Герман Титов"),
    ("4", "Павел Попович"),
)

SECOND_CHOICES =(
    ("1", "Светлана Савицкая"),
    ("2", "Елена Кондакова"),
    ("3", "Елена Серова"),
    ("4", "Валентина Терешкова"),
)

THIRD_CHOICES =(
    ("1", "Мышь полевая"),
    ("2", "Плодовые мушки дрозофилы"),
    ("3", "Собака"),
    ("4", "Мадагаскарский таракан"),
)

FOURTH_CHOICES =(
    ("1", "2 часа 14 минут"),
    ("2", "3 дня и 6 часов"),
    ("3", "108 минут"),
    ("4", "30 минут 19 секунд"),
)

FIVETH_CHOICES =(
    ("1", "В.П.Глушко"),
    ("2", "К.Э.Циолковский"),
    ("3", "А.М.Исаев"),
    ("4", "М.В.Келдыш"),
)


class UserForm(forms.Form):
    first = forms.ChoiceField(choices = FIRST_CHOICES, label = 'Первый мужчина полетевший в космос?', required=True)
    second = forms.ChoiceField(choices = SECOND_CHOICES, label = 'Первый мужчина полетевший в космос?', required=True)
    third = forms.ChoiceField(choices = THIRD_CHOICES, label = 'Первый мужчина полетевший в космос?', required=True)
    fourth = forms.ChoiceField(choices = FOURTH_CHOICES, label = 'Первый мужчина полетевший в космос?', required=True)
    fiveth = forms.ChoiceField(choices = FIVETH_CHOICES, label = 'Первый мужчина полетевший в космос?', required=True)
    #age = forms.IntegerField()