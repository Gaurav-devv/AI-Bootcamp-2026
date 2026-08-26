# **kwargs -> you always don’t have to use Args and Kwargs the main thing is * , ** you can use any names in front of them.
#          ->**kwargs becomes a dictionary


def information(**K):
    print("your information is \n\n")
    for i in K:
        print(f"{i} : {K[i]}")

information(name = "Gaurav",age = 21, designation = "AI/ML")

