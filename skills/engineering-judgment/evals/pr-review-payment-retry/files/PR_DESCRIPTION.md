# Add retries to card charging

The payment gateway times out on roughly 0.5% of charges and we've been losing checkout
conversions because of it. This wraps `charge_customer` in retries with exponential backoff.

I made the retry strategy pluggable (strategy + factory) in case we want linear backoff or
jitter later. Added some logging so we can debug failed charges.

`charge_customer` is called directly from the checkout request handler.
