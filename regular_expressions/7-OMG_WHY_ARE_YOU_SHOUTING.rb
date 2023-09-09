#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.empty?
  puts "Usage: ./7-OMG_WHY_ARE_YOU_SHOUTING.rb <input_string>"
  exit(1)
end

# Get the input string from the command line argument
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /[A-Z]/

# Use the regular expression to find matches in the input string
matches = input_string.scan(pattern)

# Join and print the matched capital letters
puts matches.join
