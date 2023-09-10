#!/usr/bin/env ruby
# Match "hbtn, htn" not "hbbtn"

puts ARGV[0].scan(/h{1}b{1}?tn{1}/).join
