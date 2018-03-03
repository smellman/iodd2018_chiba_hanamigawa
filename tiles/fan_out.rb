require 'sqlite3'
require 'sequel'
require 'json'
require 'fileutils'
require 'zlib'
require 'stringio'

0.upto(14) {|z|
  dir = "#{z}"
  FileUtils.rm_r(dir) if File.directory?(dir)
}
db = Sequel.sqlite("../hanamigawa.mbtiles")
style = {
  :version => 8,
  :name => 'hanamigawa',
  :sources => {
    'hanamigawa' => {
      :type => 'vector',
      :tiles => './{z}/{x}/{y}.mvt',
      :minzoom => 0,
      :maxzoom => 14,
      :attribution => "e-Stat"
    }
  },
  :layers => [{
    :id => 'hanamigawa',
    :type => 'vector',
    :source => 'hanamigawa'
  }]
}

db[:metadata].all.each {|pair|
  key = pair[:name]
  value = pair[:value]
  next unless %w{center bounds}.include?(key)
  value = value.split(',').map{|v| v.to_f} if %w{center bounds}.include?(key)
  style[:sources]['hanamigawa'][key] = value
}
File.write("style.json", JSON::dump(style))
count = 0
db[:tiles].each {|r|
  z = r[:zoom_level]
  x = r[:tile_column]
  y = (1 << r[:zoom_level]) - r[:tile_row] - 1
  data = r[:tile_data]
  dir = "#{z}/#{x}"
  FileUtils::mkdir_p(dir) unless File.directory?(dir)
  File.open("#{dir}/#{y}.mvt", 'w') {|w|
    w.print Zlib::GzipReader.new(StringIO.new(data)).read
    count += 1
  }
}
print "wrote #{count} tiles.\n"
