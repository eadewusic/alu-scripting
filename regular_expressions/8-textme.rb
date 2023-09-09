#!/usr/bin/env ruby

# Check if an argument was provided
if ARGV.empty?
  puts "Usage: ./8-textme.rb <log_entry>"
  exit(1)
end

# Get the log entry from the command line argument
log_entry = ARGV[0]

# Define the regular expression pattern to extract sender, receiver, and flags
pattern = /\[from:([\w+]+)\] \[to:([\w+]+)\] \[flags:([-0-9:]+)\]/

# Use the regular expression to extract sender, receiver, and flags
matches = log_entry.match(pattern)

# Check if the pattern matched successfully
if matches
  sender = matches[1]
  receiver = matches[2]
  flags = matches[3]
  puts "#{sender},#{receiver},#{flags}"
else
  puts "Invalid log entry format."
end
