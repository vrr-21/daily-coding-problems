def solver_wo_follow(n):
    # In this function, we assume only 1 or 2 steps can be taken at a time
    memory = [1,1] # Ways to climb staircase with 0 steps and 1 step respectively.
    for i in range(2,n):
        memory.append(memory[-1] + memory[-2])
    return memory[-1] + memory[-2]

if __name__ == '__main__':
    n = int(input("Enter N:"))
    print(solver_wo_follow(n))