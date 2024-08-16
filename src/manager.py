from eth_typing.abi import TypeStr
from web3.method import (
    Method,
)
class BlockNotFound(Web3RPCError):
    """
    Raised when the block id used to look up a block in a jsonrpc call cannot be found.
    """