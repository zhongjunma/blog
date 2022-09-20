# JavaScript 基础

## 什么是 JavaScript？

JavaScript（JS）是一门动态编程语言。结合 HTML 可以为网站提供动态交互特性。由 Brendan Eich（Mozilla 项目、Mozilla 基金会和 Mozilla 公司的联合创始人）发明。

想要 JS 在 HTML 中生效，需要在 HTML 的 `</body>` 前添加

```html
<script src="scripts/main.js" defer></script>
```

```{note}
在最后一行添加是因为浏览器会按照代码在文件中的顺序加载 HTML，为了避免 HTML 尚未被加载而失效，将 JS 代码放在最后是一个好策略。
```

## 变量

变量的数据类型包括：

| 数据类型 | 解释                                 | 示例                           |
| -------- | ------------------------------------ | ------------------------------ |
| String   | 字符串，单双引号都可以               | `'玛奇玛'`、`"蕾塞"`           |
| Number   | 数字                                 | `10`                           |
| Boolean  | 布尔值，关键字，无需引号             | `true` 和 `false`              |
| Array    | 数组，储存多个值                     | `[1, '玛奇玛', "蕾塞"]`        |
| Object   | **一切皆对象，一切皆可储存在变量里** | `document.querySelector('h1')` |

## 注释

```js
/*
跨行
跨行
*/

// 单行
```

## 运算符

| 运算符 | 符号  |
| ------ | ----- |
| 加     | `+`   |
| 减     | `-`   |
| 乘     | `*`   |
| 除     | `\`   |
| 赋值   | `=`   |
| 等于   | `===` |
| 不等于 | `!=`  |
| 取非   | `!`   |

## 条件语句

```js
if () {

} else {

}
```

## 函数

```js
function funcName(x, y) {
    return x+y
}
```

## 事件

事件为网页添加真实的交互能力。可以捕捉浏览器操作并且运行一些代码作为相应。例如点击事件。

```js
document.querySelector('html').onclick = function() {
    alert('点击页面');
}
```

这段代码的意思是：将匿名函数赋值给了 `html` 的 `onclick` 属性。
