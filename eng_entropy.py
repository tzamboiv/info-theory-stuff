import math

def ent_eng():
    prob_list = [.08167,.01492, .02782, .04253, .12702, .02228, .02015, .06094, .06966, .000153, .00772, .04025, .02406, .06749, .07507, .01929, .00095, .05987, .06327, .09056, .02758, .00978, .02361, .00150, .01974, .00074]
    res = 0
    hold_list = []
    for i in prob_list:
        hold_list.append(i * math.log(i,2))
    res = -sum(hold_list)
    return res
print ent_eng()

def reader(x_string):
    diction = {}
    for i in x_string:
        if i in diction:
            diction[i] +=1
        else:
            diction[i] = 1
    return diction

def frequency(x_string):
    big = float(len(x_string))
    freq_dict = {}
    y = reader(x_string)
    for k, v in y.items():
        freq_dict[k] = v/big
    return freq_dict
def entropy_est(x_string):
    vals = frequency(x_string).values()
    res = 0
    hold_list = []
    for i in vals:
        hold_list.append(i * math.log(i,2))
    res = -sum(hold_list)
    return res
print reader("teddy")
print frequency("teddy")
print entropy_est("teddy")
