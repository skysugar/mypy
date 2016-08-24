安装依赖包
yum -y install git gcc make patch zlib-devel gdbm-devel openssl-devel sqlite-devel bzip2-devel readline-devel

如果要安装到指定路面设置$PYENV_ROOT环境变量
PYENV_ROOT=/opt/pyenv

开始安装
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash


添加环境变量,一般操作家目录下.bash_profile
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
