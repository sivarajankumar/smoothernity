local env = {require = require}

local run = function(code, name)
    if name then
        f = io.open(name, 'w')
        f:write(code)
        f:close()
    end
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
assert(run([[
    require 'luacov'
    x = 1
    y = 2
]], 'untrusted_string.lua'))
assert(runfile('untrusted_file.lua'))
