#/bin/bash
yum clean all
sudo rm -rf /var/cache/yum
yum remove epel-release
rm -rf /etc/yum.repos.d/*
mv CentOS-Base.repo /etc/yum.repos.d/
yum makecache && yum install epel-release

