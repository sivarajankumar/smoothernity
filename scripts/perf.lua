local M = {}

local key = require 'key'

local SHORT_FRAMES = 60
local LONG_FRAMES = 600
local KEY = function() return API_INPUT_KEY_F2 end

local function counter_alloc(count_max)
    local self = {}

    local min = math.huge
    local max = 0
    local sum = 0
    self.count = 0
    self.str = "computing..."

    local function avg()
        if self.count > 0 then
            return sum / self.count
        else
            return 0
        end
    end

    function self.sample(value)
        if value < min then
            min = value
        end
        if value > max then
            max = value
        end
        sum = sum + value
        self.count = self.count + 1
        if self.count >= count_max then
            self.str = string.format("%.3f / %.3f / %.3f", min, max, avg())
            min = math.huge
            max = 0
            sum = 0
            self.count = 0
        end
    end

    return self
end

local function looper_alloc(count_max)
    local self = {}

    local stats = {}
    stats.physics = counter_alloc(count_max)
    stats.input = counter_alloc(count_max)
    stats.gc = counter_alloc(count_max)
    stats.storage = counter_alloc(count_max)
    stats.control = counter_alloc(count_max)
    stats.work = counter_alloc(count_max)
    stats.rupdate = counter_alloc(count_max)
    stats.rdraw = counter_alloc(count_max)
    stats.frame = counter_alloc(count_max)
    local samples = 0
    local text = nil

    local function create_text()
        local str = string.format("Recorded %i samples every %i frames", samples, count_max)
        text = api_text_alloc(str, API_TEXT_FONT_8_BY_13, 20, 20)
    end

    function self.free()
        io.write("Finished recording performance\n")
        api_text_free(text)
    end

    function self.sample(name, value)
        stats[name].sample(value)
    end

    function self.update()
        if stats.frame.count == 0 then
            samples = samples + 1
            api_text_free(text)
            create_text()
            io.write("Physics update:  "..stats.physics.str.."\n")
            io.write("Input update:    "..stats.input.str.."\n")
            io.write("Garbage collect: "..stats.gc.str.."\n")
            io.write("Storage update:  "..stats.storage.str.."\n")
            io.write("Control step:    "..stats.control.str.."\n")
            io.write("Work step:       "..stats.work.str.."\n")
            io.write("Render update:   "..stats.rupdate.str.."\n")
            io.write("Render draw:     "..stats.rdraw.str.."\n")
            io.write("Frame time:      "..stats.frame.str.."\n")
            io.write("-------------------------------------\n")
        end
    end

    io.write("Started recording performance every "..tostring(count_max).." frames\n")
    create_text()
    return self
end

function M.alloc()
    local self = {}

    local short = nil
    local long = nil
    local keyctl = nil

    local function pushfunc()
        if short == nil and long == nil then
            short = looper_alloc(SHORT_FRAMES)
        elseif short ~= nil then
            short.free()
            short = nil
            long = looper_alloc(LONG_FRAMES)
        elseif long ~= nil then
            long.free()
            long = nil
        end
    end

    function self.free()
        if short ~= nil then
            short.free()
        end
        if long ~= nil then
            long.free()
        end
    end

    function self.sample(name, value)
        if short ~= nil then
            short.sample(name, value)
        end
        if long ~= nil then
            long.sample(name, value)
        end
    end

    function self.update()
        if short ~= nil then
            short.update()
        end
        if long ~= nil then
            long.update()
        end
        keyctl.update()
    end

    keyctl = key.alloc(KEY, pushfunc, function() end)
    return self
end

return M
