
import random, time, matplotlib.pyplot as plt, numpy as np, pandas as pd

def min_signs_for_visibility(intervals):
    intervals = sorted(intervals, key=lambda x: x[1])
    signs = []
    i = 0
    n = len(intervals)
    while i < n:
        _, end = intervals[i]
        signs.append(end)
        i += 1
        while i < n and intervals[i][0] <= end <= intervals[i][1]:
            i += 1
    return signs

def gen_visibility_windows(n, max_mile=100000, max_len=300):
    return [(s := random.randint(0, max_mile - 1), s + random.randint(1, max_len)) for _ in range(n)]

def benchmark_min_signs(ns, trials=3):
    rows = []
    for n in ns:
        total = 0.0
        for _ in range(trials):
            intervals = gen_visibility_windows(n)
            t0 = time.perf_counter()
            _ = min_signs_for_visibility(intervals)
            t1 = time.perf_counter()
            total += (t1 - t0)
        rows.append({"n": n, "avg_runtime_sec": total / trials})
    return pd.DataFrame(rows)

if __name__ == "__main__":
    ns = list(range(1000, 21000, 2000))
    df = benchmark_min_signs(ns)
    plt.plot(df["n"], df["avg_runtime_sec"], marker="o", label="Measured runtime")
    nvals = np.array(df["n"])
    ref = nvals * np.log2(np.maximum(2, nvals))
    scale = df["avg_runtime_sec"].iloc[-1] / ref[-1]
    plt.plot(df["n"], ref * scale, marker="x", label="n log n (scaled)")
    plt.title("Minimal Trail Signage (Greedy)")
    plt.xlabel("n (visibility windows)")
    plt.ylabel("Average runtime (sec)")
    plt.legend()
    plt.savefig("signage_greedy_runtime.png", bbox_inches="tight")
    df.to_csv("signage_greedy_timings.csv", index=False)
    print("Saved runtime data and plot.")
