# Problem 01

1. Flow ID열을 삭제하여라
2. Source IP, Destination IP는 inet_aton함수를 이용하여 숫자로 변환하여라
3. Timestamp는 date 패키지를 이용하여 숫자로 변환하여라
4. 결손값(Init_Win_bytes_forward, Init_Win_bytes_backward 열의 -1은 결손값 임 default값은 0)을 채워라
5. Label을(BEGINE, BOT, ...)등을 숫자로 변환 하여라
6. csv파일을 10개로 나눠서 저장하라
7. 정규화를 하여라



---

```python
import socket
import struct

ip = '192.0.0.1'

struct.unpack("!I", socket.inet_aton(ip))[0]
```

---

```python
from datetime import datetime
import time

ss = "7/7/2017 8:59"
timestamp = time.mktime(datetime.strptime(ss,'%m/%d/%Y %H:%M').timetuple())
print(timestamp)
```

