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

@metadata_reactor
def find_http_probes_in_groups(metadata):
    if not metadata.get('alloy/blackbox/enable_http_probe', False):
        raise DoNotRunAgain

    http_probes = {}
    for checked_node in sorted(repo.nodes_in_any_group(metadata.get('alloy/blackbox/http_probes_groups', [])), key=lambda x: x.name):
        if not checked_node.has_bundle('nginx'):
            continue

        for site,site_cfg in checked_node.metadata.get('nginx/sites', {}).items():
            if not site_cfg.get('enabled', False) or not site_cfg.get('monitoring', {}).get('enabled', True):
                continue

            scheme = 'https' if site_cfg.get('ssl', {}) else 'http'
            http_probes[site] = {
                'address': f'{scheme}://{site}',
            }
            for additional_name in site_cfg.get('additional_server_names', []):
                http_probes[additional_name] = {
                    'address': f'{scheme}://{additional_name}',
                }

    return {
        'alloy': {
            'blackbox': {
                'http_probes': http_probes,
            }
        },
    }
