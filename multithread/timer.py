from threading import Thread, Lock
import time

class TimeException(Exception):
	pass

class Timer:
	def __init__(self, init):
		self.init = init
		self.lock = Lock()
		self.kill = False

	def timer_thread(self):
		self.current = self.init
		while True:
			with self.lock:
				if self.current<= 0: break
				if self.kill: break
				
				self.current -= 1
				print(self.current)
			time.sleep(1)
	
	def reset(self):
		with self.lock:
			self.current = self.init
	
	def stop(self):
		with self.lock:
			self.kill = True

	def time(self):
		with self.lock:
			return self.current

	def start(self):
		Thread(target=self.timer_thread).start()

t = Timer(5)
t.start()
time.sleep(2)
t.reset()
time.sleep(2)
t.stop()
