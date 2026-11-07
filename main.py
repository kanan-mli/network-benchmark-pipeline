import pandas as pd
import requests
import pyarrow

print("Environment is working!")

data = {
    "server": ["server-1", "server-2", "server-3"],
    "latency_ms": [25, 40, 18]
}

df = pd.DataFrame(data)

print(df)
print("Average latency:", df["latency_ms"].mean())