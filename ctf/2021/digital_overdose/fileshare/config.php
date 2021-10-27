<?php
$CONFIG = array (
  'apps_paths' => 
  array (
    0 => 
    array (
      'path' => '/snap/nextcloud/current/htdocs/apps',
      'url' => '/apps',
      'writable' => false,
    ),
    1 => 
    array (
      'path' => '/var/snap/nextcloud/current/nextcloud/extra-apps',
      'url' => '/extra-apps',
      'writable' => true,
    ),
  ),
  'supportedDatabases' => 
  array (
    0 => 'mysql',
  ),
  'memcache.locking' => '\\OC\\Memcache\\Redis',
  'memcache.local' => '\\OC\\Memcache\\Redis',
  'redis' => 
  array (
    'host' => '/tmp/sockets/redis.sock',
    'port' => 0,
  ),
  'log_type' => 'file',
  'logfile' => '/var/snap/nextcloud/current/logs/nextcloud.log',
  'logfilemode' => 416,
  'passwordsalt' => 'fnOGfjWeTHMsaiz5FCQl3dsBLiOdMr',
  'secret' => 'W7gQDN1YyCz/i0JaGUGAGuy0lQwwCtdozIaGHAY362Ol2A73',
  'trusted_domains' => 
  array (
    0 => 'localhost',
    1 => 'fileshare-cloud4n6.gotdns.ch',
  ),
  'datadirectory' => '/var/snap/nextcloud/common/nextcloud/data',
  'dbtype' => 'mysql',
  'version' => '22.1.1.2',
  'overwrite.cli.url' => 'http://localhost',
  'dbname' => 'nextcloud',
  'dbhost' => 'localhost:/tmp/sockets/mysql.sock',
  'dbport' => '',
  'dbtableprefix' => 'oc_',
  'mysql.utf8mb4' => true,
  'dbuser' => 'nextcloud',
  'dbpassword' => 'w5ttejzBeExyqsiIt7mUvSDxkyTHgrXI1tm8rMj2BtQufLuwGUef5ibBafsMkLQl',
  'installed' => true,
  'instanceid' => 'oc70x9zddm1h',
);
