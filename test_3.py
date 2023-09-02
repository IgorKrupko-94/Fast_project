count_cards = int(input())
self_combination = [int(x) for x in input().split()]
final_combination = [int(x) for x in input().split()]

start_index = 0
end_index = 0
for i in range(count_cards):
    if self_combination[i] != final_combination[i]:
        start_index = i
        break
for i in range(count_cards - 1, -1, -1):
    if self_combination[i] != final_combination[i]:
        end_index = i + 1
        break

self_combination[start_index:end_index] = sorted(
    self_combination[start_index:end_index])

if self_combination == final_combination:
    print('YES')
else:
    print('NO')
