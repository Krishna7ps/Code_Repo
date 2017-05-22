class Test1
    def display
        'this is instance method -- display'
    end
    def self.display
        "This is display method"
    end
end

x=Test1.new
#puts x.display
puts Test1.display   
puts Test1.instance_methods
puts Test1.instance_methods(false)


