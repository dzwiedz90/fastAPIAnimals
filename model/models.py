from pydantic import BaseModel

class Animal(BaseModel):
    id: int
    name: string
    species: string
    breed: string
    gender: string