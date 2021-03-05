def solution(participants, completions):
    dict_completion = {}
    
    for completion in completions :
        if completion not in dict_completion.keys() :
            dict_completion[completion] = 1
        else :
            dict_completion[completion] += 1
    
    
    for participant in participants :
        if participant not in dict_completion.keys() :
            return participant
        elif dict_completion[participant] == 0 :
            return participant
        else :
            dict_completion[participant] -= 1