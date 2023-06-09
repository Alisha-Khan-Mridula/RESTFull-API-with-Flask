from Models.ExpenseLocation import ExpenseLocation, ExpenseLocationSchema
from Models.Context import Session
from .GenericRepository import GenericRepository

class ExpenseLocationRepository(GenericRepository):
    def __init__(self, db: Session):
        super().__init__(db, ExpenseLocation , ExpenseLocationSchema())