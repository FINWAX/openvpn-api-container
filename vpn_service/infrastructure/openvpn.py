def make_openvpn_connection_command(
        config_path, pid_filepath,
        unknown_options_to_ignore=(), as_one_line=False
):
    cmd = [
        'openvpn',
        '--config', config_path,
        '--daemon',
        '--writepid', pid_filepath,
    ]

    for option in unknown_options_to_ignore:
        cmd.extend(['--ignore-unknown-option', option])

    if as_one_line:
        return ' '.join(cmd)

    return cmd
