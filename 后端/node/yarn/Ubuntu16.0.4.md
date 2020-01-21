1. `curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -`;
2. `echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list`;
3. `sudo apt-get update && sudo apt-get install yarn`: 安装;
4. `yarn --version`: 查看安装的版本;