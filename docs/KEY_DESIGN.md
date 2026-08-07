# Key design

- namespace: `app:entity:id`
- avoid huge keys / big HASH without bounds
- TTLs on all cache keys
- document hot keys and eviction policy (`allkeys-lru` vs `volatile-lru`)
