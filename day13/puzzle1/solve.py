with open('./input') as input_file:
    raw_lines = input_file.readlines()

earliest_timestamp = int(raw_lines[0])
bus_ids = sorted(set(int(x) for x in raw_lines[1].split(',') if x != "x"))


print(earliest_timestamp)
print(bus_ids)


def get_earliest_time(bus_id):
    multiplier = earliest_timestamp // bus_id
    if multiplier * bus_id == earliest_timestamp:
        return multiplier * bus_id
    else:
        return (multiplier + 1) * bus_id


earliest_per_bus = [
    (bus_id, get_earliest_time(bus_id))
    for bus_id in bus_ids
]

print(earliest_per_bus)

earliest_bus = sorted(earliest_per_bus, key=lambda x: x[1])[0]

depart_bus_id, depart_timestamp = earliest_bus
print(earliest_bus)

# multiplier = earliest_timestamp // bus_ids[-1]
# print("first_multiplier", multiplier)

# depart_timestamp = None
# depart_bus_id = None
# while not depart_bus_id:
# print("multiplier", multiplier)
# for bus_id in bus_ids:
# if multiplier * bus_id > earliest_timestamp:
# depart_timestamp = multiplier * bus_id
# depart_bus_id = bus_id
# break

# multiplier += 1

minutes_passed = depart_timestamp - earliest_timestamp
print("minutes_passed", minutes_passed)
print("depart_bus_id", depart_bus_id)
print(minutes_passed * depart_bus_id)

# minutes_passed = 0
# good_bus_id = None
# while True:
# print(minutes_passed)
# for bus_id in bus_ids:
# if earliest_timestamp % bus_id == 0:
# good_bus_id = bus_id
# break
# minutes_passed += 1
# earliest_timestamp += 1
