#!/bin/bash
cd "$(dirname "$0")"
lsof -ti:8789 | xargs kill -9 2>/dev/null || true
nohup .venv/bin/uvicorn src.api.main:app --host 0.0.0.0 --port 8789 > api.out 2>&1 &
echo $! > api.pid
sleep 2
if ps -p $(cat api.pid) > /dev/null 2>&1; then
    echo "API started with PID $(cat api.pid)"
    curl -s http://localhost:8789/health | python3 -m json.tool
else
    echo "Failed to start API"
    cat api.out
fi