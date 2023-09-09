#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.empty?
  puts "Usage: ./script_name.rb <input_string>"
  exit(1)
end

# Get the input string from the command line argument
input_string = ARGV[0]

# Use the regular expression pattern to find matches
matches = input_string.scan(/hbt{2,5}n/)

# Join and print the matched text
puts matches.join
