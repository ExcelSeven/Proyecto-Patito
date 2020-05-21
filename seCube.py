class SemanticCube:
	def __init__(self):
		self.cube = dict()

		#Int
		self.cube[("&&", "Int", "Int")]     = "Error"
		self.cube[("||", "Int", "Int")]     = "Error"
		self.cube[(">=", "Int", "Int")]     = "Bool"
		self.cube[("<=", "Int", "Int")]     = "Bool"
		self.cube[(">", "Int", "Int")]      = "Bool"
		self.cube[("<", "Int", "Int")]      = "Bool"
		self.cube[("==", "Int", "Int")]     = "Bool"
		self.cube[("!=", "Int", "Int")]     = "Bool"
		self.cube[("+", "Int", "Int")]      = "Int"
		self.cube[("-", "Int", "Int")]      = "Int"
		self.cube[("*", "Int", "Int")]      = "Int"
		self.cube[("/", "Int", "Int")]      = "Int"
		self.cube[("=", "Int", "Int")]      = "Int"

		self.cube[("&&", "Int", "Float")]   = "Error"
		self.cube[("||", "Int", "Float")]   = "Error"
		self.cube[(">=", "Int", "Float")]   = "Bool"
		self.cube[("<=", "Int", "Float")]   = "Bool"
		self.cube[(">", "Int", "Float")]    = "Bool"
		self.cube[("<", "Int", "Float")]    = "Bool"
		self.cube[("==", "Int", "Float")]   = "Bool"
		self.cube[("!=", "Int", "Float")]   = "Bool"
		self.cube[("+", "Int", "Float")]    = "Float"
		self.cube[("-", "Int", "Float")]    = "Float"
		self.cube[("*", "Int", "Float")]    = "Float"
		self.cube[("/", "Int", "Float")]    = "Float"
		self.cube[("=", "Int", "Float")]    = "Int"

		self.cube[("&&", "Int", "Char")]    = "Error"
		self.cube[("||", "Int", "Char")]    = "Error"
		self.cube[(">=", "Int", "Char")]    = "Error"
		self.cube[("<=", "Int", "Char")]    = "Error"
		self.cube[(">", "Int", "Char")]     = "Error"
		self.cube[("<", "Int", "Char")]     = "Error"
		self.cube[("==", "Int", "Char")]    = "Error"
		self.cube[("!=", "Int", "Char")]    = "Error"
		self.cube[("+", "Int", "Char")]     = "Error"
		self.cube[("-", "Int", "Char")]     = "Error"
		self.cube[("*", "Int", "Char")]     = "Error"
		self.cube[("/", "Int", "Char")]     = "Error"
		self.cube[("=", "Int", "Char")]     = "Error"

		#Float
		self.cube[("&&", "Float", "Int")]   = "Error"
		self.cube[("||", "Float", "Int")]   = "Error"
		self.cube[(">=", "Float", "Int")]   = "Bool"
		self.cube[("<=", "Float", "Int")]   = "Bool"
		self.cube[(">", "Float", "Int")]    = "Bool"
		self.cube[("<", "Float", "Int")]    = "Bool"
		self.cube[("==", "Float", "Int")]   = "Bool"
		self.cube[("!=", "Float", "Int")]   = "Bool"
		self.cube[("+", "Float", "Int")]    = "Float"
		self.cube[("-", "Float", "Int")]    = "Float"
		self.cube[("*", "Float", "Int")]    = "Float"
		self.cube[("/", "Float", "Int")]    = "Float"
		self.cube[("=", "Float", "Int")]    = "Float"

		self.cube[("&&", "Float", "Float")] = "Error"
		self.cube[("||", "Float", "Float")] = "Error"
		self.cube[(">=", "Float", "Float")] = "Bool"
		self.cube[("<=", "Float", "Float")] = "Bool"
		self.cube[(">", "Float", "Float")]  = "Bool"
		self.cube[("<", "Float", "Float")]  = "Bool"
		self.cube[("==", "Float", "Float")] = "Bool"
		self.cube[("!=", "Float", "Float")] = "Bool"
		self.cube[("+", "Float", "Float")]  = "Float"
		self.cube[("-", "Float", "Float")]  = "Float"
		self.cube[("*", "Float", "Float")]  = "Float"
		self.cube[("/", "Float", "Float")]  = "Float"
		self.cube[("=", "Float", "Float")]  = "Float"

		self.cube[("&&", "Float", "Char")]  = "Error"
		self.cube[("||", "Float", "Char")]  = "Error"
		self.cube[(">=", "Float", "Char")]  = "Error"
		self.cube[("<=", "Float", "Char")]  = "Error"
		self.cube[(">", "Float", "Char")]   = "Error"
		self.cube[("<", "Float", "Char")]   = "Error"
		self.cube[("==", "Float", "Char")]  = "Error"
		self.cube[("!=", "Float", "Char")]  = "Error"
		self.cube[("+", "Float", "Char")]   = "Error"
		self.cube[("-", "Float", "Char")]   = "Error"
		self.cube[("*", "Float", "Char")]   = "Error"
		self.cube[("/", "Float", "Char")]   = "Error"
		self.cube[("=", "Float", "Char")]   = "Error"

		#Char
		self.cube[("&&", "Char", "Int")]    = "Error"
		self.cube[("||", "Char", "Int")]    = "Error"
		self.cube[(">=", "Char", "Int")]    = "Error"
		self.cube[("<=", "Char", "Int")]    = "Error"
		self.cube[(">", "Char", "Int")]     = "Error"
		self.cube[("<", "Char", "Int")]     = "Error"
		self.cube[("==", "Char", "Int")]    = "Error"
		self.cube[("!=", "Char", "Int")]    = "Error"
		self.cube[("+", "Char", "Int")]     = "Error"
		self.cube[("-", "Char", "Int")]     = "Error"
		self.cube[("*", "Char", "Int")]     = "Error"
		self.cube[("/", "Char", "Int")]     = "Error"
		self.cube[("=", "Char", "Int")]     = "Error"

		self.cube[("&&", "Char", "Float")]  = "Error"
		self.cube[("||", "Char", "Float")]  = "Error"
		self.cube[(">=", "Char", "Float")]  = "Error"
		self.cube[("<=", "Char", "Float")]  = "Error"
		self.cube[(">", "Char", "Float")]   = "Error"
		self.cube[("<", "Char", "Float")]   = "Error"
		self.cube[("==", "Char", "Float")]  = "Error"
		self.cube[("!=", "Char", "Float")]  = "Error"
		self.cube[("+", "Char", "Float")]   = "Error"
		self.cube[("-", "Char", "Float")]   = "Error"
		self.cube[("*", "Char", "Float")]   = "Error"
		self.cube[("/", "Char", "Float")]   = "Error"
		self.cube[("=", "Char", "Float")]   = "Error"

		self.cube[("&&", "Char", "Char")]   = "Error"
		self.cube[("||", "Char", "Char")]   = "Error"
		self.cube[(">=", "Char", "Char")]   = "Error"
		self.cube[("<=", "Char", "Char")]   = "Error"
		self.cube[(">", "Char", "Char")]    = "Error"
		self.cube[("<", "Char", "Char")]    = "Error"
		self.cube[("==", "Char", "Char")]   = "Bool"
		self.cube[("!=", "Char", "Char")]   = "Bool"
		self.cube[("+", "Char", "Char")]    = "Char"
		self.cube[("-", "Char", "Char")]    = "Error"
		self.cube[("*", "Char", "Char")]    = "Error"
		self.cube[("/", "Char", "Char")]    = "Error"
		self.cube[("=", "Char", "Char")]    = "Char"

	def checkResult(self, operator, op1, op2):
		key = (operator, op1, op2)
		if key in self.cube:
			return self.cube[key]
		else:
			return "Error"
