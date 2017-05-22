print "Enter file name to read data from: "
fname=gets
puts "enter name is #{fname}"
n=File.read("#{fname}")
puts n
