# Define the SSH client configuration file content
$file_content = @(CONTENT)
Host 52.3.253.65
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
CONTENT

# Manage the SSH client configuration file
file { '/etc/ssh/ssh_config': # Path to the SSH client configuration file
  ensure  => file,
  content => $file_content,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}
