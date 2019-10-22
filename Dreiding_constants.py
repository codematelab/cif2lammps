
Dreiding_atom_parameters = {
	#Atom   R1     theta    R0      D0      phi  S
	"H_":  (0.330, 180.0  , 3.195 , 0.0152, 0.0, 12.382),
	"B_3": (0.880, 109.471, 4.02  , 0.095 , 0.0, 14.23),
	"B_2": (0.790, 120.0  , 4.02  , 0.095 , 0.0, 14.23),
	"C_3": (0.770, 109.471, 3.8983, 0.0951, 0.0, 14.034),
	"C_R": (0.700, 120.0  , 3.8983, 0.0951, 0.0, 14.034),
	"C_2": (0.670, 120.0  , 3.8983, 0.0951, 0.0, 14.034),
	"C_1": (0.602, 180.0  , 3.8983, 0.0951, 0.0, 14.034),
	"N_3": (0.702, 106.7  , 3.6621, 0.0774, 0.0, 13.843),
	"N_R": (0.650, 120.0  , 3.6621, 0.0774, 0.0, 13.843),
	"N_2": (0.615, 120.0  , 3.6621, 0.0744, 0.0, 13.843),
	"N_1": (0.556, 180.0  , 3.6621, 0.0744, 0.0, 13.843),
	"O_3": (0.660, 104.51 , 3.4046, 0.0957, 0.0, 13.483),
	"O_R": (0.660, 120.0  , 3.4046, 0.0957, 0.0, 13.483),
	"O_2": (0.560, 120.0  , 3.4046, 0.0957, 0.0, 13.483),
	"O_1": (0.528, 180.0  , 3.4046, 0.0957, 0.0, 13.483),
	"F_":  (0.611, 180.0  , 3.4720, 0.0725, 0.0, 14.444),
	"Al3": (1.047, 109.471, 4.39  , 0.31  , 0.0, 12.0),
	"Si3": (0.937, 109.471, 4.27  , 0.31  , 0.0, 12.0),
	"P_3": (0.890, 93.3   , 4.15  , 0.32  , 0.0, 12.0),
	"S_3": (1.040, 92.1   , 4.03  , 0.344 , 0.0, 12.0),
	"S_R": (1.040, 92.1   , 4.03  , 0.344 , 0.0, 12.0), # same as S_3, but R is more useful
	"Cl_": (0.997, 180.0  , 3.9503, 0.2833, 0.0, 13.861),
	"Ga3": (1.210, 109.471, 4.39  , 0.4   , 0.0, 12.0),
	"Ge3": (1.210, 109.471, 4.27  , 0.4   , 0.0, 12.0),
	"As3": (1.210, 92.1   , 4.15  , 0.41  , 0.0, 12.0),
	"Se3": (1.210, 90.6   , 4.03  , 0.43  , 0.0, 12.0),
	"Br_": (1.167, 180.0  , 3.95  , 0.37  , 0.0, 12.0),
	"In3": (1.390, 109.471, 4.59  , 0.55  , 0.0, 12.0),
	"Sn3": (1.373, 109.471, 4.47  , 0.55  , 0.0, 12.0),
	"Sb3": (1.432, 91.6   , 4.35  , 0.55  , 0.0, 12.0),
	"Te3": (1.280, 90.3   , 4.23  , 0.57  , 0.0, 12.0),
	"I_":  (1.360, 180.0  , 4.15  , 0.51  , 0.0, 12.0),
	"Na":  (1.860, 90.0   , 3.144 , 0.5   , 0.0, 12.0),
	"Ca":  (1.940, 90.0   , 3.472 , 0.05  , 0.0, 12.0),
	"Fe":  (1.285, 90.0   , 4.54  , 0.055 , 0.0, 12.0),
	"Zn":  (1.330, 109.471, 4.54  , 0.055 , 0.0, 12.0),
	"Cu":  (1.302, 90.0   , 4.54  , 0.055 , 0.0, 12.0), # R1 taken from UFF, the rest are just a copy of DREIDING Zn
	"Zr":  (1.564, 109.471, 4.54  , 0.055 , 0.0, 12.0), # R1 taken from UFF, the rest are just a copy of DREIDING Zn
	"Cr":  (1.345, 90.0   , 4.54  , 0.055 , 0.0, 12.0), # R1 taken from UFF, the rest are just a copy of DREIDING Zn
	# added for easier IDs
	"O_2_M": (0.560, 120.0  , 3.4046, 0.0957, 0.0, 13.483),
	"O_3_M": (0.660, 104.51 , 3.4046, 0.0957, 0.0, 13.483)
}

Dreiding_bond_orders_0 = {
	("Cu", "Cu")    : 0.25,
	("Zn", "O_2_M") : 0.50,
	("Zr", "O_2_M") : 0.50,
	("Cr", "O_2_M") : 0.50,
	("Zn", "O_3_M") : 0.50,
	("Zr", "O_3_M") : 0.50,
	("Cr", "O_3_M") : 0.50,
	'S': 1.00,
	'A': 1.50,
	'D': 2.00,
	'T': 3.00
}