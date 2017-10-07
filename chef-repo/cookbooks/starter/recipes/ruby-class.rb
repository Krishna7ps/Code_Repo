class TestClass
    
    def test_method1(x)
        puts "This is test method 1.. Mr #{x}"
    end
    
    def test_method2(y)
        puts "This is test method 2.. Ms #{y}"
    end

    def display
        puts "this all about the class with methods"
    end
    def self.test(a,b)
        puts "parameters are #{a} and #{b}"
    end
end


t1=TestClass.new
print "enter name for male "
x=gets.chomp
print "enter name for female"
y=gets.chomp
puts ""
t1.test_method1(x)
t1.test_method2(y)
print "enter request for method: "
request=gets.chomp


if t1.respond_to?(request)
    t1.__send__(request)
else
    puts "this method can't be part of object"
end


puts t1.test()