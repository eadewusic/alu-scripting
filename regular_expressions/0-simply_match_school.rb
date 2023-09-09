#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.empty?
  puts "Usage: ./script_name.rb <input_string>"
  exit(1)
end

# Get the input string from the command line argument
input_string = ARGV[0]

# Define the regular expression pattern to match "School" (case-insensitive)
pattern = /[sS]chool/

# Use the regular expression to find matches in the input string
matches = input_string.scan(pattern)

# Join and print the matched text
puts matches.join
