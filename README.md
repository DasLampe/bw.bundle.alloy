# Bundle to install and configure [Grafana Alloy](https://grafana.com/docs/alloy/latest/)

## Configuration
You can just write your configuration as you would do in a alloy config file, see `metadata.py` for an example.

There are 2 special cases, because of string and list handling:

- Adding a container, e.g. `forward_to = [foo.bar.receiver]` must be written as string `'forward_to': '[foo.bar.receiver]'`
- Using strings, like regex must be written as `key = '"^(autofs|bpf|tmpfs)$"'`

## Special configuration
#### HTTP Probe - Blackbox
To have an easier life, you can define `http_probes` in `blackbox`-exporter metadata.
This will do a `HEAD`-Request to the `address` via HTTP(S)

##### Example
```python
metadata = {
    'blackbox': {
        'enable_http_probe': True,
        'http_probes': {
            'example.org': {
                'address': 'https://example.org'
            },
        },
    },
},
```


#### TCP Probe - Blackbox
For TCP probes and to make the target definition a lot easier, you can use `tcp_probes`

##### Example
```python
metadata = {
    'blackbox': {
        'enable_tcp_probe': True,
        'tcp_probes': {
            'webserver_proxy': {
                'address': '127.0.0.1',
                'port': 8080,
            },
        },
    },
},
```
