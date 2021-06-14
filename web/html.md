# HTML 基础

## 什么是 HTML？

HTML 不是编程语言，是一种标记语言。以下内容整理自 [HTML 基础 - 学习 Web 开发 | MDN](https://developer.mozilla.org/zh-CN/docs/Learn/Getting_started_with_the_web/HTML_basics)

### 元素

HTML 由一系列元素（elements）组成。一个元素的例子：

```html
<p class="editor-note">我的猫咪脾气爆</p>
```

元素包括：

1. 开始标签（Opening tag）`<p>`。
2. 结束标签（Closing tag）`</p>`。
3. 内容（Content）`我的猫咪脾气爆`。
4. 属性（Attribute）`class="editor-note"`，其中，`class` 是属性名称，`editor-note` 是属性值。

元素可以嵌套，称为嵌套元素：

```html
<p class="editor-note">我的猫咪脾气<strong>爆</strong></p>
```

元素内容也可以为空，称为空元素。空元素*没有内容*，也*没有结束标签*：

```html
<img src="../images/asuka.png" alt="明日香">
```

### HTML 文档结构

HTML 是由一系列元素构成的，一个简单完整的 HTML 页面：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>测试页面</title>
  </head>
  <body>
    <img src="images/firefox-icon.png" alt="测试图片">
  </body>
</html>
```

这个 HTML 包括：

- `<!DOCTYPE html>`，文档类型，当今作用有限，仅用于保证文档正确读取。
- `<html></html>`，根元素，包含整个页面的内容。
- `<head></head>`，其内容对用户不可见，主要包括：搜索关键字、页面描述、CSS样式表以及字符编码声明等。
- `<meta charset="utf-8">`，HTML 文档的字符编码声明，UTF-8 已经包括绝大多数人类已知语言的字符，因此比较常用。
- `<title></title>`，页面的标题，显示在浏览器标签页上，或者收藏网页时的描述文字。
- `<body></body>`，包含用户看到的内容，包括文本、图片、视频、游戏、可播放的音轨或其他内容。

## 标签

### 图像

```html
<img src="images/firefox-icon.png" alt="测试图片">
```

`src` 是图像文件的地址，`alt` 是图像的描述内容（用户视觉障碍、图片加载出错时显示）

### 标题（Heading）

HTML 包含 6 级标题，通常使用 3～4 级就够了。

```html
<h1>主标题</h1>
<h2>顶层标题</h2>
<h3>子标题</h3>
<h4>次子标题</h4>
```

### 段落（Paragraph）

通常用于指定常规的文本内容。

```html
<p>这是一个段落</p>
```

### 列表（List）

1. 有序列表（Ordering list），`ol`。
2. 无需列表（Unordering list），`ul`。

列表中的每一个项目用 `li` 来包围。

```html
<p>Mozilla 是一个全球社区，这里聚集着来自五湖四海的</p>

<ul>
  <li>技术人员</li>
  <li>思考者</li>
  <li>建造者</li>
</ul>

<p>我们致力于……</p>
```

#### 链接（Anchor）

```html
<a href="https://www.mozilla.org/zh-CN/about/manifesto/">Mozilla 宣言</a>
```

元素的属性 `href` 指的是“超文本引用（**h**ypertext **ref**erence）”，`href` 的指就是网址的链接，元素的内容是网址的描述内容。
