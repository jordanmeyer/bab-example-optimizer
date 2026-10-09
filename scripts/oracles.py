"""Independent standard-library integer enumeration; never imports application code."""
from itertools import product


def enumerate_case(label, contributions, use, capacities, bounds):
    feasible = []
    for quantities in product(*(range(low, high + 1) for low, high in bounds)):
        used = [sum(a * b for a, b in zip(row, quantities)) for row in use]
        if all(a <= b for a, b in zip(used, capacities)):
            feasible.append((sum(a * b for a, b in zip(contributions, quantities)), quantities, used))
    best = max((x[0] for x in feasible), default=None)
    print(label, 'feasible', len(feasible), 'optimal', [x for x in feasible if x[0] == best])


enumerate_case('bakery', [25,22,40], [[12,10,20],[18,12,25],[8,10,15]], [480,590,360], [(4,24),(3,30),(2,18)])
enumerate_case('tiny', [5,4], [[2,1],[1,2],[1,1]], [8,8,6], [(0,8),(0,8)])
for machine in [18,19,20]:
    enumerate_case(f'workshop machine{machine}', [11,19,31], [[2,3,5],[1,3,4],[2,4,6]], [machine,18,24], [(0,6),(0,4),(0,3)])
# Tiny LP bound: objective = 2*(2x+y) + 1*(x+2y) <= 24.
# x=y=8/3 attains24, so rounding is not needed to prove the bound.
# Original 600-oven case certificate: oven×37/42 + packing×8/7
# + celebration upper-bound18×5/6 gives objective <=955, attained at5/5/18.

for caps in [[540,590,360],[480,650,360],[480,590,420]]:
    enumerate_case(str(caps),[25,22,40],[[12,10,20],[18,12,25],[8,10,15]],caps,[(4,24),(3,30),(2,18)])
# Revised LP certificate in dollars: oven + packing gives coefficients
# x26, y22, z40. Subtract x>=4: objective<=590+360-4=946.
# Feasible vertex x4,y43/7,z622/35 attains946.

for oven in [9940,9941,10000]:
    enumerate_case(f"oven{oven}",[25,22,40],[[12,10,20],[18,12,25],[8,10,15]],[480,oven,360],[(4,24),(3,30),(2,18)])
print('greedy', 5*25+4*22+18*40, [5*12+4*10+18*20,5*18+4*12+18*25,5*8+4*10+18*15])
print('minimum oven',4*18+3*12+2*25)
