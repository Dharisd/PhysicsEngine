"""
=========================
Simple animation examples
=========================

This example contains two animations. The first is a random walk plot. The
second is an image animation.
"""
#we need to add classes to this so we have a dt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class world:

	def __init__(self):
		self.dt = 1/60
		self.elapsed_time = 0
		self.particle = np.asarray([20,55,5,50],dtype=float) #xpos,ypos, vertical velocity ,horizontal velocity
		self.g = -9.8



	def step(self):
		self.elapsed_time += self.dt
		self.particle[1] += self.dt * self.particle[2]
		self.particle[0] += self.dt * self.particle[3]
		print(self.particle[2])
		#update position
		new_ypos = self.particle[1] + self.particle[2] 
		new_xpos = self.particle[0] + self.particle[3] * self.dt

		if new_ypos >= 0.7:
			self.particle[1] += self.particle[2]
		else:
			self.particle[2] = -0.7 * self.particle[2]
			self.particle[3] *= 0.8

		if new_xpos <= 0 or new_xpos >= 100:
			self.particle[3] *= -1

		#gravity
		self.particle[2] += 1.5 * self.g * self.dt





system = world()



fig = plt.figure()
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
plot = fig.add_subplot(111, aspect='equal', autoscale_on=False,
                     xlim=(0, 100), ylim=(0, 100))


# particles holds the locations of the particle
particles, = plot.plot([], [], 'bo', ms=6)


def init():
	global system
	particles.set_data([],[])
	return particles

def animate(i):
	system.step()
	
	particles.set_data(system.particle[0],system.particle[1])
	
	return particles








line_ani = animation.FuncAnimation(fig, animate, 60,interval=30,init_func=init)



plt.show()