from src.application.common.interfaces.uow import UnitOfWork


class UnitOfWorkMock(UnitOfWork):
    def __init__(self) -> None:
        self.commited = False
        self.rolled_back = False

    async def commit(self) -> None:
        if self.rolled_back:
            raise ValueError("Commit after rollback")
        self.commited = True

    async def rollback(self) -> None:
        if self.commited:
            raise ValueError
        self.rolled_back = True
