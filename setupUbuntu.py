import subprocess
from argparse import ArgumentParser as ap


def main():
    parser = ap(description='Simple util for server bootstraping')
    parser.add_argument('-n', action='store', dest='hostname', type=str, help='Server hostname')
    parser.add_argument('-u', action='store', dest='username', type=str, help='Your username')
    parser.add_argument('-d', action='store_true', dest='dirs', help='Create default development directories')
    parser.add_argument('-s', action='store_true', dest='ssh', help='Set default sshd settings')

    args = parser.parse_args()
    if args.dirs:
        subprocess.run(["addgroup", "web"])
        subprocess.run(["mkdir", "/var/www"])
        subprocess.run(["mkdir", "/var/www/html"])
        subprocess.run(["mkdir", "/var/www/apps"])
        subprocess.run(["chown", "-R", ":web", "/var/www"])
        subprocess.run(["chmod", "775", "/var/www"])
        subprocess.run(["chmod", "775", "/var/www/html"])
        subprocess.run(["chmod", "775", "/var/www/apps"])
    if args.hostname:
        subprocess.run(["hostnamectl", "set-hostname", args.hostname])
    if args.username:
        subprocess.run(["adduser", args.username])
        subprocess.run(["usermod", "-aG", "sudo", args.username])
        subprocess.run(["usermod", "-aG", "web", args.username])
        file = open(f'/etc/sudoers.d/{args.username}', 'w')
        file.write(f'{args.username} ALL=(ALL) NOPASSWD:ALL')
        file.close()
    if args.ssh:
        subprocess.run(["cp", "sshd_config.default", "/etc/ssh/sshd_config"])


if __name__ == '__main__':
    main()
