class Matrix(object):

  def __init__(self, rows):
    self.rows = rows

  def __add__(self, other):
    return Matrix([(a + b) for a, b in zip(self.rows, other.rows)])

  def __repr__(self):
    return f"{[row for row in self.rows]}\n"
