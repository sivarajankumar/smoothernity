local M = {}

function M.alloc()
    self = {}
    local cmds = {}
    local beginid = 0
    local endid = 0
    function self.defer(cmd)
        local id = endid
        endid = endid + 1
        cmds[id] = cmd
        while cmds[id] ~= nil do
            coroutine.yield(true)
        end
    end
    function self.run()
        if cmds[beginid] ~= nil then
            cmds[beginid]()
            cmds[beginid] = nil
            beginid = beginid + 1
        end
    end
    return self
end

return M
