local M = {}

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

local function looper_alloc(count_max, machctl, machwork)
    local self = {}

    local prev_time = api_machine_time(machctl)
    local stats_physics = counter_alloc(count_max)
    local stats_input = counter_alloc(count_max)
    local stats_gc = counter_alloc(count_max)
    local stats_control = counter_alloc(count_max)
    local stats_work = counter_alloc(count_max)
    local stats_display_update = counter_alloc(count_max)
    local stats_display_draw = counter_alloc(count_max)
    local stats_frame = counter_alloc(count_max)
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

    function self.update()
        local time = api_machine_time(machctl)
        local dispup, dispdr = api_display_timing()
        stats_physics.sample(api_physics_timing())
        stats_input.sample(api_input_timing())
        stats_gc.sample(api_main_timing())
        stats_control.sample(api_machine_timing(machctl))
        stats_work.sample(api_machine_timing(machwork))
        stats_display_update.sample(dispup)
        stats_display_draw.sample(dispdr)
        stats_frame.sample(time - prev_time)
        prev_time = time
        if stats_frame.count == 0 then
            samples = samples + 1
            api_text_free(text)
            create_text()
            io.write("Physics update:  "..stats_physics.str.."\n")
            io.write("Input update:    "..stats_input.str.."\n")
            io.write("Garbage collect: "..stats_gc.str.."\n")
            io.write("Control step:    "..stats_control.str.."\n")
            io.write("Work step:       "..stats_work.str.."\n")
            io.write("Display update:  "..stats_display_update.str.."\n")
            io.write("Display draw:    "..stats_display_draw.str.."\n")
            io.write("Frame time:      "..stats_frame.str.."\n")
            io.write("-------------------------------------\n")
        end
    end

    io.write("Started recording performance every "..tostring(count_max).." frames\n")
    create_text()
    return self
end

function M.alloc(machctl, machwork)
    local self = {}

    local pressed = 0
    local short = nil
    local long = nil

    function self.free()
        if short ~= nil then
            short.free()
        end
        if long ~= nil then
            long.free()
        end
    end

    function self.update()
        if short ~= nil then
            short.update()
        end
        if long ~= nil then
            long.update()
        end
        if pressed == 0 then
            if api_input_key(KEY()) == 1 then
                pressed = 1
                if short == nil and long == nil then
                    short = looper_alloc(SHORT_FRAMES, machctl, machwork)
                elseif short ~= nil then
                    short.free()
                    short = nil
                    long = looper_alloc(LONG_FRAMES, machctl, machwork)
                elseif long ~= nil then
                    long.free()
                    long = nil
                end
            end
        elseif pressed == 1 then
            if api_input_key(KEY()) == 0 then
                pressed = 0
            end
        end
    end

    return self
end

return M
