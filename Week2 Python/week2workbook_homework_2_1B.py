def inp():
    mass=float(input('Enter the mass:'))
    velocity=float(input('Enter the velocity: '))
    return mass, velocity

def cal_ke(m, v):
    ke=1/2*m*v**2
    return ke
KE=[]
def main():
    for i in range(2):
        results=inp()
        KE.append(cal_ke(results[0],results[1]))
#         print(KE)
    print(KE)
main()
