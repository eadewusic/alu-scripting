#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.empty?
  puts "Usage: ./6-phone_number.rb <phone_number>"
  exit(1)
end

# Get the input phone number from the command line argument
phone_number = ARGV[0]

# Define the regular expression pattern
pattern = /^\d{10}$/

# Check if the input phone number matches the pattern
if pattern.match(phone_number)
  puts phone_number
end
