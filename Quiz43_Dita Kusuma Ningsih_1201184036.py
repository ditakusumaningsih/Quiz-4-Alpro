listGPA= [2.1,2.5,4,3]
def h (GPA):
    b = 500000
    h = GPA * b
    return h

for GPA in listGPA :
    if GPA > 2.5:
        print("Hadiah anda adalah : Rp", h(GPA))
    else :
        print("Maaf,Tidak Ada Bonus")

