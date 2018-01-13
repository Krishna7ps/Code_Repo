file 'test.txt' do
  content 'This is test file'
  action :delete
  owner 'root'
  group 'root'
  mode '0755' 
end
