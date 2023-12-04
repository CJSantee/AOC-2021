file = File.open("input.txt")

lines = file.readlines.map(&:chomp)

file.close

puts "Part 1:"

x = lines[0].to_i+1
count = 0
for line in lines
    if line.to_i > x
        count += 1
    end
    x = line.to_i
end

puts count

puts "Part 2:"
sums = []
for i in 0..lines.length-2
    one = lines[i].to_i
    two = lines[i+1].to_i
    three = lines[i+2].to_i
    sums.append(one+two+three)
end

x = sums[0]+1
count = 0
for num in sums
    if num > x
        count += 1
    end
    x = num
end
puts count