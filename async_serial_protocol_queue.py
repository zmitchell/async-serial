import asyncio
import serial
import serial_asyncio
from functools import partial


class Reader(asyncio.Protocol):
    def __init__(self, q):
        """Store the queue.
        """
        super().__init__()
        self.transport = None
        self.buf = None
        self.msgs_recvd = None
        self.q = q

    def connection_made(self, transport):
        """Store the serial transport and prepare to receive data.
        """
        self.transport = transport
        self.buf = bytes()
        self.msgs_recvd = 0
        print('Reader connection created')

    def data_received(self, data):
        """Store characters until a newline is received.
        """
        self.buf += data
        if b'\n' in self.buf:
            lines = self.buf.split(b'\n')
            self.buf = lines[-1]  # whatever was left over
            for line in lines[:-1]:
                asyncio.ensure_future(self.q.put(line))
                self.msgs_recvd += 1
        if self.msgs_recvd == 4:
            self.transport.close()

    def connection_lost(self, exc):
        print('Reader closed')


class Writer(asyncio.Protocol):
    def connection_made(self, transport):
        """Store the serial transport and schedule the task to send data.
        """
        self.transport = transport
        self.buf = bytes()
        print('Writer connection created')
        asyncio.ensure_future(self.send())
        print('Writer.send() scheduled')

    def connection_lost(self, exc):
        print('Writer closed')

    async def send(self):
        """Send four newline-terminated messages, one byte at a time.
        """
        message = b'foo\nbar\nbaz\nqux\n'
        for b in message:
            await asyncio.sleep(0.5)
            self.transport.serial.write(bytes([b]))
            print(f'Writer sent: {bytes([b])}')
        self.transport.close()


async def print_received(loop, q):
    counter = 0
    while counter < 4:
        msg = await q.get()
        print(f'Message received: {msg}')
        counter += 1
    loop.stop()


queue = asyncio.Queue()
reader_partial = partial(Reader, queue)
loop = asyncio.get_event_loop()
reader = serial_asyncio.create_serial_connection(loop, reader_partial, 'reader', baudrate=115200)
writer = serial_asyncio.create_serial_connection(loop, Writer, 'writer', baudrate=115200)
asyncio.ensure_future(reader)
print('Reader scheduled')
asyncio.ensure_future(writer)
print('Writer scheduled')
asyncio.ensure_future(print_received(loop, queue))
loop.run_forever()
print('Done')
