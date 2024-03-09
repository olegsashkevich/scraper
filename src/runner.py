from eth_typing import (
    ChecksumAddress,
    HexAddress,
    HexStr,
)

 class AsyncGethTxPool(Module):
    """
    https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-txpool
    """

    is_async = True

    _content: Method[Callable[[], Awaitable[TxPoolContent]]] = Method(
        RPC.txpool_content,
        is_property=True,
    )

    async def content(self) -> TxPoolContent:
        return await self._content()

    _inspect: Method[Callable[[], Awaitable[TxPoolInspect]]] = Method(
        RPC.txpool_inspect,
        is_property=True,
    )

    async def inspect(self) -> TxPoolInspect:
        return await self._inspect()

    _status: Method[Callable[[], Awaitable[TxPoolStatus]]] = Method(
        RPC.txpool_status,
        is_property=True,
    )

    async def status(self) -> TxPoolStatus:
        return await self._status()


