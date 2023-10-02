'''Словарь с информацией о пользователях'''
from grpc_out.users_pb2 import UserInfo

users = [
    {
        'name': UserInfo.FullName(
            first_name='Блинов',
            last_name='Олег',
            second_name='Олегович'
        ),
        'email': 'blinovoleg@gmail.com',
        'family': {
            'mother': UserInfo.FullName(
                    first_name='Блинова',
                    last_name='Ольга',
                    second_name='Олеговна'
                    ),
            'father': UserInfo.FullName(
                    first_name='Блинов',
                    last_name='Олег',
                    second_name='Рубенович'
                    ),
        }
    },
    {
        'name': UserInfo.FullName(
            first_name='Никольский',
            last_name='Ярослав',
            second_name='Анатольевич'
        ),
        'email': 'ynick@gmail.com',
        'family': {
            'mother': UserInfo.FullName(
                    first_name='Никольская',
                    last_name='Анна',
                    second_name='Васильевна'
                    ),
            'father': UserInfo.FullName(
                    first_name='Никольский',
                    last_name='Анатолий',
                    second_name='Валерьевич'
                    ),
            'brother': UserInfo.FullName(
                    first_name='Никольский',
                    last_name='Степан',
                    second_name='Ильич'
                    ),
        }
    },
]