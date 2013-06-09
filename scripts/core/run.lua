local M = {}

function M.run(mod, func)
    local errmsg
    io.output(io.stderr)
    xpcall(require(mod)[func],
        function(msg)
            io.write(string.format('\n"%s.%s" execution failed%s\n',
                                   mod, func, debug.traceback('', 2)))
            errmsg = msg
        end)
    if errmsg ~= nil then
        error(errmsg)
    end
end

return M
