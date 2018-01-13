#
# Cookbook:: .
# Recipe:: file_test
#
# Copyright:: 2017, The Authors, All Rights Reserved.

file "file1.txt" do
content "welcome to chef ... file updated"
action :create
end
