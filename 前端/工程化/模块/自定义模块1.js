/**
 * 一般自定义的模块结构
 */


// 定义模块架构
const MyModules = (function Manager() {
	let modules = {}

	// 模块名, 依赖模块, 主体内容
	function define(name, deps, impl) {
		for (let i = 0; i < deps.length; i++) {
			deps[i] = modules[deps[i]]
		}
		// 执行 impl, 以其他模块为参数
		modules[name] = impl.apply(impl, deps)
	}

	function get(name) {
		return modules[name]
	}

	return {
		define,
		get
	}
})();

// 定义bar模块
MyModules.define('bar', [], function () {
	function hello(who) {
		return `let me introduce ${who}`
	}
	return { hello }
})

// 定义foo模块, 此模块依赖 bar模块
MyModules.define('foo', ['bar'], function (Bar) {
	let hungry = 'hippo'

	function toUpperCase(name) {
		console.log(Bar.hello(name || hungry).toUpperCase());
	}

	return { toUpperCase }
})

// 普通调用
let Bar = MyModules.get('bar')
console.log(Bar.hello('四叶草'));
// 有模块依赖的调用
MyModules.get('foo').toUpperCase('四叶草')

