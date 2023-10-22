# ###################################### some definitions and constants ################################################
# ##################################### некоторые определения и константы ##############################################

from enums import Facelet as Fc, Color as Cl

"""
Map the corner positions to facelet positions.
Карта соответствия позиций углов и сторон.
"""
cornerFacelet = [[Fc.U9, Fc.R1, Fc.F3], [Fc.U7, Fc.F1, Fc.L3], [Fc.U1, Fc.L1, Fc.B3], [Fc.U3, Fc.B1, Fc.R3],
				 [Fc.D3, Fc.F9, Fc.R7], [Fc.D1, Fc.L9, Fc.F7], [Fc.D7, Fc.B9, Fc.L7], [Fc.D9, Fc.R9, Fc.B7]
				 ]

"""
Map the edge positions to facelet positions.
Карта соответствия позиций ребер и сторон.
"""
edgeFacelet = [[Fc.U6, Fc.R2], [Fc.U8, Fc.F2], [Fc.U4, Fc.L2], [Fc.U2, Fc.B2], [Fc.D6, Fc.R8], [Fc.D2, Fc.F8],
			   [Fc.D4, Fc.L8], [Fc.D8, Fc.B8], [Fc.F6, Fc.R4], [Fc.F4, Fc.L6], [Fc.B6, Fc.L4], [Fc.B4, Fc.R6]
			   ]

"""
Map the corner positions to facelet colors.
Карта соответствия позиций углов и цветов сторон.
"""
cornerColor = [[Cl.U, Cl.R, Cl.F], [Cl.U, Cl.F, Cl.L], [Cl.U, Cl.L, Cl.B], [Cl.U, Cl.B, Cl.R],
			   [Cl.D, Cl.F, Cl.R], [Cl.D, Cl.L, Cl.F], [Cl.D, Cl.B, Cl.L], [Cl.D, Cl.R, Cl.B]
			   ]

"""
Map the edge positions to facelet colors.
Карта соответствия позиций ребер и цветов сторон.
"""
edgeColor = [[Cl.U, Cl.R], [Cl.U, Cl.F], [Cl.U, Cl.L], [Cl.U, Cl.B], [Cl.D, Cl.R], [Cl.D, Cl.F],
			 [Cl.D, Cl.L], [Cl.D, Cl.B], [Cl.F, Cl.R], [Cl.F, Cl.L], [Cl.B, Cl.L], [Cl.B, Cl.R]
			 ]

# ###################################### some "constants" ##############################################################
# ################################### некоторые "постоянные" ###########################################################
N_PERM_4 = 24
N_CHOOSE_8_4 = 70

"""
number of possible face moves
число возможных ходов сторон
"""
N_MOVE = 18

"""
3^7 possible corner orientations in phase 1
3^7 возможных ориенаций углов на фазе 1
"""
N_TWIST = 2187

"""
2^11 possible edge orientations in phase 1
2^11 возможных ориентаций на фазе 1
"""
N_FLIP = 2048

"""
12*11*10*9 possible positions of the FR, FL, BL, BR edges in phase 1
12*11*10*9 возможных положений ребер FR, FL, BL, BR на фазе 1
"""
N_SLICE_SORTED = 11880

"""
we ignore the permutation of FR, FL, BL, BR in phase 1
мы игнорируем перестановку FR, FL, BL, BR на фазе 1
"""
N_SLICE = N_SLICE_SORTED // N_PERM_4

"""
number of equivalence classes for combined flip+slice concerning symmetry group D4h
количество классов эквивалентности для комбинированного flip + slice относительно группы симметрии D4h
"""
N_FLIPSLICE_CLASS = 64430

"""
number of different positions of the edges UR, UF, UL and UB in phase 2
количество различных положений ребер UR, UF, UL и UB в фазе 2
"""
N_U_EDGES_PHASE2 = 1680

"""
8! corner permutations in phase 2
8! угловых перестановок в фазе 2
"""
N_CORNERS = 40320

"""
number of equivalence classes concerning symmetry group D4h
количество классов эквивалентности относительно группы симметрий D4h
"""
N_CORNERS_CLASS = 2768

"""
8! permutations of the edges in the U-face and D-face in phase 2
8! перестановки ребер в U-грани и D-грани в фазе 2
"""
N_UD_EDGES = 40320

"""
number of cube symmetries of full group Oh
число симметрий куба полной группы Oh
"""
N_SYM = 48

"""
Number of symmetries of subgroup D4h
Число симметрий подгруппы D4h
"""
N_SYM_D4h = 16
########################################################################################################################
