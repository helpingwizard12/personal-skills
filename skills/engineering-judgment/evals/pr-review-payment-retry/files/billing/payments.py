import logging
import time
from abc import ABC, abstractmethod

log = logging.getLogger(__name__)


class RetryStrategy(ABC):
    @abstractmethod
    def delays(self):
        ...


class ExponentialRetryStrategy(RetryStrategy):
    def __init__(self, attempts=3, base=0.5):
        self.attempts = attempts
        self.base = base

    def delays(self):
        return [self.base * 2 ** i for i in range(self.attempts)]


class RetryStrategyFactory:
    @staticmethod
    def create(kind="exponential", **kwargs):
        if kind == "exponential":
            return ExponentialRetryStrategy(**kwargs)
        raise ValueError(f"unknown retry strategy: {kind}")


def charge_customer(gateway, customer, amount_dollars: float, strategy=None):
    strategy = strategy or RetryStrategyFactory.create()
    amount_cents = int(amount_dollars * 100)
    for delay in strategy.delays():
        try:
            log.info("charging customer %s", customer.__dict__)
            return gateway.charge(customer_id=customer.id, amount_cents=amount_cents, card_token=customer.card_token)
        except Exception as e:
            log.warning("charge failed, retrying in %ss: %s", delay, e)
            time.sleep(delay)
    raise RuntimeError("charge failed after retries")
