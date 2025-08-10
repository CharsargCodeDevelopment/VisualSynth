def ActivateCore(core = "lupa"):
    if core == "lupa":
        import ModularLuaInterface.LupaCore

        
        ModularLuaInterface.Core = ModularLuaInterface.LupaCore
