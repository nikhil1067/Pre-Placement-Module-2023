from collections import Counter
    summary = Counter(nums)
    
    result = [[]]
    
    for i in summary.keys():
        N = summary[i]
        new = []
        for j in range(N+1):
            new.append([i] * j)
        new_result = []
        for old in result:
            for sub in new:
                new_sub = old + sub
                new_result.append(new_sub)
        result = new_result
            

    return result