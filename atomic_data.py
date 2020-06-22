metals = set(['Ac','Ag','Al','Am','Au','Ba','Be','Bi',
			  'Bk','Ca','Cd','Ce','Cf','Cm','Co','Cr',
			  'Cs','Cu','Dy','Er','Es','Eu','Fe','Fm',
			  'Fr','Ga','Gd','Hf','Hg','Ho','In','Ir',
			  'K','La','Li','Lr','Lu','Md','Mg','Mn',
			  'Mo','Na','Nb','Nd','Ni','No','Np','Os',
			  'Pa','Pb','Pd','Pm','Pr','Pt','Pu','Ra',
			  'Rb','Re','Rh','Ru','Sc','Sm','Sn','Sr',
			  'Ta','Tb','Tc','Th','Ti','Tl','Tm','U',
			  'V','W','Y','Yb','Zn','Zr'])

mass_key = {
"X" : 0.000001,
"NA": 0.000001,
"H" : 1.00794,
"He": 4.002602,
"Li": 6.941,
"Be": 9.012182,
"B" : 10.811,
"C" : 12.0107,
"N" : 14.0067,
"O" : 15.9994,
"F" : 18.9984032,
"Ne": 20.1797,
"Na": 22.98976928,
"Mg": 24.3050,
"Al": 26.9815386,
"Si": 28.0855,
"P" : 30.973762,
"S" : 32.065,
"Cl": 35.453,
"Ar": 39.948,
"K" : 39.0983,
"Ca": 40.078,
"Sc": 44.955912,
"Ti": 47.867,
"V" : 50.9415,
"Cr": 51.9961,
"Mn": 54.938045,
"Fe": 55.845,
"Co": 58.933195,
"Ni": 58.6934,
"Cu": 63.546,
"Zn": 65.38,
"Ga": 69.723,
"Ge": 72.64,
"As": 74.92160,
"Se": 78.96,
"Br": 79.904,
"Kr": 83.798,
"Rb": 85.4678,
"Sr": 87.62,
"Y" : 88.90585,
"Zr": 91.224,
"Nb": 92.90638,
"Mo": 95.96,
"Tc": 98,
"Ru": 101.07,
"Rh": 102.90550,
"Pd": 106.42,
"Ag": 107.8682,
"Cd": 112.411,
"In": 114.818,
"Sn": 118.710,
"Sb": 121.760,
"Te": 127.60,
"I" : 126.90447,
"Xe": 131.293,
"Cs": 132.9054519,
"Ba": 137.327,
"La": 138.90547,
"Ce": 140.116,
"Pr": 140.90765,
"Nd": 144.242,
"Pm": 145,
"Sm": 150.36,
"Eu": 151.964,
"Gd": 157.25,
"Tb": 158.92535,
"Dy": 162.500,
"Ho": 164.93032,
"Er": 167.259,
"Tm": 168.93421,
"Yb": 173.054,
"Lu": 174.9668,
"Hf": 178.49,
"Ta": 180.94788,
"W" : 183.84,
"Re": 186.207,
"Os": 190.23,
"Ir": 192.217,
"Pt": 195.084,
"Au": 196.966569,
"Hg": 200.59,
"Tl": 204.3833,
"Pb": 207.2,
"Bi": 208.98040,
"Po": 209,
"At": 210,
"Rn": 222,
"Fr": 223,
"Ra": 226,
"Ac": 227,
"Th": 232.03806,
"Pa": 231.03588,
"U" : 238.02891,
"Np": 237,
"Pu": 244,
"Am": 243,
"Cm": 247,
"Bk": 247,
"Cf": 251,
"Es": 252,
"Fm": 257,
"Md": 258,
"No": 259,
"Lr": 262,
"Rf": 265,
"Db": 268,
"Sg": 271,
"Bh": 272,
"Hs": 270,
"Mt": 276,
"Ds": 281,
"Rg": 280,
"Cn": 285,
"Uut": 284,
"Uuq": 289,
"Uup": 288,
"Uuh": 293,
"Uuo": 294
}