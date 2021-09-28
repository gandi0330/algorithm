n = int(input())

energy_w = list(map(int,input().split()))

energy_list = []

def cal(energy, energy_w, length):

    if length == 2:
        energy_list.append(energy)
        return

    else:
        for i in range(1,length-1):
            energy += (energy_w[i-1] * energy_w[i+1])
            cal(energy,energy_w[:i] + energy_w[i+1:], length-1)
            energy -= (energy_w[i-1] * energy_w[i+1])
    
cal(0,energy_w,n)

print(max(energy_list))

