local env = {myrequire = require}
local index = 0

local run = function(code)
    index = index + 1
    local name = string.format('untrusted_string%i.lua', index)
    if name then
        f = io.open(name, 'w')
        f:write(code)
        f:close()
    end
    code = string.format("myrequire 'luacov'\n%s", code)
    print(name)
    print(code)
    local fn, msg = load(code, name, 't', env)
    if not fn then
        return nil, message
    end
    return pcall(fn)
end

local runfile = function(name)
    local fn, msg = loadfile(name, 't', env)
    if not fn then
        return nil, message
    end
    return pcall(fn)
end

-- test
assert(not run [[print(debug.getinfo(1))]])
assert(env[x] == nil)
assert(run [[x = 1]])
assert(env.x == 1)
assert(run [[
x = 1
y = 2
]])
assert(runfile('untrusted_file.lua'))
