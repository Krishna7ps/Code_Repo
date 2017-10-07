file "#{ENV['HOME']}/file1.txt" do
  content 'This is file with env'
  mode '0700'
  owner 'root'
  group 'root'
  action :create
end
