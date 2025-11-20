from ..repository import repository

class Service:
   def __init__(self, repo : repository.Repository):
       self.repo = repo

