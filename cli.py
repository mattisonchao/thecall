import click


@click.group()
def main():
    pass


@main.command()
@click.option('--name', prompt='请输入该服务器的名称', help='服务器名称')
@click.option('--user', prompt='请输入用户名', help='用户名')
@click.option('--host', prompt='请输入IP地址', help='IP 地址')
@click.option('--passwd', prompt='请输入密码', help='密码', hide_input=True)
@click.option('--ssh_login', prompt='是否免密登录', help='是否免密登录，传输 ssh public key', required=False, default=True)
def add(name, user, host, passwd, ssh_login):
    click.echo('args is %s ,%s, %s, %s,%s', name, user, host, passwd, ssh_login)

@main.command()
@click.option('--name', prompt='请输入该服务器的名称', help='服务器名称')
@click.option('--user', prompt='请输入用户名', help='用户名')
@click.option('--host', prompt='请输入IP地址', help='IP 地址')
@click.option('--passwd', prompt='请输入密码', help='密码', hide_input=True)
@click.option('--ssh_login', prompt='是否免密登录', help='是否免密登录，传输 ssh public key', required=False, default=True)
def run():
    click.echo()

if __name__ == '__main__':
    main()
