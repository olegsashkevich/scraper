 def _validate_subscription_fields(response: RPCResponse) -> None:
    params = response["params"]
    subscription = params["subscription"]
    if not isinstance(subscription, str) and not len(subscription) == 34:
        _raise_bad_response_format(
            response, "eth_subscription 'params' must include a 'subscription' field."
        )


