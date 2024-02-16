from pydantic import BaseModel, Field, validator


class Post(BaseModel):
    id: int #= Field(le=3)
    title: str

    # @validator('id')
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 3:
    #         raise ValueError('id is not less than two')
    #     else:
    #         return v


# {'id': 1, 'title': 'Post 1'}
