from typing import Union,List
import random
import math

def ones() -> "vector": return vector(1,1,1)

def zeros() -> "vector": return vector(0,0,0)

def fill(value) -> "vector": return vector(value,value,value)

def vec(x: Union[int,float],y: Union[int,float],z: Union[int,float]): return vector(x,y,z)

def rand(seed: Union[None,int] = None) -> "vector":
    if seed is not None: random.seed(seed)
    return vector(random.random(),random.random(),random.random())

class vector:
    def __init__(self,x: Union[int,float],y: Union[int,float],z: Union[int,float]) -> Union[None,str]:
        if self.__check__(x,y,z):
            self.__x = x
            self.__y = y
            self.__z = z
        else: raise TypeError(f"x, y, and z must be an int or a float!")

    def __check__(self,x,y,z):
        if isinstance(x,(int,float)) and isinstance(y,(int,float)) and isinstance(z,(int,float)): return True
        return False

    def __repr__(self) -> str: return f"vector: ({self.__x} {self.__y} {self.__z})"

    def __sqrt__(self,value):
        if value <= 0: raise ValueError("input must be a positive number")
        guess = value / 2
        tolerance = 1e-10
        while True:
            new_guess = (guess + value / guess) / 2
            if abs(new_guess - guess) < tolerance: break
            guess = new_guess
        return guess

    def __getitem__(self,index) -> Union[None,str]:
        if index == "x": return self.__x
        elif index == "y": return self.__y
        elif index == "z": return self.__z
        raise IndexError(f"invalid index, expected from x, y, and z but got {index}!")

    def __setitem__(self,index,value) -> Union[int,float,str]:
        if not isinstance(value,(int,float)):
            raise ValueError(f"given value must be an interger or a float not {value}")
        if index == "x": self.__x = value
        elif index == "y": self.__y = value
        elif index == "z": self.__z = value
        raise IndexError(f"invalid index, expected from x, y, and z but got {index}")

    @property
    def x(self) -> Union[int,float]: return self.__x

    @property
    def y(self) -> Union[int,float]: return self.__y

    @property
    def z(self) -> Union[int,float]: return self.__z

    def __add__(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(self.__x + other,self.__y + other,self.__z + other)
        elif isinstance(other,vector): return vector(self.__x + other.__x,self.__y + other.__y,self.__z + other.__z)
        raise TypeError(f"unsupported operand type for +: `{type(other).__name__}` and `vector`")

    def __radd__(self,other: Union[int,float]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(other + self.__x,other + self.__y,other + self.__z)
        raise TypeError(f"unsupported operand type +: `{type(other).__name__}` and `vector`")

    def __sub__(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(self.__x - other,self.__y - other, self.__z - other)
        elif isinstance(other,vector): return vector(self.__x - other.__x,self.__y - other.__y,self.__z - other.__z)
        raise TypeError(f"unsupported operand type for -: `{type(other).__name__}` and `vector`")

    def __rsub__(self,other: Union[int,float]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(other - self.__x,other - self.__y,other - self.__z)
        raise TypeError(f"unsupported operand type for -: `{type(other).__name__}` and `vector`")

    def __mul__(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(self.__x * other,self.__y * other,self.__z * other)
        elif isinstance(other,vector): return vector(self.__x * other.__x,self.__y * other.__y,self.__z * other.__z)
        raise TypeError(f"unsupported operand type for *: `{type(other).__name__}` and `vector`")

    def __rmul__(self,other: Union[int,float]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(other * self.__x,other * self.__y,other * self.__z)
        raise TypeError(f"unsupported operand type for *: `{type(other).__name__}` and `vector`")

    def __matmul__(self,other: "vector") -> Union[str,"vector"]:
        if isinstance(other,vector): return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z
        raise TypeError(f"unsupported operand type for @: `{type(other).__name__}` and `vector`")

    def __truediv__(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(self.__x / other,self.__y / other,self.__z / other)
        elif isinstance(other,vector): return vector(self.__x / other.__x,self.__y / other.__y, self.__x / other.__y)
        raise TypeError(f"unsupported operand type for /: `{type(other).__name__}` and `vector`")

    def __rtruediv__(self,other: Union[int,float]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(other / self.__x,other / self.__y,other / self.__z)
        raise TypeError(f"unsupported operand type for /: `{type(other).__name__}` and `vector`")

    def __floordiv__(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(self.__x // other,self.__y // other,self.__z // other)
        elif isinstance(other,vector): return vector(self.__x // other.__x,self.__y // other.__y,self.__z // other.__z)
        raise TypeError(f"unsupported operand type for //: `{type(other).__name__}` and `vector`")

    def __rfloordiv__(self,other: Union[int,float]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(other // self.__x,other // self.__y,other // self.__z)
        raise TypeError(f"unsupported operand type for //: `{type(other).__name__}` and `vector`")

    def __pos__(self) -> "vector": return vector(self.__x,self.__y,self.__z)

    def __neg__(self) -> "vector": return vector(-self.__x,-self.__y,-self.__z)

    def __mod__(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(self.__x % other,self.__y % other,self.__z % other)
        elif isinstance(other,vector): return vector(self.__x % other.__x,self.__y % other.__y,self.__z % other.__z)
        raise TypeError(f"unsupported opernad type for %: `{type(other).__name__}` and `vector`")

    def __rmod__(self,other: Union[int,float]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(other % self.__x,other % self.__y,other % self.__z)
        raise TypeError(f"unsupported operand type for %: `{type(other).__name__}` and `vector`")

    def __pow__(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(self.__x ** other,self.__y ** other,self.__z ** other)
        elif isinstance(other,vector): return vector(self.__x ** other.__x,self.__y ** other.__y,self.__z ** other.__z)
        raise TypeError(f"unsupported operand type for **: `{type(other).__name__} and `vector`")

    def __rpow__(self,other: Union[int,float]) -> Union[str,"vector"]:
        if isinstance(other,(int,float)): return vector(other ** self.__x,other ** self.__y,other ** self.__z)
        raise TypeError(f"unsupported operand typr for **: `{type(other).__name__}` and `vector`")

    def __eq__(self,other: "vector") -> Union[str,bool]:
        if isinstance(other,vector): return self.norm() == other.norm()
        raise TypeError(f"unsupported operand type for ==: `{type(other).__name__}` and `vector`")

    def __ne__(self,other: "vector") -> Union[str,bool]:
        if isinstance(other,vector): return self.norm() != other.norm()
        raise TypeError(f"unsupported operand type for !=: `{type(other).__name__}` and `vector`")

    def __gt__(self,other: "vector") -> Union[str,bool]:
        if isinstance(other,vector): return self.norm() > other.norm()
        raise TypeError(f"unsupported operand type for >: `{type(other).__name__}` and `vector`")

    def __ge__(self,other: "vector") -> Union[str,bool]:
        if isinstance(other,vector): return self.norm() >= other.norm()
        raise TypeError(f"unsupported operand type for >=: `{type(other).__name__}` and `vector`")

    def __lt__(self,other: "vector") -> Union[str,bool]:
        if isinstance(other,vector): return self.norm() < other.norm()
        raise TypeError(f"unsupported operand type for <: `{type(other).__name__}` and `vector`")

    def __le__(self,other: "vector") -> Union[str,bool]:
        if isinstance(other,vector): return self.norm() <= other.norm()
        raise TypeError(f"unsupported operand type for <=: `{type(other).__name__}` and `vector`")

    def __and__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(self.__x & other,self.__y & other,self.__z & other)
        elif isinstance(other,vector): return vector(self.__x & other.__x,self.__y & other.__y,self.__z & other.__z)
        raise TypeError(f"unsupported operand type for &: `{type(other).__name__}` and `vector`")

    def __rand__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(other & self.__x,other & self.__y,other & self.__y)
        raise TypeError(f"unsupported operand type for &: `{type(other).__name__}` and `vector`")

    def __or__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(self.__x | other,self.__y | other,self.__z | other)
        elif isinstance(other,vector): return vector(self.__x | other.__x,self.__y | other.__y,self.__z | other.__z)
        raise TypeError(f"unsupported operand type for |: `{type(other).__name__}` and `vector`")

    def __ror__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(other | self.__x,other | self.__y,other | self.__z)
        raise TypeError(f"unsupported operand type for |: `{type(other).__name__}` and `vector`")

    def __xor__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(self.__x ^ other,self.__y ^ other,self.__z ^ other)
        elif isinstance(other,vector): return vector(self.__x ^ other.__x,self.__y ^ other.__y,self.__z ^ other.__z)
        raise TypeError(f"unsupported operand type for ^: `{type(other).__name__}` and `vector`")

    def __rxor__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(other ^ self.__x,other ^ self.__y,other ^ self.__z)
        raise TypeError(f"unsupported operand type for ^: `{type(other).__name__}` and `vector`")

    def __invert__(self) -> int: return vector(~self.__x,~self.__y,~self.__z)

    def __lshift__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(self.__x << other,self.__y << other,self.__z << other)
        elif isinstance(other,vector): return vector(self.__x << other.__x,self.__y << other.__y,self.__z << other.__z)
        raise TypeError(f"Unsupported operand type for <<: '{type(other).__name__}' and 'vector'")

    def __rlshift__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(other << self.__x,other << self.__y,other << self.__z)
        raise TypeError(f"Unsupported operand type for <<: '{type(other).__name__}' and 'vector'")

    def __rshift__(self,other: Union[int,"vector"]) -> Union[str,"vector"]:
        if isinstance(other,int): return vector(self.__x >> other,self.__y >> other,self.__z >> other)
        elif isinstance(other,vector): return vector(self.__x >> other.__x,self.__y >> other.__y,self.__z >> other.__z)
        raise TypeError(f"Unsupported operand type for >>: '{type(other).__name__}' and 'vector'")

    def __rrshift__(self,other: Union[int,"int"]) -> Union[str,"int"]:
        if isinstance(other,int): return vector(other >> self.__x,other >> self.__y,other >> self.__z)
        raise TypeError(f"Unsupported operand type for >>: '{type(other).__name__}' and 'vector'")

    def add(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return self + other

    def radd(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return  other + self

    def sub(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return self - other

    def rsub(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return other - self

    def mul(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return self * other

    def rmul(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return other * self

    def truediv(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return self / other

    def rtruediv(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return other / self

    def floordiv(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return self // other

    def rfloordiv(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return other // self

    def pos(self) -> "vector": return vector(+self.__x,+self.__y,+self.__z)

    def neg(self) -> "vector": return vector(-self.__x,-self.__y,-self.__z)

    def mod(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return self % other

    def rmod(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return other % self

    def pow(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return self ** other

    def rpow(self,other: Union[int,float,"vector"]) -> Union[str,"vector"]: return other ** self

    def matmul(self,other: "vector") -> Union[str,"vector"]: return self @ other

    def eq(self,other: "vector") -> Union[str,bool]: return self == other

    def ne(self,other: "vector") -> Union[str,bool]: return self != other

    def gt(self,other: "vector") -> Union[str,bool]: return self > other

    def ge(self,other: "vector") -> Union[str,bool]: return self >= other

    def lt(self,other: "vector") -> Union[str,bool]: return self < other

    def le(self,other: "vector") -> Union[str,bool]: return self <= other

    def AND(self,other: Union[int,"vector"]) -> Union[str,int]: return self & other

    def RAND(self,other: Union[int,"vector"]) -> Union[str,int]: return other & self

    def OR(self,other: Union[int,"vector"]) -> Union[str,int]: return self | other

    def ROR(self,other: Union[int,"vector"]) -> Union[str,int]: return other | self

    def XOR(self,other: Union[int,"vector"]) -> Union[str,int]: return self ^ other

    def RXOR(self,other: Union[int,"vector"]) -> Union[str,int]: return other ^ self

    def INVERT(self) -> Union[str,int]: return ~self

    def lshift(self,other: Union[str,int]) -> Union[str,int]: return self << other

    def rlshift(self,other: Union[str,int]) -> Union[str,int]: return other << self

    def rshift(self,other:Union[str,int]) -> Union[str,int]: return self >> other

    def rrshift(self,other: Union[str,int]) -> Union[str,int]: return other >> self

    def scale(self,value: Union[int,float,"vector"]) -> Union[str,"vector"]: return vector(self.__x * value,self.__y * value,self.__z * value)

    def norm(self) -> Union[int,float]: return self.__sqrt__(self.__x ** 2 + self.__y ** 2 + self.__z ** 2)

    def dot(self,other: "vector") -> Union[int,float,str]:
        if isinstance(other,vector): return self @ other
        raise TypeError(f"can't find dot product between two different datatype `{type(other).__name__}` with `vector`")

    def cross(self,other: "vector") -> Union[str,"vector"]:
        if isinstance(other, vector):
            X = self.__y * other.__z - self.__z * other.__y
            Y = self.__z * other.__x - self.__x * other.__z
            Z = self.__x * other.__y - self.__y * other.__x
            return vector(X,Y,Z)
        raise TypeError(f"can't find cross product between two different datatypes `{type(other).__name__}` with `vector`")

    def angle(self,other: "vector") -> Union[int,float]: return math.acos(self.dot(other) / (self.norm() * other.norm()))

    def octant(self) -> int:
        if self.__x >= 0 and self.__y >= 0 and self.__z >= 0: return 1
        elif self.__x < 0 and self.__y >= 0 and self.__z >= 0: return 2
        elif self.__x < 0 and self.__y < 0 and self.__z >= 0: return 3
        elif self.__x >= 0 and self.__y < 0 and self.__z >= 0: return 4
        elif self.__x >= 0 and self.__y >= 0 and self.__z < 0: return 5
        elif self.__x < 0 and self.__y >= 0 and self.__z < 0: return 6
        elif self.__x < 0 and self.__y < 0 and self.__z < 0: return 7
        elif self.__x >= 0 and self.__y < 0 and self.__z < 0: return 8
        raise ValueError("Unexpected conditions in determining octant.")
    
    def unit(self) -> Union[int,float]: return self / self.norm()

    def proj(self,onto: "vector") -> Union[int,float]: return (self @ onto) / onto.norm()

    def copy(self) -> "vector": return vector(self.__x,self.__y,self.__z)

    def is_orthogonal(self,other: "vector") -> Union[str,bool]: return self.dot(other) == 0

    def is_parallel(self,other: "vector") -> Union[str,bool]: return self.angle(other) == 0

    def to_list(self) -> List[Union[int,float]]: return [self.__x,self.__y,self.__z]

    def dir_cosine(self) -> List[Union[int,float]]:
        norm = self.norm()
        return [self.__x / norm,self.__y / norm,self.__z / norm]
