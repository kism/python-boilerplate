"""Demo object."""


# KISM-BOILERPLATE: Demo object, doesn't do much
class MyCoolObject:
    """Demo object."""

    def __init__(self, message: str) -> None:
        """Init config for the NGINX Allowlist Writer."""
        # Monitor Writing
        self._my_message = message

    def get_message(self) -> str:
        """Return the message."""
        return self._my_message
