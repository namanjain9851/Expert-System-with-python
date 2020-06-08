class college:
	name=""
	program=""
	Quota=""
	Seat_Type=""
	opening_rank=""
	closing_rank=""
	rank=""
	branch_priority=""
	def __init__(self,name,program,Quota,Seat_Type,opening_rank,closing_rank,rank,branch_priority):
		self.name=name
		self.program=program
		self.Quota=Quota
		self.Seat_Type=Seat_Type
		self.opening_rank=opening_rank
		self.closing_rank=closing_rank
		self.rank=rank
		self.branch_priority=branch_priority
	def ToString(self):
		return self.name+'\t'+self.program+'\t'+self.Quota+'\t'+self.Seat_Type+'\t'+str(self.opening_rank)+'\t'+str(self.closing_rank)
	def withname(self):
		return self.name+'\t'+'$'+self.program+'\t'+'$'+self.Quota+'\t'+'$'+self.Seat_Type+'\t'+'$'+str(self.opening_rank)+'\t'+'$'+str(self.closing_rank)

