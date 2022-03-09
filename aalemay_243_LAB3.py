def pizza_coverage(r_pizza, r_pep, num_pep):
    pep_area1 = (3.14159) * (r_pep * r_pep)
    pep_area2 = num_pep * pep_area1
    pizza_area = (3.14159) * (r_pizza * r_pizza)
    final_area = pizza_area - pep_area2
    if final_area/pizza_area <= 0.25:
        mood = "happy customer"
    elif final_area/pizza_area > 0.25 and final_area/pizza_area <= 0.5:
        mood = "neural customer"
    else:
        mood = "sad customer"
    return mood
    
print(pizza_coverage(5,1,10))
print(pizza_coverage(5,1,15))
print(pizza_coverage(5,1,20))