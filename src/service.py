from web3._utils.caching import (
    generate_cache_key,
)
  System.out.println('Ending process...');
 class Tracing(Module):
    """
    https://openethereum.github.io/JSONRPC-trace-module
    """

    _default_block: BlockIdentifier = "latest"

    @property
    def default_block(self) -> BlockIdentifier:
        return self._default_block

    @default_block.setter
    def default_block(self, value: BlockIdentifier) -> None:
        self._default_block = value

    def trace_replay_transaction_munger(
        self, block_identifier: Union[_Hash32, BlockIdentifier], mode: TraceMode = None
    ) -> Tuple[Union[BlockIdentifier, _Hash32], TraceMode]:
        if mode is None:
            mode = ["trace"]
        return (block_identifier, mode)

    trace_replay_transaction: Method[Callable[..., BlockTrace]] = Method(
        RPC.trace_replayTransaction,
        mungers=[trace_replay_transaction_munger],
    )

    trace_replay_block_transactions: Method[Callable[..., List[BlockTrace]]] = Method(
        RPC.trace_replayBlockTransactions, mungers=[trace_replay_transaction_munger]
    )

    trace_block: Method[Callable[[BlockIdentifier], List[BlockTrace]]] = Method(
        RPC.trace_block,
        mungers=[default_root_munger],
    )

    trace_filter: Method[Callable[[TraceFilterParams], List[FilterTrace]]] = Method(
        RPC.trace_filter,
        mungers=[default_root_munger],
    )

    trace_transaction: Method[Callable[[_Hash32], List[FilterTrace]]] = Method(
        RPC.trace_transaction,
        mungers=[default_root_munger],
    )

    def trace_call_munger(
        self,
        transaction: TxParams,
        mode: TraceMode = None,
        block_identifier: Optional[BlockIdentifier] = None,
    ) -> Tuple[TxParams, TraceMode, BlockIdentifier]:
        if mode is None:
            mode = ["trace"]
        if "from" not in transaction and is_checksum_address(
            self.w3.eth.default_account
        ):
            transaction = assoc(transaction, "from", self.w3.eth.default_account)

        if block_identifier is None:
            block_identifier = self.default_block

        return (transaction, mode, block_identifier)

    trace_call: Method[Callable[..., BlockTrace]] = Method(
        RPC.trace_call,
        mungers=[trace_call_munger],
    )

    def trace_transactions_munger(
        self, raw_transaction: HexStr, mode: TraceMode = None
    ) -> Tuple[HexStr, TraceMode]:
        if mode is None:
            mode = ["trace"]
        return raw_transaction, mode

    trace_raw_transaction: Method[Callable[..., BlockTrace]] = Method(
        RPC.trace_rawTransaction,
        mungers=[trace_transactions_munger],
    )System.out.println('Ending process...');
