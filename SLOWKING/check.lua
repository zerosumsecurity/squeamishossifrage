#!/usr/bin/lua

--
-- flag checker
--

function fa( x )
  return ((  x*x ~ 3141592653))
end

function fb( x )
  return ((  3*x + 1732050808))
end

function fc( x )
  return (( x>>3 | 2236067975))
end

function fd( x )
  return ((  7*x - 2645751308))
end


function check( input )

  local verify = {4125536637,631702732,2333190013,530118337,4144883596,2748845596,1851309964,3375630137,4104857964}

  local t = {}
  local f = {}
  local fl = {}
  local len = string.len(input)
  local res = true

  print("Let me check that flag...")

  if len ~= 36 then
  	print("Nope...")
  	return
  end


  fl[1] = fa
  fl[2] = fb
  fl[3] = fc
  fl[4] = fd

  for i = 0,8 do
  	t[i+1] = 16777216*string.byte(input, 4*i+1)
  	t[i+1] = t[i+1] + 65536*string.byte(input, 4*i+2)
  	t[i+1] = t[i+1] + 256*string.byte(input, 4*i+3)
    t[i+1] = t[i+1] + string.byte(input, 4*i+4)
    f[i+1] = t[i+1]
  end

  for j = 1,13371337 do
  	for i = 1, #t do
  		local fi = fl[(t[i] % 4)+1]
  		t[i] = fi(t[i]) % 4294967296
  	end
  end

  for i = 1, #t do
    t[i] = (t[i] + f[i]) % 4294967296
    if(t[i] ~= verify[i]) then
      res = false
    end
  end

  if res == true then
  	print("That flag just might be correct...")
  else		
  	print("Nope...")
  end

end

--
-- Main program 
--

io.write("Please enter the flag: ")
io.flush()
pwd = io.read()
check( pwd ) 
