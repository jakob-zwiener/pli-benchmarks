from collections import defaultdict

histogram = defaultdict(int)

with open('out', 'r') as input:
    for line in input:
        if not line.strip():
            continue
        histogram[int(line.strip())] += 1

with open('aggregated', 'w') as output:
    output.write(str(histogram))
