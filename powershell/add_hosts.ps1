# Add hosts file info
# ./add_hosts.ps1 -add 1.1.1.1 google.com

param (
   [string]$add =" "
)
$username = 'administrator'
$password = '123456'
$securePassword = ConvertTo-SecureString $password -AsPlainText -Force
$credential = New-Object System.Management.Automation.PSCredential $username, $securePassword
Start-Process powershell -arg "start-process powershell '-exec bypass add-content C:\WINDOWS\system32\drivers\etc\hosts ''$add''' -verb runas" -Credential $Credential
