from vpython import *
#Web VPython 3.2

# PROJ1-Q2
# Author: MAHEEN & VALERIE
# Class: PHYS1454

# create the objects:
golf = sphere(pos = vec(0,0,0), radius = 1.250, mass = 0.5, color = color.yellow, make_trail = True, trail_color = color.green)
building = box(pos = vec(80,6,0), size = vec(10,13,15), texture = textures.gravel)

t = 0
dt = 0.1
Max_height = 0
Max_time = 0

# the ball was hit with 30m/s at 50* angle so inorder to convert degree to radians- added pi.
golf.vel = vec(30*cos(50*pi/180), 30*sin(50*pi/180), 0)
# acceleration due to gravity is 9.81, put -ive 
golf.acc = vec(0, -9.81, 0)
# calculate acceleration components
golf.acc_tan = (golf.acc).proj(golf.vel)
golf.acc_rad = golf.acc - golf.acc_tan


#create velocity, acceleration, tangential and radial acc arrows 
velArr = attach_arrow(golf, "vel", color = color.magenta, round = True)
accArr = attach_arrow(golf, "acc", color = color.cyan, round = True)
acc_radArr = attach_arrow(golf, "acc_rad", color = color.white, round = True)
acc_tanArr = attach_arrow(golf, "acc_tan", color = color.purple, round = True)


#calculate the k,u,e energies as a func of t - 
#k = 1/2 mv^2 
golf.Kinetic = 0.5 * golf.mass * golf.vel.mag2
# u = mgh  = used .y as pos is a vector
golf.Potential = golf.mass * 9.81 * golf.pos.y
# e = k + u 
golf.Mechanical = golf.Kinetic + golf.Potential

# for ploting the graph- we set the x and y axis as kinetic vs t, potential vs t, mechanical vs t
graK= graph(xtitle = "Time (Second)", ytitle=" Kinetic (Joules)")
graU= graph (xtitle = "Time (Second)", ytitle=" Potential (Joules)")
graE= graph (xtitle = "Time (Second)", ytitle = "Mechanical (Joules)")

#adding the curve to the graph of each, set the width to 2   
gKinetic = gcurve(graph=graK, color=color.blue, width = 2)
gPotential = gcurve(graph=graU, color=color.red, width = 2)
gMechanical = gcurve(graph=graE, color=color.purple, width = 2)

#plotting the graphs
gKinetic.plot(t,golf.Kinetic)
gPotential.plot(t,golf.Potential)
gMechanical.plot(t,golf.Mechanical)

#setting the cam to follow the golf motion
scene.camera.follow(golf)

#making sure that height > 11.5 ALSO pos is greater than 0 using while statement
#loop to animate the golf
while golf.pos.y > 11.5 or golf.vel.y > 0:
    
    #sets the rate to control loop speed
    rate(1/dt)
    
    #updating for new value of pos and velocity w respect to change in time
    golf.pos = golf.pos + golf.vel*dt
    golf.vel = golf.vel + golf.acc*dt
    golf.Kinetic = 0.5 * golf.mass * golf.vel.mag2
    golf.Potential = golf.mass * 9.81 * golf.pos.y
    golf.Mechanical = golf.Kinetic + golf.Potential
    
    #update the time variable 
    t = t + dt
    # calculate acceleration components
    golf.acc_tan = (golf.acc).proj(golf.vel)
    golf.acc_rad = golf.acc - golf.acc_tan
    
    #updating the plot as well with new values of K,U,E
    gKinetic.plot(t,golf.Kinetic)
    gPotential.plot(t,golf.Potential)
    gMechanical.plot(t,golf.Mechanical)
    
    #incase if y less than 0.05 and greater than -0.05 then set the max height = pos and max time = t - otherwise the v and t is 0 
    if (golf.vel.y < 0.05 and golf.vel.y > -0.05):
        Max_height = golf.pos.y
        Max_time = t


print("* Before landing time in air = " + t + " s \n")
print("* Range = " + golf.pos.x + " m \n")
print("* Max height reached by ball = " + Max_height + " m \n")
print("* Time to reach max height = " + Max_time + "s \n")
print("* Ball's Velocity when hitting the roof = " + golf.vel + " m/s")
