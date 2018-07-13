def solver_wo_follow(n):
    # In this function, we assume only 1 or 2 steps can be taken at a time
    memory = [1,1] # Ways to climb staircase with 0 steps and 1 step respectively.
    for i in range(2,n):
        memory.append(memory[-1] + memory[-2])
    return memory[-1] + memory[-2]

def solver_w_follow(n,stepList):
    # In this function, stepList is the list of number of steps which can be taken at one point.
    if n == 0:
        return 1
    memory = [1]
    for i in range(1,n+1):
        totalSteps = 0
        for steps in stepList:
            if i >= steps:
                totalSteps = totalSteps + memory[i - steps]
        memory.append(totalSteps)
    return memory[n]

if __name__ == '__main__':
    n = int(input("Enter N:"))
    print(solver_wo_follow(n))
    print(solver_w_follow(n,[1,2]))