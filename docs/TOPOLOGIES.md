# Topologies

| Pattern | When |
|---------|------|
| Primary + replica | Simple HA, read scale limited |
| Cluster mode | Large dataset, slot-based scale out |
| ElastiCache Multi-AZ | Managed failover |
| Client-side cluster | redis-py / lettuce cluster aware |

Prefer TLS + AUTH in all non-local environments.
