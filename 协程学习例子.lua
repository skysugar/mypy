function event()
  while true do
    local client = coroutine.yield()
    local line, err = client:receive()
    print('recve:' .. line)
    client:send('HTTP/1.1 200\r\n\r\nOK')
    client:close()
  end
end



local co = coroutine.create(event)
coroutine.resume(co)

local socket = require("socket")
local server = assert(socket.bind("*", 12345))
print("Server is running on port 12345")

while true do
  local client = server:accept()
  print('Connect from: ' .. client:getpeername())
  coroutine.resume(co, client)
end
