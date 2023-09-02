sum_money, count_bill = [int(x) for x in input().split()]
nominals = [int(x) for x in input().split()]

nominals *= 2
nominals.sort(reverse=True)
final_nominals = []
for elem in nominals:
    if sum(final_nominals) + elem == sum_money:
        final_nominals.append(elem)
        break
    elif sum(final_nominals) + elem > sum_money:
        continue
    else:
        final_nominals.append(elem)

if sum(final_nominals) < sum_money:
    print(-1)
else:
    print(len(final_nominals))
    print(*sorted(final_nominals))
