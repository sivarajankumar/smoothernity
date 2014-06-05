local script = function(code)
    local env = {yield=coroutine.yield}
    fn, msg = load(code, nil, 't', env)
    if not fn then
        error(msg)
    end
    return fn()
end

--
-- Concepts.
--

add = script([[
    return function(f1, f2)
        local v = nil
        return function()
            if v == nil then
                local v1 = f1()
                yield()
                local v2 = f2()
                yield()
                v = v1 + v2
            end
            return v
        end
    end
]])
mul = script([[
    return function(f1, f2)
        local v = nil
        return function()
            if v == nil then
                local v1 = f1()
                yield()
                local v2 = f2()
                yield()
                v = v1 * v2
            end
            return v
        end
    end
]])
const = script([[
    return function(n)
        return function()
            return n
        end
    end
]])

--
-- Dependency graph.
--

c1 = const(10)
c2 = const(20)
c3 = const(30)
a23 = add(c2, c3)
m123 = mul(c1, a23)

--
-- Runtime
--

check = coroutine.wrap(function()
    assert(c1() == 10)
    assert(c2() == 20)
    assert(c3() == 30)
    assert(a23() == 50)
    assert(m123() == 500)
    return 'ok'
end)

while check() ~= 'ok' do
    print 'step'
end
print 'all ok'
