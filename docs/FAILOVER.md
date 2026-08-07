# Failover

1. Detect primary loss (managed event or sentinel)
2. Promote replica - verify clients reconnect
3. Watch keyspace / lag if async replication
4. Expect brief connection errors - clients need retry + backoff
5. Post-failover: confirm replica count restored
