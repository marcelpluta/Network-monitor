from collections import Counter

def analyze():
    with open("data_log.txt", "r") as f:
        lines = f.readlines()

    results = []

    for line in lines:
        if "GOOD" in line:
            results.append("GOOD")
        elif "MEDIUM" in line:
            results.append("MEDIUM")
        else:
            results.append("BAD")

    count = Counter(results)

    print("\n=== NETWORK REPORT ===")
    for k, v in count.items():
        print(f"{k}: {v}")

    total = len(results)
    print(f"\nTotal samples: {total}")

analyze()
