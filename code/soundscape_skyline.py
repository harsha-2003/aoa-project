
import random, time, matplotlib.pyplot as plt, numpy as np, pandas as pd

def skyline(events):
    def merge(S1, S2):
        i = j = 0
        h1 = h2 = 0
        res = []
        while i < len(S1) and j < len(S2):
            if S1[i][0] < S2[j][0]:
                x, h1 = S1[i]; i += 1
            elif S1[i][0] > S2[j][0]:
                x, h2 = S2[j]; j += 1
            else:
                x = S1[i][0]; h1 = S1[i][1]; h2 = S2[j][1]; i += 1; j += 1
            h = max(h1, h2)
            if not res or res[-1][1] != h:
                res.append((x, h))
        while i < len(S1):
            if not res or res[-1][1] != S1[i][1]:
                res.append(S1[i])
            i += 1
        while j < len(S2):
            if not res or res[-1][1] != S2[j][1]:
                res.append(S2[j])
            j += 1
        return res

    def build(evts):
        if not evts:
            return []
        if len(evts) == 1:
            L, R, H = evts[0]
            return [(L, H), (R, 0)]
        mid = len(evts) // 2
        left = build(evts[:mid])
        right = build(evts[mid:])
        return merge(left, right)

    events_sorted = sorted(events, key=lambda x: (x[0], x[1], -x[2]))
    return build(events_sorted)

def gen_events(n, max_t=100000, max_dur=400, max_h=200):
    return [(L := random.randint(0, max_t - 1), L + random.randint(1, max_dur), random.randint(1, max_h)) for _ in range(n)]

def benchmark_skyline(ns, trials=3):
    rows = []
    for n in ns:
        total = 0.0
        for _ in range(trials):
            evts = gen_events(n)
            t0 = time.perf_counter()
            _ = skyline(evts)
            t1 = time.perf_counter()
            total += (t1 - t0)
        rows.append({"n": n, "avg_runtime_sec": total / trials})
    return pd.DataFrame(rows)

if __name__ == "__main__":
    ns = list(range(500, 10500, 1000))
    df = benchmark_skyline(ns)
    plt.plot(df["n"], df["avg_runtime_sec"], marker="o", label="Measured runtime")
    nvals = np.array(df["n"])
    ref = nvals * np.log2(np.maximum(2, nvals))
    scale = df["avg_runtime_sec"].iloc[-1] / ref[-1]
    plt.plot(df["n"], ref * scale, marker="x", label="n log n (scaled)")
    plt.title("City Soundscape Outline (D&C)")
    plt.xlabel("n (events)")
    plt.ylabel("Average runtime (sec)")
    plt.legend()
    plt.savefig("soundscape_skyline_runtime.png", bbox_inches="tight")
    df.to_csv("soundscape_skyline_timings.csv", index=False)
    print("Saved runtime data and plot.")
