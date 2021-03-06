class SemanticCube:
	def __init__(self):
		self.cube = dict()

		#int
		self.cube[("&&", "int", "int")]     = "Error"
		self.cube[("||", "int", "int")]     = "Error"
		self.cube[(">=", "int", "int")]     = "bool"
		self.cube[("<=", "int", "int")]     = "bool"
		self.cube[(">", "int", "int")]      = "bool"
		self.cube[("<", "int", "int")]      = "bool"
		self.cube[("==", "int", "int")]     = "bool"
		self.cube[("!=", "int", "int")]     = "bool"
		self.cube[("+", "int", "int")]      = "int"
		self.cube[("-", "int", "int")]      = "int"
		self.cube[("*", "int", "int")]      = "int"
		self.cube[("/", "int", "int")]      = "int"
		self.cube[("=", "int", "int")]      = "int"

		self.cube[("&&", "int", "float")]   = "Error"
		self.cube[("||", "int", "float")]   = "Error"
		self.cube[(">=", "int", "float")]   = "bool"
		self.cube[("<=", "int", "float")]   = "bool"
		self.cube[(">", "int", "float")]    = "bool"
		self.cube[("<", "int", "float")]    = "bool"
		self.cube[("==", "int", "float")]   = "bool"
		self.cube[("!=", "int", "float")]   = "bool"
		self.cube[("+", "int", "float")]    = "float"
		self.cube[("-", "int", "float")]    = "float"
		self.cube[("*", "int", "float")]    = "float"
		self.cube[("/", "int", "float")]    = "float"
		self.cube[("=", "int", "float")]    = "int"

		self.cube[("&&", "int", "char")]    = "Error"
		self.cube[("||", "int", "char")]    = "Error"
		self.cube[(">=", "int", "char")]    = "Error"
		self.cube[("<=", "int", "char")]    = "Error"
		self.cube[(">", "int", "char")]     = "Error"
		self.cube[("<", "int", "char")]     = "Error"
		self.cube[("==", "int", "char")]    = "Error"
		self.cube[("!=", "int", "char")]    = "Error"
		self.cube[("+", "int", "char")]     = "Error"
		self.cube[("-", "int", "char")]     = "Error"
		self.cube[("*", "int", "char")]     = "Error"
		self.cube[("/", "int", "char")]     = "Error"
		self.cube[("=", "int", "char")]     = "Error"

		#float
		self.cube[("&&", "float", "int")]   = "Error"
		self.cube[("||", "float", "int")]   = "Error"
		self.cube[(">=", "float", "int")]   = "bool"
		self.cube[("<=", "float", "int")]   = "bool"
		self.cube[(">", "float", "int")]    = "bool"
		self.cube[("<", "float", "int")]    = "bool"
		self.cube[("==", "float", "int")]   = "bool"
		self.cube[("!=", "float", "int")]   = "bool"
		self.cube[("+", "float", "int")]    = "float"
		self.cube[("-", "float", "int")]    = "float"
		self.cube[("*", "float", "int")]    = "float"
		self.cube[("/", "float", "int")]    = "float"
		self.cube[("=", "float", "int")]    = "float"

		self.cube[("&&", "float", "float")] = "Error"
		self.cube[("||", "float", "float")] = "Error"
		self.cube[(">=", "float", "float")] = "bool"
		self.cube[("<=", "float", "float")] = "bool"
		self.cube[(">", "float", "float")]  = "bool"
		self.cube[("<", "float", "float")]  = "bool"
		self.cube[("==", "float", "float")] = "bool"
		self.cube[("!=", "float", "float")] = "bool"
		self.cube[("+", "float", "float")]  = "float"
		self.cube[("-", "float", "float")]  = "float"
		self.cube[("*", "float", "float")]  = "float"
		self.cube[("/", "float", "float")]  = "float"
		self.cube[("=", "float", "float")]  = "float"

		self.cube[("&&", "float", "char")]  = "Error"
		self.cube[("||", "float", "char")]  = "Error"
		self.cube[(">=", "float", "char")]  = "Error"
		self.cube[("<=", "float", "char")]  = "Error"
		self.cube[(">", "float", "char")]   = "Error"
		self.cube[("<", "float", "char")]   = "Error"
		self.cube[("==", "float", "char")]  = "Error"
		self.cube[("!=", "float", "char")]  = "Error"
		self.cube[("+", "float", "char")]   = "Error"
		self.cube[("-", "float", "char")]   = "Error"
		self.cube[("*", "float", "char")]   = "Error"
		self.cube[("/", "float", "char")]   = "Error"
		self.cube[("=", "float", "char")]   = "Error"

		#char
		self.cube[("&&", "char", "int")]    = "Error"
		self.cube[("||", "char", "int")]    = "Error"
		self.cube[(">=", "char", "int")]    = "Error"
		self.cube[("<=", "char", "int")]    = "Error"
		self.cube[(">", "char", "int")]     = "Error"
		self.cube[("<", "char", "int")]     = "Error"
		self.cube[("==", "char", "int")]    = "Error"
		self.cube[("!=", "char", "int")]    = "Error"
		self.cube[("+", "char", "int")]     = "Error"
		self.cube[("-", "char", "int")]     = "Error"
		self.cube[("*", "char", "int")]     = "Error"
		self.cube[("/", "char", "int")]     = "Error"
		self.cube[("=", "char", "int")]     = "Error"

		self.cube[("&&", "char", "float")]  = "Error"
		self.cube[("||", "char", "float")]  = "Error"
		self.cube[(">=", "char", "float")]  = "Error"
		self.cube[("<=", "char", "float")]  = "Error"
		self.cube[(">", "char", "float")]   = "Error"
		self.cube[("<", "char", "float")]   = "Error"
		self.cube[("==", "char", "float")]  = "Error"
		self.cube[("!=", "char", "float")]  = "Error"
		self.cube[("+", "char", "float")]   = "Error"
		self.cube[("-", "char", "float")]   = "Error"
		self.cube[("*", "char", "float")]   = "Error"
		self.cube[("/", "char", "float")]   = "Error"
		self.cube[("=", "char", "float")]   = "Error"

		self.cube[("&&", "char", "char")]   = "Error"
		self.cube[("||", "char", "char")]   = "Error"
		self.cube[(">=", "char", "char")]   = "Error"
		self.cube[("<=", "char", "char")]   = "Error"
		self.cube[(">", "char", "char")]    = "Error"
		self.cube[("<", "char", "char")]    = "Error"
		self.cube[("==", "char", "char")]   = "bool"
		self.cube[("!=", "char", "char")]   = "bool"
		self.cube[("+", "char", "char")]    = "char"
		self.cube[("-", "char", "char")]    = "Error"
		self.cube[("*", "char", "char")]    = "Error"
		self.cube[("/", "char", "char")]    = "Error"
		self.cube[("=", "char", "char")]    = "char"

	def checkResult(self, op1, op2, operator):
		key = (op1, op2, operator)
		if key in self.cube:
			return self.cube[key]
		# elif isinstance(int(op1), int) == True or isinstance(float(op1), float) == True or isinstance(op2, int) == True or isinstance(op2, float) == True:
		# 	return self.cube[key]
		else:
			return "Type Mismatch!"
