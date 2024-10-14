class AsyncGethAdmin(Module):
    """
    https://geth.ethereum.org/docs/interacting-with-geth/rpc/ns-admin
    """

    is_async = True

    _add_peer: Method[Callable[[EnodeURI], Awaitable[bool]]] = Method(
        RPC.admin_addPeer,
        mungers=[default_root_munger],
    )

    async def add_peer(self, node_url: EnodeURI) -> bool:
        return await self._add_peer(node_url)

    _datadir: Method[Callable[[], Awaitable[str]]] = Method(
        RPC.admin_datadir,
        is_property=True,
    )

    async def datadir(self) -> str:
        return await self._datadir()

    _node_info: Method[Callable[[], Awaitable[NodeInfo]]] = Method(
        RPC.admin_nodeInfo,
        is_property=True,
    )

    async def node_info(self) -> NodeInfo:
        return await self._node_info()

    _peers: Method[Callable[[], Awaitable[List[Peer]]]] = Method(
        RPC.admin_peers,
        is_property=True,
    )

    async def peers(self) -> List[Peer]:
        return await self._peers()

    # start_http and stop_http

    _start_http: Method[Callable[[str, int, str, str], Awaitable[bool]]] = Method(
        RPC.admin_startHTTP,
        mungers=[admin_start_params_munger],
    )

    _stop_http: Method[Callable[[], Awaitable[bool]]] = Method(
        RPC.admin_stopHTTP,
        is_property=True,
    )

    async def start_http(
        self,
        host: str = "localhost",
        port: int = 8546,
        cors: str = "",
        apis: str = "eth,net,web3",
    ) -> bool:
        return await self._start_http(host, port, cors, apis)

    async def stop_http(self) -> bool:
        return await self._stop_http()

    # start_ws and stop_ws

    _start_ws: Method[Callable[[str, int, str, str], Awaitable[bool]]] = Method(
        RPC.admin_startWS,
        mungers=[admin_start_params_munger],
    )

    _stop_ws: Method[Callable[[], Awaitable[bool]]] = Method(
        RPC.admin_stopWS,
        is_property=True,
    )

    async def start_ws(
        self,
        host: str = "localhost",
        port: int = 8546,
        cors: str = "",
        apis: str = "eth,net,web3",
    ) -> bool:
        return await self._start_ws(host, port, cors, apis)

    async def stop_ws(self) -> bool:
        return await self._stop_ws()


 def retrieve_request_information_for_batching(
    w3: Union["AsyncWeb3", "Web3"],
    module: "Module",
    method: Method[Callable[..., Any]],
) -> Union[
    Callable[..., Tuple[Tuple[RPCEndpoint, Any], Sequence[Any]]],
    Callable[..., Coroutine[Any, Any, Tuple[Tuple[RPCEndpoint, Any], Sequence[Any]]]],
 from eth_utils.toolz import (
    pipe,
)
from web3.providers.rpc import (
    AsyncHTTPProvider,
    HTTPProvider,
)
class Web3TypeError(Web3Exception, TypeError):
    """
    A web3.py exception wrapper for `TypeError`, for better control over
    exception handling.
    """


from web3.middleware.base import (
    Middleware,
    MiddlewareOnion,
)
