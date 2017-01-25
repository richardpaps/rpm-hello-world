#Getting an RPM running as service

#Done on CentOS 7 virtualbox iso, must be done on linux machine with systemd/sysV

#Setup

systemctl restart network

yum -y install maven && yum -y install rpm-build

useradd builduser

yum -y install rpm-build rpmdevtools

su - builduser

rpmdev-setuptree

#Using this git as a good example to test what we would need to do to get it running on one of our spring boot apps.
git clone https://github.com/Chomeh/java-rpm-example.git

cd java-rpm-example

#Build package in to target
mvn install

cd target

#Moves package to the rpmbuild/SOURCES
cp myservice-0.1-rpm.tar.gz ~/rpmbuild/SOURCES

#Builds the rpm in SOURCES and moves to RPMS
rpmbuild -ba java-rpm-example.spec

#At this point the rpm can be installed on any machine that takes rpms. Can be installed and run as a service.

su - root

#Installs rpm on to root user to let you run it
yum install ~builduser/rpmbuild/RPMS/noarch/myservice-0.1-1.e17.centos.noarch.rpm

#runs rpm as a service
service myservice start

tail -f /var/log/myservice/myservice.log 

#Lets you check if spring boot app is running
curl http://localhost:8080
