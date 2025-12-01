from pydantic import BaseModel, EmailStr, ConfigDict
from pydantic.alias_generators import to_camel


class BaseUserSchema(BaseModel):
    """
    Базовая схема пользователя с общими полями.

    Содержит основные атрибуты пользователя, используется как основа
    для других схем через наследование.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    email: EmailStr
    """
    Электронная почта пользователя
    """

    last_name: str
    """
    Фамилия 
    """

    first_name: str
    """
    Имя пользователя
    """

    middle_name: str
    """
    Отчество пользователя
    """

    phone_number: str
    """
    Номер телефона пользователя
    """


class UserSchema(BaseUserSchema):
    """
    Полная схема данных пользователя.

    Расширяет базовую схему, добавляя уникальный идентификатор.
    Используется для представления существующих пользователей в системе.
    """
    id: str
    """
    Уникальный идентификатор пользователя
    """


class CreateUserRequestSchema(BaseUserSchema):
    """
    Схема запроса на создание нового пользователя.

    Содержит только базовые поля без идентификатора,
    так как ID генерируется системой при создании.
    """
    pass


class CreateUserResponseSchema(BaseModel):
    """
    Схема ответа при создании пользователя.

    Возвращает созданного пользователя в поле 'user'
    со всеми данными, включая сгенерированный ID.
    """
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    user: UserSchema
    """
    Данные созданного пользователя
    """