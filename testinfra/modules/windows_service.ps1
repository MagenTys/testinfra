Function Exit-Json($obj)
{
    # If the provided $obj is undefined, define one to be nice
    If (-not $obj.GetType)
    {
        $obj = New-Object psobject
    }

    echo $obj | ConvertTo-Json -Compress -Depth 99
    Exit
}

function FindService
{
  param($name)
  $result = Get-WmiObject Win32_Service | Where-Object {$_.Name -eq $name -or $_.DisplayName -eq $name}
  Exit-Json $result
}