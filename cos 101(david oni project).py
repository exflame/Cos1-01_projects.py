print('cos 101 assignment')
print(' work on five physics or math operation')
print('solution')
print(' Number 1 : force')
def calculate_force():
    mass=float(input('what is the value for mass'))

    acceleration = float(input('what is the value for acceleration'))

    force = mass * acceleration

    print('force is', force,'N(newton)')
calculate_force()

print(' Number 2 : volume')
def calculate_volume():


    length = float(input('what is the value of length '))
    breadth = float(input('what is the value of breadth '))
    height = float(input('what is the value of height'))

    volume = length * breadth * height
    print('volume is ', volume,)
calculate_volume()

print(' Number 3 : acceleration')
def calculate_acceleration():

    distance=float(input('what is the value of distance'))
    time=float(input('what is the value of time'))
    acceleration= distance / time

    print('acceleration is',acceleration)
calculate_acceleration()

print( ' Number 4 : area')
def calculate_area():

    length = float(input('what is the value of length '))
    breadth = float(input('what is the value of breadth '))

    area = length * breadth

    print('area is ',area  )
calculate_area()

print(' Number 5 : work')
def calculate_work():

    force=float(input('what is the value of force'))
    displacement=float(input('what is the value of displacement'))
    work= force * displacement

    print('work is',work,'j(joules)')
calculate_work()

print('assignment finished')
print('thank you')