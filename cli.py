import click
import json


@click.group()
def main():
    pass


@main.command()
@click.option('--key_path', prompt='密钥路径', help='密钥路径')
def conf(key_path):
    click.echo('config')


@main.command()
@click.option('--name', prompt='请输入该服务器的名称', help='服务器名称')
@click.option('--user', prompt='请输入用户名', help='用户名')
@click.option('--host', prompt='请输入IP地址', help='IP 地址')
@click.option('--passwd', prompt='请输入密码', help='密码', hide_input=True)
@click.option('--ssh_login', prompt='是否免密登录', help='是否免密登录，传输 ssh public key', required=False, default=True)
def add(name, user, host, passwd, ssh_login):
    server = {'name': name, 'user': user, 'host': host, 'passwd': passwd, 'ssh_login': ssh_login}
    server_json = json.dumps(server)
    click.echo(f'add new server {server_json}')


@main.command()
def run():
    click.echo('run the server')


@main.command()
def rm():
    click.echo('remove the server')


if __name__ == '__main__':
    main()
