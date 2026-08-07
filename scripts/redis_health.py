#!/usr/bin/env python3
"""Redis INFO / PING health helper. Works with redis-py if installed."""
from __future__ import annotations
import argparse, os, sys

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--host", default=os.getenv("REDIS_HOST", "127.0.0.1"))
    p.add_argument("--port", type=int, default=int(os.getenv("REDIS_PORT", "6379")))
    p.add_argument("--tls", action="store_true")
    args = p.parse_args()
    try:
        import redis
    except ImportError:
        print("redis package missing - pip install redis")
        print(f"would check {args.host}:{args.port}")
        return
    r = redis.Redis(host=args.host, port=args.port, ssl=args.tls, socket_connect_timeout=3)
    pong = r.ping()
    info = r.info(section="replication")
    print(f"PING={pong}")
    for k in ("role", "connected_slaves", "master_link_status", "master_repl_offset"):
        if k in info:
            print(f"{k}={info[k]}")
    mem = r.info(section="memory")
    print(f"used_memory_human={mem.get('used_memory_human')}")
    print(f"maxmemory_policy={mem.get('maxmemory_policy')}")

if __name__ == "__main__":
    main()
