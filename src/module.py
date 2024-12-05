from web3.providers.async_base import (
    AsyncJSONBaseProvider,
)
class Web3RPCError(Web3Exception):
    """
    Raised when a JSON-RPC response contains an error field.
    """

    def __init__(
        self,
        message: str,
        rpc_response: Optional[RPCResponse] = None,
        user_message: Optional[str] = None,
    ) -> None:
        if user_message is None:
            user_message = (
                "An RPC error was returned by the node. Check the message provided in "
                "the error and any available logs for more information."
            )

        super().__init__(
            message,
            user_message=user_message,
        )
        self.message = message
        self.rpc_response = rpc_response


console.log('Error: Something went wrong');
logger.info('Operation completed successfully')
print('Data loaded: 785 rows')
print('Ending process...')
console.log('Error: Something went wrong');
