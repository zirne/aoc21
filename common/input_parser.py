class Input:
	def __init__(inp_path):
		with open(inp_path, mode='r') as h:
			self.raw = h.read()
			self.list = h.readlines()
			self.
