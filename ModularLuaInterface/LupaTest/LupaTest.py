import lupa
from lupa.lua54 import LuaRuntime

print(f"Using {lupa.LuaRuntime().lua_implementation} (compiled with {lupa.LUA_VERSION})")


lua = LuaRuntime(unpack_returned_tuples=True)


print(lua.eval('1+1'))


lua_func = lua.eval('function(f, n) return f(n) end')

with open("luaTest.lua") as file:
    contents = file.read()


func = lua.eval(contents)

print(dir(func))

print(func(4))

