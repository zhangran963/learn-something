// 命令`pm2 init`生成
// 使用1 `pm2 start`
// 使用2 `pm2 start /path/to/ecosystem.config.js`

module.exports = {
	apps: [
		{
			name: 'app',
			script: './app.js',
			// 默认变量名称
			// 使用 pm2 start ecosystem.config.js
			env: {
				NODE_ENV: 'development'
			},
			// 变量名称: env_<environment-name>
			// 使用 pm2 start ecosystem.config.js --env production
			env_production: {
				NODE_ENV: 'production'
			}
		}
	],
	deploy: {
		production: {
			user: 'ran',  //'远程主机用户名',
			host: '39.106.53.163',   //'远程主机的ssh-config中的别名',
			port: '22',   // '远程主机ssh端口',
			ref: 'origin/master', //远程gitee上的分支
			repo: 'git@github.com:Clayder-ran/mine-server.git',  // 远程仓库地址
            path: '/home/ran/www/mine-server',
            'pre-deploy': 'git fetch --all',  // 部署前执行
			'post-deploy':
				'npm install && pm2 reload ecosystem.config.js --env production' //部署完成后的操作
		}
	}
};
