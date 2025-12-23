# invalid ids (Part Two)
try:
    total = 0
    with open("ranges.txt", "r") as file:
        line = file.read().strip()
        section = line.split(',')
        for section_str in section:
            parts = section_str.split('-')
            start = int(parts[0])
            end = int(parts[1])
            for id_num in range(start, end + 1):
                id_str = str(id_num)
                length = len(id_str)
                if length > 0 and not id_str.startswith('0'):
                    invalid = False
                    # Check for any repetition >=2
                    for sub_len in range(1, length // 2 + 1):  # sub_len up to half length
                        if length % sub_len == 0:
                            repetitions = length // sub_len
                            if repetitions >= 2:
                                substring = id_str[:sub_len]
                                if substring * repetitions == id_str:
                                    invalid = True
                                    break
                    if invalid:
                        total += id_num
    print("Total sum of invalid id: ", total)
except Exception as e:
    print("An error occurred:", e)
input("Press Enter to exit...")