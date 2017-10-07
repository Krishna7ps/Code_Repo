#
# Cookbook:: apache
# Recipe:: default
#
# Copyright:: 2017, The Authors, All Rights Reserved.

include_recipe

remote_file '/path/to/file' do
  source 'source_file'
  owner 'root'
  group 'root'
  mode '0755'
  action :create
end
