def add(tasks):
	sm= 0
	for i in tasks:
		sm += i.rem_bt
	return sm
class Task:
	def __init__(self, at, deadline, bt):
		self.at, self.deadline, self.bt = int(at), int(deadline), int(bt)
		self.rem_bt = self.bt
		self.execution_seconds = list()
	def execute(self, time):
		self.execution_seconds.append(time)
		self.rem_bt -= 1
	def is_finished(self):
		return True if self.bt==0 else False
	def display_status(self):
		print ("Task: A.T =",self.at,
			", Deadline = ",self.deadline,
			", Burst = ",self.bt,
			", Finished = ",self.is_finished(),
			", Remaining burst = ",self.rem_bt,
			", Execution at =",self.execution_seconds)

print("Enter no. of processes?")
n = int(input())
print ("Enter <Arrival time> <Deadline> <Burst time>")
all_tasks = list()
queue = list()
for _ in range(n):
	x,y,z = input().split()
	all_tasks.append(Task(x,y,z))
all_tasks.sort(key = lambda task: task.deadline)
curr_time = -1
while add(all_tasks)!=0:
	curr_time+=1
	for task in all_tasks:
		if task.at==curr_time:
			queue.append(task)
	queue.sort(key = lambda task: task.deadline)
	queue[0].execute(curr_time)
	if queue[0].is_finished():
		queue.pop(0)
for task in all_tasks:
	task.display_status()

