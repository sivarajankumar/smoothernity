local M = {}

function M.run(th)
    -- TODO: remove begin
    io.write(string.format('thread %i begin\n', th))
    io.write(api_thread_reply(th, string.format('thread %i to main\n', th)))
    io.write(string.format('thread %i end\n', th))
    -- TODO: remove end
end

return M
