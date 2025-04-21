from collections import deque

packet_stream = [      # list of names and where they belong
    "S Mary", "P Dee", "P Dee", "E Eileen", "E Mike", "E Joe",
    "P Dee", "E Vicky", "E George", "P Dee", "P Joe", "E Sally",
    "P Joe", "S Pete", "P Dee", "S Bill", "S Chase", "E Price",
    "P Dee", "E Sue"
]

with open("packet_stream.txt", "w") as f:
    f.write("\n".join(packet_stream))

def read_input_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def build_queues(packets):        # making queues
    premium = deque()
    standard = deque()
    economy = deque()

    for packet in packets:
        if packet.startswith('P'):
            premium.append(packet)
        elif packet.startswith('S'):
            standard.append(packet)
        elif packet.startswith('E'):
            economy.append(packet)

    return premium, standard, economy

def apply_wfq(premium, standard, economy):
    while premium or standard or economy:
        for _ in range(3):
            if premium:
                print(premium.popleft())
        for _ in range(2):
            if standard:
                print(standard.popleft())
        for _ in range(1):
            if economy:
                print(economy.popleft())


def main():
    filename = 'packet_stream.txt'
    packets = read_input_file(filename)
    premium, standard, economy = build_queues(packets)

    print("Queues Built")
    print ("")
    print("Premium Queue:")
    for p in premium: print("  ", p)

    print("\nStandard Queue:")
    for s in standard: print("  ", s)

    print("\nEconomy Queue:")
    for e in economy: print("  ", e)

    print("\nWFQ Dequeue Output")
    apply_wfq(premium, standard, economy)

if __name__ == '__main__':
    main()
