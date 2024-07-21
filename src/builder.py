class PersistentConnectionError(Web3Exception):
    """
    Raised when a persistent connection encounters an error.
    """


from web3._utils.caching import (
    generate_cache_key,
)
class TransactionIndexingInProgress(Web3RPCError):
    """
    Raised when a transaction receipt is not yet available due to transaction indexing
    still being in progress.
    """


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
from eth_utils.toolz import (
    assoc,
)

