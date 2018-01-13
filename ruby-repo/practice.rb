class Test
    
        def initialize(name)
                @name=name
        end

        def name
            @name
        end

        def password=(password)
            @passwd=password
        end

        def greet(other)
            puts "hello " + other.name() +" !" + "this is "+self.name
        end

end

test1 = Test.new("krishna")
test2 = Test.new("Anjana")

test1.greet(test2)