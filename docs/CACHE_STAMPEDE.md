# Cache stampede

When hot key expires, many clients hit DB.

Mitigations:

- probabilistic early expiration / soft TTL
- singleflight / request coalescing
- lock around recompute
- never cache null storms without TTL jitter
