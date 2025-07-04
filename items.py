config = node.metadata.get('alloy')

pkg_apt = {
    'alloy': {
        'installed': True,
        'needs': [
            'file:/etc/apt/sources.list.d/grafana-alloy.list',
            'action:get_grafana_gpg_key',
            'action:force_update_apt_cache',
        ],
    }
}

svc_systemd = {
    'alloy.service': {
        'running': True,
        'enabled': True,
        'needs': [
            'tag:.pre',
            'pkg_apt:alloy',
        ]
    }
}

actions = {
    'get_grafana_gpg_key': {
        'command': 'curl -s https://apt.grafana.com/gpg.key | gpg --dearmor > /etc/apt/keyrings/grafana.gpg',
        'unless': 'test -f /etc/apt/keyrings/grafana.gpg',
        'needs': [
            'pkg_apt:curl',
            'pkg_apt:gpg',
        ],
        'tags': [
            '.pre'
        ],
        'triggers': [
            'action:force_update_apt_cache',
        ],
    }
}

files = {
    '/etc/apt/sources.list.d/grafana-alloy.list': {
        'content': 'deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main',
        'owner': 'root',
        'group': 'root',
        'tags': [
            '.pre'
        ],
        'triggers': [
            'action:force_update_apt_cache',
        ],
    },
    '/etc/default/alloy': {
        'source': 'etc/default/alloy.j2',
        'content_type': 'jinja2',
        'context': {
            'cfg': config,
        },
        'needs': [
            'pkg_apt:alloy',
        ],
        'triggers': [
            'svc_systemd:alloy.service:restart'
        ]
    },
    '/etc/alloy/config.alloy': {
        'source': 'etc/alloy/config.alloy.j2',
        'content_type': 'jinja2',
        'context': {
            'cfg': config,
        },
        'owner': config.get('user'),
        'group': config.get('group'),
        'needs': [
            'pkg_apt:alloy',
        ],
        'triggers': [
            'svc_systemd:alloy.service:reload',
        ],
    }
}
