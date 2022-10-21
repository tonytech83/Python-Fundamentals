def fill_the_lift(wagons, people):
    for idx in range(len(wagons)):
        if people == 0:
            break
        if wagons[idx] == 4:
            continue
        for place in range(4):
            wagons[idx] += 1
            people -= 1
            if wagons[idx] == 4:
                break
            if people == 0:
                break

    return wagons, people


waiting_people = int(input())
lift = [int(x) for x in input().split()]

lift_status, left_people = fill_the_lift(lift, waiting_people)

if left_people == 0 and sum(lift) < len(lift) * 4:
    print(f'The lift has empty spots!')

elif left_people > 0:
    print(f"There isn't enough space! {left_people} people in a queue!")

print(*lift_status, sep=' ')
