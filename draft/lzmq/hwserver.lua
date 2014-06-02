-- Hello World server

require "zhelpers"
local zmq = require "lzmq"

print("Starting")
local context = zmq.context()
local responder, err = context:socket{zmq.REP, bind = "tcp://*:5555"}
responder:bind("ipc://weather.ipc")
zassert(responder, err)
while true do
  print("Listening")
  local buffer = zassert(responder:recv())
  print("Received " .. buffer)
  sleep (1) -- Do some 'work'
  zassert(responder:send("World"))
end
