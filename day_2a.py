try:
    total = 0
    with open('ranges.txt', 'r') as file:
        line = file.read().strip()  
    ranges = line.split(',')  
    for range_str in ranges:
        parts = range_str.split('-')
        start = int(parts[0])
        end = int(parts[1])
        for id_num in range(start, end + 1):  
            id_str = str(id_num)
            length = len(id_str)
            if length % 2 == 0 and length > 0 and not id_str.startswith('0'):
                half = length // 2  # Integer division
                first_half = id_str[:half]
                second_half = id_str[half:]
                if first_half == second_half:
                    total += id_num  # Sum the invalid ID
    print("Total sum of invalid IDs:", total)
except Exception as e:
    print("An error occurred:", e)
input("Press Enter to exit")