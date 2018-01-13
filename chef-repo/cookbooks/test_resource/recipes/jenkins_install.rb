#
# Cookbook:: .
# Recipe:: jenkins_install
#
# Copyright:: 2017, The Authors, All Rights Reserved.

execute 'update' do
  command 'sudo yum update -y'
 # command 'sudo yum install epel-release -y'
 # command 'sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo'
 # command 'sudo rpm --import http://pkg.jenkins-ci.org/redhat-stable/jenkins-ci.org.key'
 # command 'sudo yum update -y'
  action :run
end


package 'java-1.8.0-openjdk.x86_64' do
  action :install
end


package 'tomcat' do
  action :install
end

service 'tomcat' do
  action [:enable, :start]
end
=begin
    
rescue => exception
    
end
remote_file '/path/to/file' do
  source 'source_file'
  owner 'root'
  group 'root'
  mode '0755'
  action :create
end

=end
