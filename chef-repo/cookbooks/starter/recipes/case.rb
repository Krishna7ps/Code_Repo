puts "enter age of the player"
age=gets.to_i
puts "the age is #{age.class}"
case age
when 0..20
    puts "this guy is too young to play international"
when 20..30
     "perfect time for play"
when 40..100
    puts "please you retire"
else 
    puts "no more"
end 