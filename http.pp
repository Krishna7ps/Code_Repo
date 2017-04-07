package {'httpd':
    ensure => installed,
}

service { "httpd":
    ensure     => running,
    enable     => true,
    hasrestart => true,
    hasstatus  => true,
    # pattern    => 'httpd',
}