#dayup
def dayUp(dayf):
    day=1
    for i in range(365):
        if i%7 in [0,6]:
            day=day*(1-0.01)
        else:
            day=day*(1+dayf)
    return day
