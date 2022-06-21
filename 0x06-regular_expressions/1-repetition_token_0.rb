#!/usr/bin/env ruby
#busco palabras con 2 o hasta 5 t repetidas
puts ARGV[0].scan(/hbt{2,5}n/).join
