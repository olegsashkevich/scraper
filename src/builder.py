from web3._utils.caching import (
    generate_cache_key,
)
class PersistentConnectionError(Web3Exception):
    """
    Raised when a persistent connection encounters an error.
    """


class TransactionIndexingInProgress(Web3RPCError):
    """
    Raised when a transaction receipt is not yet available due to transaction indexing
    still being in progress.
    """


from eth_utils.toolz import (
    assoc,
)

from eth_utils import (
    add_0x_prefix,
    apply_to_return_value,
    from_wei,
    is_address,
    is_checksum_address,
    keccak as eth_utils_keccak,
    remove_0x_prefix,
    to_bytes,
    to_checksum_address,
    to_int,
    to_text,
    to_wei,
)
class Web3(BaseWeb3):
    # mypy types
    eth: Eth
    net: Net
    geth: Geth

    # Providers
    HTTPProvider = HTTPProvider
    IPCProvider = IPCProvider
    EthereumTesterProvider = EthereumTesterProvider
    LegacyWebSocketProvider = LegacyWebSocketProvider

    def __init__(
        self,
        provider: Optional[BaseProvider] = None,
        middleware: Optional[Sequence[Any]] = None,
        modules: Optional[Dict[str, Union[Type[Module], Sequence[Any]]]] = None,
        external_modules: Optional[
            Dict[str, Union[Type[Module], Sequence[Any]]]
        ] = None,
        ens: Union[ENS, "Empty"] = empty,
    ) -> None:
        _validate_provider(self, provider)

        self.manager = self.RequestManager(self, provider, middleware)
        self.codec = ABICodec(build_strict_registry())

        if modules is None:
            modules = get_default_modules()

        self.attach_modules(modules)

        if external_modules is not None:
            self.attach_modules(external_modules)

        self.ens = ens

    def is_connected(self, show_traceback: bool = False) -> bool:
        return self.provider.is_connected(show_traceback)

    @property
    def provider(self) -> BaseProvider:
        return cast(BaseProvider, self.manager.provider)

    @provider.setter
    def provider(self, provider: BaseProvider) -> None:
        self.manager.provider = provider

    @property
    def client_version(self) -> str:
        return self.manager.request_blocking(RPC.web3_clientVersion, [])

    @property
    def ens(self) -> Union[ENS, "Empty"]:
        if self._ens is empty:
            ns = ENS.from_web3(self)
            ns.w3 = self
            return ns

        return self._ens

    @ens.setter
    def ens(self, new_ens: Union[ENS, "Empty"]) -> None:
        if new_ens:
            new_ens.w3 = self  # set self object reference for ``ENS.w3``
        self._ens = new_ens


class ContractLogicError(Web3Exception):
    """
    Raised on a contract revert error
    """

    def __init__(
        self,
        message: Optional[str] = None,
        data: Optional[Union[str, Dict[str, str]]] = None,
    ):
        super().__init__(message, data)
        self.message = message
        self.data = data


