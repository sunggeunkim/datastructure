from threading import Thread, Lock
import time

class TimeException(Exception):
	pass

class Timer:
	def __init__(t, init):
		t.init = init
		t.lock = Lock()
		t.kill = False

	def timer_thread(t):
		t.current = t.init
		while True:
			try:
				t.lock.acquire()

				if t.current<= 0: break
				if t.kill: break
				
				t.current -= 1
				print(t.current)
			finally:
				t.lock.release()			
			time.sleep(1)
	
	def reset(t):
		try:
			t.lock.acquire()
			t.current = t.init
		finally:
			t.lock.release()
	
	def stop(t):
		try:
			t.lock.acquire()
			t.kill = True
		finally:
			t.lock.release()

	def time(t):
		try:
			t.lock.acquire()
			return t.current
		finally:
			t.lock.release()

	def start(t):
		Thread(target=t.timer_thread).start()

t = Timer(5)
t.start()
time.sleep(2)
t.reset()
time.sleep(2)
t.stop()
