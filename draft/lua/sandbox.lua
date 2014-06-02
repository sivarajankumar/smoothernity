local env = {myrequire=require, myprint=print}
local index = 0

local run = function(code)
    code = string.format("myrequire 'luacov'\n%s", code)
    index = index + 1
    local name = string.format('untrusted_string%i.lua', index)
    f = io.open(name, 'w')
    f:write(code)
    f:close()
    local fn, msg = loadfile(name, 't', env)
    if not fn then
        return nil, msg
    end
    return pcall(fn)
end

-- test
assert(not run [[asdf]])
assert(not run [[print(debug.getinfo(1))]])
assert(env['x'] == nil)
assert(run [[x = 1]])
assert(env.x == 1)
assert(run [[x = 1; y = 2]])
assert(run "function f()\n    return 123\nend")
assert(env.f() == 123)

print 'all ok'
