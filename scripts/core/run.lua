local M = {}

function M.run(mod, func)
    io.output(io.stderr)
    local errmsg
    xpcall(require(mod)[func],
        function(msg)
            io.write(string.format('\n"%s.%s" execution failed\n%s\n',
                                   mod, func, debug.traceback()))
            errmsg = msg
        end)
    if errmsg ~= nil then
        error(errmsg)
    end
end

return M
