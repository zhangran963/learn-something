
```sh
No receipt for 'com.apple.pkg.CLTools_Executables' found at '/'.
No receipt for 'com.apple.pkg.DeveloperToolsCLILeo' found at '/'.
No receipt for 'com.apple.pkg.DeveloperToolsCLI' found at '/'.
gyp: No Xcode or CLT version detected!
```
1. `sudo rm -rf $(xcode-select -print-path)`
2. `xcode-select --install`