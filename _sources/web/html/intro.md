# HTML 简介

## 什么是 HTML？

HTML（**H**yper**T**ext **M**arkup **L**anguage）不是编程语言，是一种标记语言。

详细教程见[学习 HTML ：指南与教程](https://developer.mozilla.org/zh-CN/docs/Learn/HTML)。

HTML 由一系列元素（elements）组成。一个元素的例子：

```html
<p class="editor-note">我的猫咪脾气爆</p>
```

元素包括：

1. 开始标签（Opening tag）`<p>`。
2. 结束标签（Closing tag）`</p>`。
3. 内容（Content）`我的猫咪脾气爆`。
4. 属性（Attribute）`class="editor-note"`，其中，`class` 是属性名称，`editor-note` 是属性值。

一个简单完整的 HTML 页面：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>测试页面</title>
  </head>
  <body>
    <p>测试</p>
  </body>
</html>
```

这个 HTML 包括：

- `<!DOCTYPE html>`，文档类型，当今作用有限，仅用于保证文档正确读取。
- `<html></html>`，包含整个页面的内容。
- `<head></head>`，其内容对用户不可见，主要包括：搜索关键字、页面描述、CSS样式表以及字符编码声明等。
- `<body></body>`，包含用户看到的内容，包括文本、图片、视频、游戏、可播放的音轨或其他内容。

本章内容包括：

- [HTML 元素](html-element)
- [文字处理](html-text)
- [文档与网站架构](html-structure)