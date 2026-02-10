def cohens_kappa(rater1, rater2):
    if rater1 == rater2:
        return 1.0
    if len(rater1) != len(rater2):
        return 0
    n = len(rater1)

    if n == 0:
        return 0 

    num_agreements = 0
    label_count_1 = {}
    label_count_2 = {}
    
    for i in range(n):
        if rater1[i] == rater2[i]:
            num_agreements += 1
        if rater1[i] in label_count_1.keys():
            label_count_1[rater1[i]] += 1
        else:
            label_count_1[rater1[i]] = 1

        if rater2[i] in label_count_2.keys():
            label_count_2[rater2[i]] += 1
        else:
            label_count_2[rater2[i]] = 1
        
    for key in label_count_1.keys():
        if key not in label_count_2.keys():
            label_count_2[key] = 0

    for key in label_count_2.keys():
        if key not in label_count_1.keys():
            label_count_1[key] = 0

    p_e = 0
    for key in label_count_1.keys():   
        p_e += label_count_1[key]/n * label_count_2[key]/n 
    
    return (num_agreements/n - p_e)/(1 - p_e)


    

