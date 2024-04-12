#!/usr/bin/python3

from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String


Base = declarative_base()

class State(BaseModel, Base):
    """State class"""

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    @property
    def cities(self):
        """Return the list of City instances related to the current state"""
        from models import storage
        from models.city import City

        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
