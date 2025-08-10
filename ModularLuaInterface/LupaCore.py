import lupa
from lupa.lua54 import LuaRuntime


print(f"Using {lupa.LuaRuntime().lua_implementation} (compiled with {lupa.LUA_VERSION})")



class Lua:
    def __init__(self):
        self.runtime = LuaRuntime(unpack_returned_tuples=True)

    def eval(self,content):
        return self.runtime.eval(content)
    
