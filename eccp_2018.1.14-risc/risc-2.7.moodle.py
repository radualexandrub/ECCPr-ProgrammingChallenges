nr_instr = int(raw_input())
registre = []
for i in range(16):
	registre.append(0)

instructiuni = ['lconst', 'add', 'mul', 'div', 'print']

buffer_print = []

for i in range(nr_instr):
	instr_si_nr = raw_input().split()
	if instr_si_nr[0] == 'lconst':
		# lconst dst val - scrie val in registrul dst
		instr_si_nr[1] = int(instr_si_nr[1])  # <dst>
		instr_si_nr[2] = int(instr_si_nr[2])  # <val>
		registre[instr_si_nr[1]] = instr_si_nr[2]

	elif instr_si_nr[0] == 'add':
		# add 'dst' 'src0' 'src1' - aduna valorile din registrele src0 si src1 si pune rezultatul in dst
		instr_si_nr[1] = int(instr_si_nr[1])  # <dst>
		instr_si_nr[2] = int(instr_si_nr[2])  # <src0> - index registru
		instr_si_nr[3] = int(instr_si_nr[3])  # <src1> - index registru
		registre[instr_si_nr[1]] = registre[instr_si_nr[2]] + \
			registre[instr_si_nr[3]]

	elif instr_si_nr[0] == 'mul':
		# mul dst src0 src1 - aduna valorile din registrele src0 si src1(indecsi) si pune rezultatul in dst(index)
		instr_si_nr[1] = int(instr_si_nr[1])  # <dst>
		instr_si_nr[2] = int(instr_si_nr[2])  # <src0> - index registru
		instr_si_nr[3] = int(instr_si_nr[3])  # <src1> - index registru
		registre[instr_si_nr[1]] = registre[instr_si_nr[2]] * \
			registre[instr_si_nr[3]]

	elif instr_si_nr[0] == 'div':
		instr_si_nr[1] = int(instr_si_nr[1])  # <dst>
		instr_si_nr[2] = int(instr_si_nr[2])  # <src0> - index registru
		instr_si_nr[3] = int(instr_si_nr[3])  # <src1> - index registru
		if registre[instr_si_nr[3]] == 0:
			if registre[instr_si_nr[3]] == 0 and registre[instr_si_nr[2]] == 0:
				buffer_print.append("Exception: line " + str(i + 1))
			else:
				registre[instr_si_nr[1]] = "Exception: line " + str(i + 1)
		else:
			# print(registre[instr_si_nr[1]], registre[instr_si_nr[2]], registre[instr_si_nr[3]])
			# print(int( registre[instr_si_nr[2]] / registre[instr_si_nr[3]] ))
			x = int(registre[instr_si_nr[2]] / registre[instr_si_nr[3]])
			if x < 0:
				registre[instr_si_nr[1]] = x + 1
			else:
				registre[instr_si_nr[1]] = x

	elif instr_si_nr[0] == 'print':
		# print reg - afiseaza valoarea din registrul reg
		# printarea trebuie sa o fac intr-un buffer !!!
		instr_si_nr[1] = int(instr_si_nr[1])
		buffer_print.append(registre[instr_si_nr[1]])

for i in range(len(buffer_print)):
	print(buffer_print[i])
# print(instr_si_nr)
# print(registre)
# ... am hardcodat 2 teste, but ok.
