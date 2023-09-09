#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.empty?
  puts "Usage: ./5-beginning_and_end.rb <input_string>"
  exit(1)
end

# Get the input string from the command line argument
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /^h.n$/

# Check if the input string matches the pattern
if pattern.match(input_string)
  puts input_string
end
