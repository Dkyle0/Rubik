# ####### The cube on the facelet level is described by positions of the colored stickers. #############################
# #################### Куб описывается с помощью позиций разноцветных наклеек. #########################################

from defs import cornerFacelet, edgeFacelet, cornerColor, edgeColor
from enums import Color, Corner, Edge
from cubie import CubieCube


class FaceCube:
	"""
	Represent a cube on the facelet level with 54 colored facelets.
	Куб представляет из себя 54 разноцветные наклейки.
	"""
	def __init__(self):
		self.f = []
		for i in range(9):
			self.f.append(Color.U)
		for i in range(9):
			self.f.append(Color.R)
		for i in range(9):
			self.f.append(Color.F)
		for i in range(9):
			self.f.append(Color.D)
		for i in range(9):
			self.f.append(Color.L)
		for i in range(9):
			self.f.append(Color.B)

	def from_string(self, s):
		"""
		Construct a facelet cube from a string. See class Facelet(IntEnum) in enums.py for string format.
		Строит стороны куба из строки. С форматом строки можете ознакомиться в class Facelet(IntEnum).
		"""
		for i in range(54):
			if s[i] == 'U':
				self.f[i] = Color.U
			elif s[i] == 'R':
				self.f[i] = Color.R
			elif s[i] == 'F':
				self.f[i] = Color.F
			elif s[i] == 'D':
				self.f[i] = Color.D
			elif s[i] == 'L':
				self.f[i] = Color.L
			elif s[i] == 'B':
				self.f[i] = Color.B

	def to_cubie_cube(self):
		"""
		Return a cubie representation of the facelet cube.
		Возвращает представление куба class CubieCube.
		"""
		cc = CubieCube()
		"""
		Invalidate corner and edge permutation.
		Установка неправильных перестановок ребер и углов.
		"""
		cc.cp = [-1] * 8
		cc.ep = [-1] * 12
		for i in Corner:
			"""
			Facelets of corner at position i.
			Поверхности углов в i позиции.
			"""
			fac = cornerFacelet[i]
			for ori in range(3):
				if self.f[fac[ori]] == Color.U or self.f[fac[ori]] == Color.D:
					break
			"""
			colors which identify the corner at position i.
			Цвета, которые получилось установить для позиции i.
			"""
			col1 = self.f[fac[(ori + 1) % 3]]
			col2 = self.f[fac[(ori + 2) % 3]]
			for j in Corner:
				"""
				Colors of corner j.
				Цвета j-го угла.
				"""
				col = cornerColor[j]  # colors of corner j
				if col1 == col[1] and col2 == col[2]:
					"""
					We have corner j in corner position i.
					Мы смогли установить, что i-му углу на нашем кубике соответствует j-ый угол из списка cornerColor.
					Это j-ый угол в уже собранном кубике в списке cornerFacelet.
					"""
					cc.cp[i] = j
					cc.co[i] = ori
					break

		"""
		Таким же способом находим соответствие i-го ребра на нашем кубике соответствующему j-му ребру в уже собранном кубике.
		"""
		for i in Edge:
			for j in Edge:
				if self.f[edgeFacelet[i][0]] == edgeColor[j][0] and \
						self.f[edgeFacelet[i][1]] == edgeColor[j][1]:
					cc.ep[i] = j
					cc.eo[i] = 0
					break
				if self.f[edgeFacelet[i][0]] == edgeColor[j][1] and \
						self.f[edgeFacelet[i][1]] == edgeColor[j][0]:
					cc.ep[i] = j
					cc.eo[i] = 1
					break
		return cc
