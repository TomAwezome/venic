import string
class Keyboard:
	def __init__(self, manager):
		self.manager = manager
		self.bindings = {}
		self.bind()
	def update(self):	# grab key and do something with it
		c = self.manager.stdscr.getch()
		if c == -1:
			return
		c = self.manager.curses.keyname(c)
		c = c.decode("utf-8")
		if c in self.bindings:
			self.bindings[c]()
		elif c in string.punctuation + string.digits + string.ascii_letters + " \t":
			self.bindings["printable-character"](c)
	def terminate(self):
		pass
	def bind(self):
		self.bindings["KEY_UP"] = self.manager.Windows["fileWindow"].moveFilecursorUp
		self.bindings["KEY_DOWN"] = self.manager.Windows["fileWindow"].moveFilecursorDown
		self.bindings["KEY_LEFT"] = self.manager.Windows["fileWindow"].moveFilecursorLeft
		self.bindings["KEY_RIGHT"] = self.manager.Windows["fileWindow"].moveFilecursorRight
		self.bindings["printable-character"] = self.manager.Windows["fileWindow"].enterTextAtFilecursor
		self.bindings["KEY_BACKSPACE"] = self.manager.Windows["fileWindow"].backspaceTextAtFilecursor
		self.bindings["KEY_DC"] = self.manager.Windows["fileWindow"].deleteTextAtFilecursor
		self.bindings["KEY_END"] = self.manager.Windows["fileWindow"].gotoEndOfLine
		self.bindings["KEY_F(3)"] = self.manager.Windows["fileWindow"].gotoStartOfFile
		self.bindings["KEY_F(4)"] = self.manager.Windows["fileWindow"].gotoEndOfFile
		self.bindings["KEY_HOME"] = self.manager.Windows["fileWindow"].gotoStartOfLine
		self.bindings["KEY_NPAGE"] = self.manager.Windows["fileWindow"].scrollDown
		self.bindings["KEY_PPAGE"] = self.manager.Windows["fileWindow"].scrollUp
		self.bindings["^D"] = self.manager.Windows["fileWindow"].deleteLineAtFilecursor
		self.bindings["^J"] = self.manager.Windows["fileWindow"].newLineAtFilecursor
		self.bindings["^W"] = self.manager.Windows["fileWindow"].saveFile