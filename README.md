# wraith-scanner v1.1

nmap in termux = cancer (freezes, SO_ERROR 103, dead terminal)

this fixes it.

### features
- live output (no hang)
- auto save → ~/logs/ (with timestamp)
- just run `python wraith.py` + normal nmap flags
- scan done (finally! 😂)

### usage
```bash
python wraith.py -sS 192.168.1.0/24
python wraith.py -A 10.0.0.1
