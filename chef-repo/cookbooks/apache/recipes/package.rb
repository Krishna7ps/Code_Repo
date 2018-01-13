=begin
execute 'yum_update' do
  command 'yum update -y'
  action :run
end
=end

apt_update 'update'

package 'apache2' do
  action :install
end

template '/var/www/html/index.html' do
  source 'index.html.erb'
  action :create
end

service 'apache2' do
  action [ :enable, :start ]
end


