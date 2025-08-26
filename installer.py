import subprocess as sub
from os import geteuid
"TODO:delete excess element"
distros = {
'debian':'apt install',
'rhel':'yum install',
'arch':'pacman -S',
'opensuse':'zypper install',
'gentoo':'emerge',
'termux':'pkg install'}

def init():
  global installCom
  global isArch
"""
  TODO: remove this comment
  if geteuid != 0:
    print('Exec with sudo')
    exit(2)"""
  print('Init start')
  "TODO:change parh to normal"
  out = sub.run('cat ~/*release | grep "^ID_LIKE="',stdout=sub.PIPE,encoding='utf-8',shell=True)
  idLike = out.stdout.split('=', 1)[-1].strip()

  if idLike == arch: isArch = True
  else: isArch = False

  try:
    installCom = distros[idLike]
    if input(f'Your install command is {installCom} \nIs it?(Y/n):') in ['y','Y','']:
      print('ok')
    else:
      installCom = input('Please input install comand(like: apt install, pacman -S, etc):')
  except KeyError:
     print('ERROR:PACKAGE MANAGER NOT FOUND! ABORDING')
     exit(1)
   print('Init complete') 

def dependencies():
  print('Installation start')
  if !isArch:
    sub.run(f'{installCom} -y zsh curl', shell=True)
  else:
    sub.run(f'{installCom} --noconfim zsh curl', shell=True)
  sub.run('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"',shell=True)
  git clone --depth=1 https://github.com/romkatv/powerlevel10k.git "${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k"
  print('Installation complete')
init()
