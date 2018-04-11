# eos-scripts
Collection of EOS Scripts

## check\_eos\_bp.py
BP Health check plugin. It follows the [Nagios plugin guidelines](https://nagios-plugins.org/doc/guidelines.html) so it can be used with [Nagios](https://www.nagios.org/
) or any other compatible monitoring software like [Icinga](https://www.icinga.com/
) or [Consul](https://www.consul.io
).

### Dependencies
* Python3

### Usage

```bash
./check_eos_bp.py --help
usage: check_eos_bp.py [-h] [-H HOST] [-p HTTP_PORT] [-p2 P2P_PORT]

Check BP status

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  IP or hostname to check. default = localhost
  -p HTTP_PORT, --http_port HTTP_PORT
                        HTTP port number. default = 8888
  -p2 P2P_PORT, --p2p_port P2P_PORT
                        P2P port number. default = 9876
```
