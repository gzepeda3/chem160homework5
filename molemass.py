#Write a function called molemass() and make it return total atomic mass based on mass table below.
names=["H", "C", "N", "O", "P", "S", "K", "F"]
masses=[1.0079,12.0107,14.0067,15.9994,30.9738,32.0660,39.0983, 18.9984]
dict1=dict(zip(names,masses))
def molemass(compound):
    mass=0
    for i in compound:
        if i in dict1.keys():
            mass += dict1[i]
    return mass
