

function(T,f)
    x = 0
    y = 0
    i = 0
    for freq in python.iter(f) do
        i= i+1
        
    
        rate = 1/110
        t = math.fmod(T,rate)/(rate)
        --return t,math.cos(math.rad(T*440*360))

        --return t*math.sin(math.rad(T*440*360*1.1)),t*math.cos(math.rad(T*440*360))
        --return math.sin(math.rad(T*440*360*1.1)),math.cos(math.rad(T*440*360))
        x = x + math.sin(math.rad(T*freq*360*1)+i)
        y = y + math.cos(math.rad(T*freq*360)+i)
        --return math.sin(math.rad(T*freq*360*1.1)),math.cos(math.rad(T*freq*360))
    end
    return x,y
    --return math.sin(math.rad(T*1*360*1.1)),math.cos(math.rad(T*1*360))
end

--[[
function(T, p)
  local freq1 = 220 -- First frequency
  local freq2 = 440        -- Second frequency

  -- Generate the first triangle wave
  local phase1 = (T * freq1) % 1
  local value1
  if phase1 < 0.5 then
    value1 = 4 * phase1 - 1
  else
    value1 = 3 - 4 * phase1
  end

  -- Generate the second triangle wave
  local phase2 = (T * freq2) % 1
  local value2
  if phase2 < 0.5 then
    value2 = 4 * phase2 - 1
  else
    value2 = 3 - 4 * phase2
  end
  
  -- Return the two generated values.
  -- The 'p' parameter from the original function is unused but maintained
  -- to match the function signature.
  return value1, value2
end
]]--