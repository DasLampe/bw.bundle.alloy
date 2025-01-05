defaults = {
    'apt': {
        'packages': {
            'gpg': {
                'installed': True,
            },
        },
    },
    'alloy': {
        'custom_args': [],
        'user': 'alloy',
        'group': 'alloy',
        'remote_prometheus': {
            # 'push_url': 'https://localhost:9009/api/v1/push',
            # 'username': 'prometheus',
            # 'password': 'secret',
        },
        'blackbox': {
            'enable_http_probe': False,
            'http_probes': {
                # 'example.org': {
                #     'address': 'https://example.org',
                # },
            },
            'enable_tcp_probe': False,
            'tcp_probes': {
                # 'second_webserver': {
                #     'address': '127.0.0.1',
                #     'port': '8080',
                # }
            },
        },
        'components': {
            # 'prometheus': {
            #     'scrape': {
            #         'node_exporter': {
            #             'targets': 'prometheus.exporter.unix.node.targets',
            #             'forward_to': '[prometheus.remote_write.global.receiver]',
            #         },
            #     },
            #     'exporter.unix': {
            #         'node': {
            #             'disable_collectors': ["ipvs", "btrfs", "infiniband", "xfs", "zfs", "arp", "bcache", "cpufreq", "nfs", "nfsd", "powersupplyclass", "pressure", "rapl", "tapestats"],
            #             'enable_collectors': ["systemd"],
            #             'filesystem': {
            #                 'fs_types_excluded': '',
            #                 'mount_points_excluded': '',
            #                 'mount_timeout': '',
            #             },
            #             'netclass': {
            #                 'ignored_devices': '',
            #             },
            #             'netdev': {
            #                 'device_exclude': '',
            #             },
            #         }
            #     },
            # },
        },
    },
}
