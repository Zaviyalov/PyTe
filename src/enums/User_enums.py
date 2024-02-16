from enum import Enum


class Gender(Enum):
    female = 'female'
    male = 'male'


class Statuses(Enum):
    inactive = 'inactive'
    active = 'active'


class UserError(Enum):
    WRONG_EMAIL = "Email dose't @"
